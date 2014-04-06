var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

// Create a new game object
function ChessGame(id) {
	this.id = id;
	this.created = new Date();
	this.sideToMove = 0;
	this.fen = START_FEN;
	this.analyzed = true;
	this.score = 0.28;
	this.bestMove = 'e2e4';
}

ChessGame.prototype.updateFEN = function(newFEN) {
	this.analyzed = false;
	this.sideToMove = 1 - this.sideToMove;
	this.fen = newFEN;

	// TODO kick off analysis
};

exports.new = function(id){
	return new ChessGame(id);
};