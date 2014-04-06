var chessGames = require('./../lib/chess-games.js')

// Get id of a game
exports.create = function(req, res){
	res.end(chessGames.createGame().toString());
}