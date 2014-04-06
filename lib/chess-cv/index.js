var spawn = require('child_process').spawn;
var path = require('path');

exports.process_vision = function(id, origImg, sobelImg){
  var child = spawn('python', 
              [path.join(__dirname, 'py-chess-cv/process_vision.py'), origImg.path, sobelImg.path], function(){
                
              });

  child.stdout.on('data', function (buffer) {
    console.log('stdout: ' + buffer.toString());
  });

  child.stderr.on('data', function (buffer) {
    console.log(buffer.toString());
  });

  child.on('close', function (code) {
    if (code !== 0) {
      console.log('process exited with code ' + code);
    }
  });
}