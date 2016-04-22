var express = require("express");
var app = express();
var fs = require("fs");
var minify = require('express-minify');



//Middleware
var port = process.env.PORT || 3000;
var strings = require('./strings.json');

app.use(minify());
app.use(express.static(__dirname + '/public'));
app.use(express.static(__dirname + '/data'));

app.set('view engine', 'ejs');


app.get('/', function(req, res) {
  fs.readdir("./data", function(err, files) {
    if(err) console.log(err);

    res.render(__dirname + '/view/pages/home.ejs', {
      strings: strings,
      trials: files
    });
  });
});

app.get('/theatre', function(req, res) {
  fs.readFile(__dirname + '/data/' + req.query.trial,function(err,file){
    var trialData = JSON.parse(file);
    res.render(__dirname + '/view/pages/theatre.ejs', {
      strings: strings,
      trial: {"fileName":req.query.trial,"metadata":trialData}
    });
  });
});


app.listen(port);
console.log("live at: " + port);
