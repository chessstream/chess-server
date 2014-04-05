var process = require('./subprocess.js');

exports.lookUpGame = function(id){
	// if id is not already running a process
	newGame(id);
}

function newGame(id){
	process.generate();
}