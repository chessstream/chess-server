import subprocess
import sys
import os
import json

def get_best_move(fen, move_time):

	# print os.getcwd()

	stockfish = subprocess.Popen(["./lib/chess-analyze/stockfish"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

	stockfish.stdin.write(('position fen ' + fen + '\n').encode('utf-8'))
	stockfish.stdin.flush()
	stockfish.stdin.write(('go movetime ' + move_time + '\n').encode('utf-8'))
	stockfish.stdin.flush()

	bestmove = ""
	analysis = ""
	mate = False

	while True:
		line = stockfish.stdout.readline().decode().rstrip()
		if "score cp" in line:
			analysis = line.split()[7]
			mate = False
		elif "score mate" in line:
			analysis = line.split()[7]
			mate = True
		elif "bestmove" in line:
			bestmove = line
			mate = False
			break
	
	dictionary = {"bestMove": bestmove.split()[1], "score": analysis, "isMate": mate}
	print json.dumps(dictionary)

if len(sys.argv) == 2:
	get_best_move(sys.argv[1], "1000")