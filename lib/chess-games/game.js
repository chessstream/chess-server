var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
var spawn = require('child_process').spawn;

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

	var child = spawn('python ../chess-analyze/engine.py');

	child.stdout.on('data', function (data) {
		console.log('stdout: ' + data);
	});
	  
	
};


exports.new = function(id){
	return new ChessGame(id);
};