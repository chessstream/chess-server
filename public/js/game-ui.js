var socket = io.connect();
socket.emit('init', {url: document.URL});

$(function(){
  var start = fen; // fen is set in game view
  var board = new ChessBoard('board', {
    pieceTheme: '/img/chesspieces/{piece}.svg',
    position: start
  })

  function updateBoard(fen){
    board.position(fen);
  }

  socket.on('update', updateBoard);
});
