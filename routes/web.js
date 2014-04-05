// Get home page
exports.index = function(req, res){
  res.render('index');
};

// Get game stream page
exports.game = function(req, res){
	res.render('game');
}