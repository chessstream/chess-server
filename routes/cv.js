var chessCV = require('./../lib/chess-cv/')

exports.analyze = function(req, res){
	chessCV.analyze();
	res.end();
}