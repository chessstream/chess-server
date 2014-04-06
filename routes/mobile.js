var chessGames = require('./../lib/chess-games'),
	chessWeb = require('./../lib/chess-web');

// Get id of a game
exports.create = function(req, res){
	res.end(chessGames.createGame().toString());
}

// Manually add a fen string
exports.fen = function(req, res) {
	var id = req.body.id;
	var fen = req.body.fen;
	console.log(id);
	console.log(fen);
	chessWeb.updateGame(id, fen);
	res.end('success');
}