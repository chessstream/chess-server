var process = require('./subprocess.js');

exports.analyze = function(id, img){
	// if id is not already running a process
	newGame(id);
}

function newGame(id){
	process.generate();
}