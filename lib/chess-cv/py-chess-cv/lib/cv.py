import cv2
import numpy as np
from game import initialize_game
from Square import Square

def crop_img(orig_img, sobel_img):
    #Make it grayscale
    gray = cv2.cvtColor(sobel_img,cv2.COLOR_BGR2GRAY)
    #Compute thresholds, don't need to use adaptive cause it's black and white
    ret,thresh = cv2.threshold(gray,127,255,0)
    #Calculate contours from thresh, no idea what ret is even for.
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Search for the biggest contour
    biggest = None
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            if area > max_area and len(approx)==4:
                biggest = approx
                max_area = area

    x_max = 0;
    x_min = 100000;
    y_max = 0
    y_min = 100000;
    for d in biggest:
       x = d[0][0] 
       y = d[0][1]
       if x > x_max:
           x_max = x
       if x < x_min:
           x_min = x
       if y > y_max:
           y_max = y
       if y < y_min:
           y_min = y
    
    x_start = x_min + 50
    x_end = x_max - 50
    y_start = y_min + 50
    y_end = y_max + 50
    new_original = orig_img[y_start:y_end, x_start:x_end]
    new_sobel = sobel_img[y_start:y_end, x_start:x_end]
    return new_original, new_sobel

# only use horizontal/vertical lines
def valid_line(theta):
    DIFFERENCE = np.pi/120
    ninety = np.pi/2;
    num = theta / ninety - np.floor(theta / ninety)
    return num * (np.pi/2) < DIFFERENCE

def hough_lines(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,175,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,180)
    horizontal_lines = []
    vertical_lines = []
    for rho,theta in lines[0]:
        if (valid_line(theta)):
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            if x1 < -900 and x2 > 900:
              horizontal_lines.append({'rho': rho, 'theta': theta, 'p1': (x1, y1), 'p2': (x2, y2)})
            if y1 > 900 and y2 < -900:
              vertical_lines.append({'rho': rho, 'theta': theta, 'p1': (x1, y1), 'p2': (x2, y2)})
            #cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    return (horizontal_lines, vertical_lines)

THETA_DIFF = np.pi
MAGNITUDE_DIFF = 25

def merge_lines(lines):
    """
    Merge similar lines
    lines: Array of dictionarys with rho and theta attributes
    """
    i = 0
    while i in range(len(lines)):
        j = 0
        while j in range(len(lines)):
            # if lines have same angle
            if (i != j and 
                abs(lines[i]['theta'] - lines[j]['theta']) < THETA_DIFF and 
                abs(lines[i]['rho'] - lines[j]['rho']) < MAGNITUDE_DIFF):
                del lines[j]
                j -= 1
            j+=1
        i+=1

def sort_lines(lines, orientation):
    if orientation == 'horizontal':
        ind = 1
    elif orientation == 'vertical':
        ind = 0
    # sort by average of points
    return sorted(lines, key=lambda line: (line['p1'][ind] + line['p1'][ind])/2)


def find_intersection(line1, line2, sobel_img):
    # diff in x-coordinates for both lines
    diffx1 = line1['p1'][0] - line1['p2'][0]
    diffx2 = line2['p1'][0] - line2['p2'][0]
    # slopes
    m1 = None if (diffx1 == 0) else (line1['p1'][1] - line1['p2'][1]) / diffx1
    m2 = None if (diffx2 == 0) else (line2['p1'][1] - line2['p2'][1]) / diffx2
    # y-intercepts
    b1 = None if (diffx1 == 0) else line1['p1'][1] - m1 * line1['p1'][0]
    b2 = None if (diffx2 == 0) else line2['p1'][1] - m2 * line2['p1'][0]

    # assume we only have 1 vertical line
    if m1 == None:
        x = line1['p1'][0]
    elif m2 == None:
        x = line2['p1'][0]
    else:
        x = ((b2-b1) / (m1-m2))

    # TODO: parallel lines

    y = m1 * x + b1
    cv2.circle(sobel_img, (x, y), 3, (255, 0, 0), 2)
    return (x,y)

def get_squares(horizontal_lines, vertical_lines, orig_img, sobel_img, board_state):
    squares = np.empty(shape=(7,7), dtype=object)
    height, width, depth = orig_img.shape
    square_height = height / 8 
    square_width = width / 8
    for i in range(7):
        for j in range(7):
            orig_square = orig_img[i*square_height:(i+1)*square_height, j*square_width:(j+1)*square_width]
            sobel_square = sobel_img[i*square_height:(i+1)*square_height, j*square_width:(j+1)*square_width]
            squares[i][j] = Square(sobel_square, orig_square, i, j, board_state)
    print(squares)


