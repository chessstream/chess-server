var chessCV = require('./../lib/chess-cv/')

exports.analyze = function(req, res){
	var id = req.body.id;
	console.log(id);
	console.log(req.files);
	chessCV.analyze();
	res.end();
}