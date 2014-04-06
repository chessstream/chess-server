var chessGames = require('./../lib/chess-games');

// Get home page
exports.index = function(req, res){
  res.render('index', {latestId: chessGames.getLatestId()});
};

// Get game stream page
exports.game = function(req, res){
	var id = parseInt(req.params.gameId);
	if (chessGames.isValidId(id)){
		res.render('game', {fen: chessGames.getFen(id)});
	} else {
		res.render('error', {error: 'This game is not currently active!'});
	}
}