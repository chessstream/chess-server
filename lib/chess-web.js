var socketio = require('socket.io')
  , url = require('url')
  , chessGames = require('chessGames');
var io;

exports.listen = function(server) {
  io = socketio.listen(server);
  io.set('log level', 2);
  io.sockets.on('connection', function(socket){
    var path = url.parse(data.url).path;
    var gameId = parseInt(path.substring(1));
    socket.join(gameId);
    console.log(socket.id + " just connected!");
  });
}

exports.updateGame = function(id, fen) {
  chessGames.updateGames(id, fen);
  io.sockets.in(id).emit('update', fen);
}