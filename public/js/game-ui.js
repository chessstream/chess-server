var socket = io.connect();
socket.emit('init', {url: document.URL});

$(function(){
  var start = fen; // fen is set in game view
  var board = new ChessBoard('board', {
    pieceTheme: '/img/chesspieces/{piece}.svg',
    position: start
  });

  function scoreToNatLang(score) {
    var pScore = Math.abs(score);
    if (pScore == 0) {
      return "The game is a draw.";
    } else if (pScore < .25) {
      return "Neither side has a clear advantage.";
    } else if (pScore < .6) {
      return ((score > 0) ? "White" : "Black") + " has a slight advantage.";
    } else if (pScore < 1.2) {
      return ((score > 0) ? "White" : "Black") + " has an advantage.";
    } else if (pScore < 3) {
      return ((score > 0) ? "White" : "Black") + " is winning.";
    } else if (pScore < 5) {
      return ((score > 0) ? "White" : "Black") + " is clearly winning.";
    } else if (pScore < 10) {
      return ((score > 0) ? "White" : "Black") + " is totally destroying the other side.";
    } else {
      return ((score > 0) ? "White" : "Black") + " is about to win in a few moves!";
    }
  }

  /*
   * @game A ChessGame object.
   */
  function updateBoard(game){
    board.position(game.fen);

    // Clear
    $('.analysis-text').html('');

    // Side to move
    var text = "It's <b>" + ((game.sideToMove == 0) ? "white's" : "black's") + "</b> turn to move.";
    $('.analysis-text').append('<p>' + text + '</p>');

    console.log(game.score);
    console.log(game.isMate);

    // Score
    if (game.isMate) {
      // Checkmate
      var score = game.score;
      if (game.sideToMove == 1) {
        score = -score;
      }
      if (score > 0) {
        $('.analysis-text').append('<p>White will win in ' + score + ' moves.');
      } else {
        $('.analysis-text').append('<p>Black will win in ' + -score + ' moves.');
      }
    } else {
      var score = game.score / 100;
      if (game.sideToMove == 1) {
        score = -score;
      }
      $('.analysis-text').append('<p>' + scoreToNatLang(score) + '</p>');
    }

    // Best move
    text = ((game.sideToMove == 0) ? "White" : "Black") + " should do <b>" + game.bestMove + "</b>.";
    $('.analysis-text').append('<p>' + text + '</p>');
  }

  socket.on('update', updateBoard);
});
