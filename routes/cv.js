fs = require('fs');

var chessCV = require('./../lib/chess-cv/')
var chessWeb = require('./../lib/chess-web');

var fileCounter = 0;

exports.analyze = function(req, res){
  var id = req.body.id;
  var img = req.files.img;
  if (!id || !img){
    res.end('error');
  }
  fs.readFile(req.files.img.path, function (err, data) {
    var counter = fileCounter++;
    var newPath = path.join(__dirname, 'uploads/' + counter + '.jpeg');
    fs.writeFile(newPath, data, function (err) {
      res.end('error');
    });
  });
  console.log(id);
  console.log(req.files);
  var fen = chessCV.analyze(id, img);
  chessWeb.updateGame(id, fen);
  res.end('success');
}