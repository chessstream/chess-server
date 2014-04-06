import subprocess

stockfish = subprocess.Popen(["./../../Stockfish/src/stockfish"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def get_best_move(fen, move_time):
	# moves_as_str = ' '.join(moves_list)
	# stockfish.stdin.write(('setoption name Threads value 4\n').encode('utf-8'))
	# stockfish.stdin.flush()
	# stockfish.stdin.write(('setoption name Hash value 512\n').encode('utf-8'))
	# stockfish.stdin.flush()
	# stockfish.stdin.write(('setoption name OwnBook value true\n').encode('utf-8'))
	# stockfish.stdin.flush()
	# stockfish.stdin.write(('setoption name Skill Level value ' + skill_level + '\n').encode('utf-8'))
	# stockfish.stdin.flush()
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
			analysis = line.split('multipv')[0]
			mate = False
		elif "score mate" in line:
			analysis = line.split('multipv')[0]
			mate = True
		elif "bestmove" in line:
			bestmove = line
			mate = False
			break
	
	return bestmove.split()[1], analysis, mate

