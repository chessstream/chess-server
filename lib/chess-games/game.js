var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

// Create a new game object
function ChessGame(id) {
	this.id = id;
	this.created = new Date();
	this.sideToMove = 0;
	this.fen = START_FEN;
	this.analyzed = false;
	this.score = 0;
	this.winChance = 0;
	this.bestMove - '';
}

ChessGame.prototype.updateFEN = function(newFEN) {
	this.sideToMove = 1 - this.sideToMove;
	this.fen = newFEN;
};

exports.new = function(id){
	return new ChessGame(id);
}