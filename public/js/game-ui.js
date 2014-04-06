var socket = io.connect();
socket.emit('init', {url: document.URL});

$(function(){
  var start = fen; // fen is set in game view
  var board = new ChessBoard('board', {
    pieceTheme: '/img/chesspieces/{piece}.svg',
    position: start
  });

  /*
   * @game A ChessGame object.
   */
  function updateBoard(game){
    board.position(game.fen);
    // TODO update the stats
  }

  socket.on('update', updateBoard);
});
