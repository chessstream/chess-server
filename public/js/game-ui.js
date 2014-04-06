var socket = io.connect();
socket.emit('init', {url: document.URL});

$(function(){
  var start = game.fen; // fen is set in game view
  var board = new ChessBoard('board', {
    pieceTheme: '/img/chesspieces/{piece}.svg',
    position: start
  });

  /*
   * @game A ChessGame object.
   */
  function updateBoard(game){
    board.position(game.fen);
    $('.analysis-text').html('');
    $('.analysis-text').append('<p>' + (game.sideToMove === 0) ? 'White' : 'Black' + ' to move</p>');
  }

  socket.on('update', updateBoard);
  updateBoard(game);
});
