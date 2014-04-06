var socket = io.connect();
socket.emit('init', {url: document.URL});

$(function(){
  var start = fen; // fen is set in game view
  var board = new ChessBoard('board', {
    pieceTheme: 'bower_components/chessboard.js/img/chesspieces/wikipedia/{piece}.png',
    position: start
  })

  function updateBoard(fen){
    board.position(fen);
  }

  socket.on('update', updateBoard);
});
