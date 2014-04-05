var chessMobile = require('./../lib/chess-mobile.js')

// Get id of a game
exports.getId = function(req, res){
	res.end(chessMobile.getNextId().toString());
}