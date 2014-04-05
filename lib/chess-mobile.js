var id = 0;

// Generate id for new games
exports.getNextId = function() {
	return ++id;
}