var chessGames = require('./../lib/chess-games')

// Get id of a game
exports.create = function(req, res){
	res.end(chessGames.createGame().toString());
}