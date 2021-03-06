// Server
var express = require('express')
  , http = require('http')
  , path = require('path')

// Socket.io
var chessWeb = require('./lib/chess-web')

// Routes
var webRoutes = require('./routes/web')
  , mobileRoutes = require('./routes/mobile')
  , cvRoutes = require('./routes/cv');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser({keepExtensions: true, uploadDir: './files/'}));
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

// Visited from web
app.get('/', webRoutes.index);
app.get('/create', mobileRoutes.create);
app.get('/test/:gameId', webRoutes.test, webRoutes.game);
app.post('/update', cvRoutes.analyze);
app.post('/fen', mobileRoutes.fen);
app.get('/:gameId', webRoutes.game);

var server = http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});

chessWeb.listen(server);