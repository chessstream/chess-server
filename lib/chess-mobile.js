var id = 0;

// Generate id for new games
exports.genId = function(req, res, next) {
	id++;
	res.end(id.toString());
}