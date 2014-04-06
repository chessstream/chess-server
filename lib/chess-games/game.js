var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

// Create a new game object
function ChessGame(id) {
	this.id = id;
	this.created = new Date();
	this.sideToMove = 0;
	this.fen = START_FEN;
	this.score = 0;
	this.bestMove = '';
	this.isMate = false;
}

ChessGame.prototype.updateFEN = function(newFEN) {
	this.analyzed = false;
	this.sideToMove = 1 - this.sideToMove;
	this.fen = newFEN;

	stockfish();
};

function stockfish() {
	var stockfish = require('child_process').spawn('./stockfish');
	stockfish.stdin.write('position fen ' + this.fen);
	stockfish.stdin.write('go movetime 1000');

	stockfish.stdout.on('data', function (data) {
	    if (line.indexof("score cp") >= 0) {
	    	score = 
	    	this.isMate = false;
	    } else if (line.indexof("score mate") >= 0) {
	    	score = 
	    	this.isMate = true;
	    } else if (line.indexof("bestmove") >= 0) {
	    	bestMove = line;
	    }
	});
}

exports.new = function(id){
	return new ChessGame(id);
};