var chessGames = require('./../lib/chess-games')

// Get id of a game
exports.create = function(req, res){
	res.end(chessGames.createGame().toString());
}

// Manually add a fen string
exports.fen = function(req, res) {
	var id = req.body.id;
	var fen = req.body.fen;
	chessGames.updateGame(id, fen);
	res.end('success');
}