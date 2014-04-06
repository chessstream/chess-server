var spawn = require('./subprocess.js').spawn;
var childProcess = require('child_process')

exports.process_vision = function(id, origImg, sobelImg){
  var child = spawn('python', ['py-chess-cv/process_vision.py', origImg.path, sobelImg.path]);

  child.stdout.on('data', function (data) {
    console.log('stdout: ' + data);
  });

  child.stderr.on('data', function (buffer) {
    console.log('error: ' + buffer.toJSON());
  });

  child.on('close', function (code) {
    if (code !== 0) {
      console.log('grep process exited with code ' + code);
    }
  });
}