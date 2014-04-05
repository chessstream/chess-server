var socketio = require('socket.io');
var io;

exports.listen = function(server) {
	io = socketio.listen(server);
	io.set('log level', 2);
	io.sockets.on('connection', function(socket){
		console.log(socket.id + " just connected!");
	});
}