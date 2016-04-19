var express = require("express");
var app = express();


//Middleware
var port = process.env.PORT || 3000;
var strings = require('./strings.json');
app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs');


app.get('/', function(req, res) {
  res.render(__dirname + '/view/pages/display.ejs',{strings: strings});
});


app.listen(port);
console.log("live at: " + port);
