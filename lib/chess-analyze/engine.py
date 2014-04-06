import subprocess

stockfish = subprocess.Popen(["./../../Stockfish/src/stockfish"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def get_best_move(fen, move_time):
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
	
	print "{ bestmove: " + str(bestmove.split()[1]) + ", score: " + analysis + ", isMate: " + ("true" if mate else "false") + " }"

