var socketio = require('socket.io')
  , url = require('url')
  , chessGames = require('./chess-games');
var io;

exports.listen = function(server) {
  io = socketio.listen(server);
  io.set('log level', 2);
  io.sockets.on('connection', function(socket){
    socket.on('init', function(data){
      var path = url.parse(data.url).path;
      var gameId = parseInt(path.substring(1));
      socket.join(gameId);
      console.log(socket.id + " just connected to " + gameId + "!");
    })
  });
}

exports.updateGame = function(id, fen) {
  chessGames.updateGame(id, fen);
  io.sockets.in(id).emit('update', fen);
}