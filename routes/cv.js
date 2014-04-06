var chessCV = require('./../lib/chess-cv/')
var chessWeb = require('./../lib/chess-web');

exports.analyze = function(req, res){
	var id = req.body.id;
	var origImg = req.files.original;
	var sobelImg = req.files.sobel;
	if (!id || !origImg || !sobelImg){
		res.end('error');
	}
	var boardState = chessCV.process_vision(id, origImg, sobelImg);
	// chessWeb.updateGame(id, bo);
	res.end('success');
}