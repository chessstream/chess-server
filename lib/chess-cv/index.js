var process = require('./subprocess.js');
var childProcess = require('child_process')

exports.process_vision = function(id, origImg, sobelImg){
  var child = childProcess.spawn('python', ['py-chess-cv/process_vision.py', origImg.path, sobelImg.path]);

  child.stdout.on('data', function (data) {
    console.log('stdout: ' + data);
  });

}