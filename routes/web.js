var chessGames = require('./../lib/chess-games');
var chessWeb = require('./../lib/chess-web');
// Get home page
exports.index = function(req, res){
  res.render('index', {latestId: chessGames.getLatestId()});
};

// Get game stream page
exports.game = function(req, res){
	var id = parseInt(req.params.gameId);
	if (chessGames.isValidId(id)){
		res.render('game', {game: chessGames.getGame(id)});
	} else {
		res.render('error', {error: 'This game is not currently active!'});
	}
}

exports.test = function(req, res, next) {
	chessWeb.updateGame(req.params.id, "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 1 1");
	next();
}