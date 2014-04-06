var chessCV = require('./../lib/chess-cv/')

exports.analyze = function(req, res){
	var id = req.body.id;
	var img = req.files.img;
	console.log(id);
	console.log(req.files);
	if (!id || !img){
		res.end('error');
	}
	chessCV.analyze(id, img);
	res.end('success');
}