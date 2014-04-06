var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
var spawn = require('child_process').spawn;
var path = require('path');

// Create a new game object
function ChessGame(id) {
	this.id = id;
	this.created = new Date();
	this.sideToMove = 0;
	this.fen = START_FEN;
	this.score = 24;
	this.bestMove = 'e2e4';
	this.isMate = false;
}

ChessGame.prototype.updateFEN = function(newFEN, cb) {
	console.log('update self');
	var self = this;
	this.sideToMove = 1 - this.sideToMove;
	this.fen = newFEN;
	console.log(newFEN);

	var child = spawn('python', 
              [path.join(__dirname, '../chess-analyze/engine.py'), this.fen]);

	child.stdout.on('data', function (data) {
		console.log('got some stuff yay!!!');
		var obj = JSON.parse(data);
		self.score = obj.score;
		self.bestMove = obj.bestMove;
		self.isMate = obj.isMate;
		console.log("Checkmate: " + self.isMate);
		cb();
	});


	child.stderr.on('data', function (buffer) {
	    console.log('error: ' + buffer.toString());
	});

	child.on('close', function (code) {
	    if (code !== 0) {
	      console.log('process exited with code ' + code);
	    }
	});
	  
	
};


exports.new = function(id){
	return new ChessGame(id);
};