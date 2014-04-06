var chessGame = require('./game.js');

// stores fens of games
var latest_id = 0;
var games = {}

exports.createGame = function() {
	var id = ++latest_id;
	games[latest_id] = chessGame.new(id);
	return id;
} 

exports.updateGame = function(id, fen) {
	if (games[id]) {
		games[id].updateFEN(fen);
	}
}

exports.deleteGame = function(id) {
	delete games[id];
}

exports.getFen = function(id) {
	return games[id].fen;
}

exports.getGame = function(id) {
	return games[id];
}

exports.isValidId = function(id) {
	return (0 < id && id <= latest_id && games[id]);
}

exports.getLatestId = function(id) {
	return latest_id;
}