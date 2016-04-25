var trial;
var cursor = 0
var dataset = []; // Initialize empty array

var canvas_width = 600;
var canvas_height = 600;
var padding = 10; // for chart edges
var actorRadius = 5;

var colors = {
  "mario": {
    "fill": "red",
    "stroke": "blue"
  },
  "toad": {
    "fill": "white",
    "stroke": "red"
  },
  "wall": {
    "fill": "#607d8b",
    "stroke": "#607d8b"
  }

}

// Setup data
function visualization() {
  trial.frames[cursor].points.forEach(function(ele, i) {
    dataset.push(ele);
  });
  cursor++;
  trial.map.forEach(function(ele, i) {
    dataset.push(ele);
  });

  // Create scale functions
  var xScale = d3.scale.linear() // xScale is width of graphic
    .domain([0, d3.max(dataset, function(d) {
      return d.x; // input domain
    })])
    .range([padding, canvas_width - padding * 2]); // output range

  var yScale = d3.scale.linear() // yScale is height of graphic
    .domain([0, d3.max(dataset, function(d) {
      return d.y; // input domain
    })])
    .range([canvas_height - padding, padding]); // remember y starts on top going down so we flip

  // Create SVG element
  var svg = d3.select("#graphic") // This is where we put our vis
    .append("svg")
    .attr("width", canvas_width)
    .attr("height", canvas_height)

  // Create Circles
  svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle") // Add circle svg
    .attr("cx", function(d) {
      return xScale(d.x); // Circle's X
    })
    .attr("cy", function(d) { // Circle's Y
      return yScale(d.y);
    }).attr("fill", function(d) {
      return colors[d.type].fill;
    }).attr("stroke", function(d) {
      return colors[d.type].stroke;
    }).attr("stroke-width", 3)
    .attr("r", actorRadius * (7 / 5)); // radius
  setInterval(function() {
    var numValues = dataset.length; // Get original dataset's length
    dataset = []; // Initialize empty array
    trial.frames[cursor].points.forEach(function(ele, i) {
      dataset.push(ele);
    });
    cursor++;

    // Update circles
    svg.selectAll("circle")
      .data(dataset) // Update with new data
      .transition() // Transition from old to new
      .duration(120) // Length of animation
      .each("start", function() { // Start animation
        d3.select(this) // 'this' means the current element
          .attr("r", actorRadius); // Change size
      })

    .ease("linear") // Transition easing - default 'variable' (i.e. has acceleration), also: 'circle', 'elastic', 'bounce', 'linear'
      .attr("cx", function(d) {
        return xScale(d.x);
      })
      .attr("cy", function(d) {
        return yScale(d.y);
      })
      .each("end", function() { // End animation
        d3.select(this) // 'this' means the current element
          .transition()
          .duration(100)
      });
  }, 100);
}

window.onload = function() {
  dataTrial = document.getElementById('trial').innerHTML;
  d3.json(dataTrial, function(error, json) {
    if (error) return console.warn(error);
    trial = json;

    visualization();
  });
}
