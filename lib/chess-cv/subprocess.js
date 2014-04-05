var childProcess = require('child_process');

// Generates a new process
exports.generate = function(){
	return new SubProcess();
}

function SubProcess() {
	this.child = childProcess.spawn('python', ['-u', '-i']);
}

SubProcess.prototype.run = function(commmand, cb) {

}