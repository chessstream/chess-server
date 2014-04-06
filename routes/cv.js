var chessCV = require('./../lib/chess-cv/')
var chessWeb = require('./../lib/chess-web');

exports.analyze = function(req, res){
	var id = req.body.id;
	var img = req.files.img;
	console.log(id);
	console.log(req.files);
	if (!id || !img){
		res.end('error');
	}
	var fen = chessCV.analyze(id, img);
	chessWeb.updateGame(id, fen);
	res.end('success');
}