def find_squares(horizontal_lines, vertical_lines, square_length,orig_img, sobel_img, board_state):
    squares = np.empty(shape=(7,7), dtype=object)
    top_line_ind = 0
    bottom_line_ind = 1
    left_line_ind = 0
    right_line_ind = 1
    # current position on board
    x = 0
    y = 0
 
    while bottom_line_ind < len(horizontal_lines):
        print(left_line_ind, right_line_ind, top_line_ind, bottom_line_ind)
        # when at right end of board
        if right_line_ind >= len(vertical_lines):
            left_line_ind = 0
            right_line_ind = 1
            top_line_ind += 1
            bottom_line_ind += 1
            if bottom_line_ind >= len(horizontal_lines):
                if x == 7 and y == 7:
                    return squares
                raise Exception('Did not find correct number of squares')

        top_line = horizontal_lines[top_line_ind]
        bottom_line = horizontal_lines[bottom_line_ind]
        left_line = vertical_lines[left_line_ind]
        right_line = vertical_lines[right_line_ind]

        # corners of square
        top_left = find_intersection(top_line, left_line, sobel_img)
        top_right = find_intersection(top_line, right_line, sobel_img)
        bottom_left = find_intersection(bottom_line, left_line, sobel_img)
        bottom_right = find_intersection(bottom_line, right_line, sobel_img)

        valid_horizontal_diff = valid_diff(top_left[0], bottom_right[0], square_length)
        valid_vertical_diff = valid_diff(top_left[1], bottom_right[1], square_length)
        if valid_horizontal_diff != 0:
            print('horizontal: ' + str(valid_horizontal_diff))
        if valid_horizontal_diff < 0: # too small
            right_line_ind += 1
        elif valid_horizontal_diff > 0: # too big
            left_line_ind += 1
        
        if valid_vertical_diff != 0:
            print('vertical: ' + str(valid_vertical_diff))
        if valid_vertical_diff < 0: # too small
            bottom_line_ind += 1
        elif valid_vertical_diff > 0:
            top_line_ind += 1

        if valid_square(top_left, bottom_right, square_length):
            # crop squares
            orig_square = orig_img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            sobel_square = sobel_img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            squares[x][y] = Square(sobel_square, orig_square, x, y, board_state)
            cv2.circle(sobel_img, top_left, 3, (255,0,0))
            cv2.circle(sobel_img, top_right, 3, (255,0,0))
            cv2.circle(sobel_img, bottom_left, 3, (255,0,0))
            cv2.circle(sobel_img, bottom_right, 3, (255,0,0))
            cv2.imwrite('output.jpg', sobel_img)
            if x + 1 > 7:
                y = y + 1
                x = 0
            else:
                x = x + 1
            if x == 7 and y == 7:
                return squares
            left_line_ind += 1
            right_line_ind += 1

    if x != 7 or y != 7:
        raise Exception('Did not find correct number of squares')
    return squares

def valid_square(top_left, bottom_right, square_length):
    return (valid_diff(top_left[0], bottom_right[0], square_length) == 0 
            and valid_diff(top_left[1], bottom_right[1], square_length) == 0)

def valid_diff(coord1, coord2, square_length):
    """
    Returns:
        0 : if the distance between two coords is close enough to side length
        1 : if the distance between two coords is too high
        -1 : if the distance between two coords is too low
    """
    SQUARE_LENGTH_THERSHOLD = 20
    diff = abs(coord1 - coord2)
    if (diff > square_length + SQUARE_LENGTH_THERSHOLD):
        return 1
    if (diff < square_length - SQUARE_LENGTH_THERSHOLD):
        return -1
    return 0


def find_everything(orig_img_path, sobel_img_path, board_state=None):
    orig_img_in = cv2.imread(orig_img_path)
    sobel_img_in = cv2.imread(sobel_img_path)
    orig_img, sobel_img = crop_img(orig_img_in, sobel_img_in)

    height, width, depth = orig_img.shape
    NUM_LINES = 10
    AVG_SQUARE_LENGTH = ((height + width) / 2)/NUM_LINES

    horizontal_lines, vertical_lines = hough_lines(sobel_img)
    # print(vertical_lines)

    # more lines than necessary, so merge
    if (len(vertical_lines) * len(horizontal_lines) > 49):
        merge_lines(vertical_lines)
        merge_lines(horizontal_lines)
    vertical_lines = sort_lines(vertical_lines, 'vertical')
    horizontal_lines = sort_lines(horizontal_lines, 'horizontal')

    # add edges to sobel_img
    for vert_line in vertical_lines:
        cv2.line(sobel_img,vert_line['p1'],vert_line['p2'],(0,0,255),2)
    for hori_line in horizontal_lines:
        cv2.line(sobel_img,hori_line['p1'],hori_line['p2'],(0,0,255),2)

    cv2.imwrite('output.jpg', sobel_img)
    return get_squares(horizontal_lines, vertical_lines, orig_img, sobel_img, board_state)

