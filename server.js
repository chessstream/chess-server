var express = require('express')
  , routes = require('./routes')
  , http = require('http')
  , path = require('path')
  , chessWeb = require('./lib/chess-web.js')
  , chessMobile = require('./lib/chess-mobile.js');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

// Web
app.get('/', routes.index);
app.get('/game/:gameId', routes.game);

// Mobile
app.get('/id', chessMobile.genId);

var server = http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});

chessWeb.listen(server);