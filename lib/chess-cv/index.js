var process = require('./subprocess.js');
var processes = {};

exports.analyze = function(id, img){
	process = (processes[id]) ? processes[id] : newGame(id);
}

function newGame(id){
	processes[id] = process.generate();
	return processes[id];
}