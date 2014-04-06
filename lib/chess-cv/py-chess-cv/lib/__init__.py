import game, cv
from Square import Square
import json

def start_game(orig, sobel):
    squares = cv.find_everything(orig, sobel)
    info = game.initialize_game(squares)
    fen = info['fen']
    output = {fen: fen, game_state: info}
    print output
    return json.encode(output)

def process_input(orig, sobel, board_state):
    squares = cv.find_everything(orig, sobel, board_state)
    
    
