import game, cv
from Square import Square
import json

def start_game(orig, sobel):
    squares = cv.find_everything(orig, sobel)
    info = game.initialize_game(squares)
    # fen = info['fen']
    # output = {fen: fen, game_state: info}
    print info
    return info

def process_input(orig, sobel, board_state):
    try:
        squares = cv.find_everything(orig, sobel, board_state)
        info = game.update_game(squares, board_state)
        print info
        return info
    except:
        pass