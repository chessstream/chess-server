var fs = require('fs')
  , path = require('path');

var chessCV = require('./../lib/chess-cv/')
var chessWeb = require('./../lib/chess-web');

var fileCounter = 0;

exports.analyze = function(req, res){
  var id = req.body.id;
  var img = req.files.img;
  if (!id || !img){
    res.end('error');
  }
  console.log(req.files.img.path);
  var root = path.dirname(require.main.filename);
  fs.rename(path.join('chess-server/', req.files.img.path), path.join('chess-server/', 'uploads/' + fileCounter + '.jpeg'), function(err){
    if (err) throw err;
    console.log('renamed complete');
  });
  var fen = chessCV.analyze(id, img);
  chessWeb.updateGame(id, fen);
  res.end('success');
}