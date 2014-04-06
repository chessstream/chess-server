var socket = io.connect();

$(function(){
  var start = (typeof fen == 'undefined') ? 'start' : fen;
  var board = new ChessBoard('board', {
    pieceTheme: 'bower_components/chessboard.js/img/chesspieces/wikipedia/{piece}.png',
    position: start
  })

  function updateBoard(fen){
    board.position(fen);
  }

  socket.on('update', updateBoard);
});
