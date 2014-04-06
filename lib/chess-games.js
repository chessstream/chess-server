// stores fens of games
var latest_id = 0;
var games = {}
var START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

exports.createGame = function() {
	var id = ++latest_id;
	games[latest_id] = START_FEN;
	return id;
} 

exports.updateGame = function(id, fen) {
	if (games[id]) {
		games[id] = fen;
	}
}

exports.deleteGame = function(id) {
	delete games[id];
}

exports.getFen = function(id) {
	return games[id];
}

exports.isValidId = function(id) {
	return (0 < id && id <= latest_id && games[id]);
}