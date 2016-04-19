var trial;
    function buildWall(){
    for(var i =0;i<trial.map.length;i++){
      dataset.push([trial.map[i].x,trial.map[i].y]);
    }
    }
    var cursor = 0
        var dataset = []; // Initialize empty array

      // Setup data
     function visualization(){
    for (var i = 0; i < trial.frames[cursor].points.length; i++) {
      var frame = trial.frames[cursor].points[i];
      dataset.push([frame.x, frame.y]); // Add new number to array
    }
    cursor++;
    buildWall();

    // Setup settings for graphic
    var canvas_width = 460;
    var canvas_height = 460;
    var padding = 10; // for chart edges

    // Create scale functions
    var xScale = d3.scale.linear() // xScale is width of graphic
      .domain([0, d3.max(dataset, function(d) {
        return d[0]; // input domain
      })])
      .range([padding, canvas_width - padding * 2]); // output range

    var yScale = d3.scale.linear() // yScale is height of graphic
      .domain([0, d3.max(dataset, function(d) {
        return d[1]; // input domain
      })])
      .range([canvas_height - padding, padding]); // remember y starts on top going down so we flip

    // Define X axis

    // Create SVG element
    var svg = d3.select("h3") // This is where we put our vis
      .append("svg")
      .attr("width", canvas_width)
      .attr("height", canvas_height)

    // Create Circles
    svg.selectAll("circle")
      .data(dataset)
      .enter()
      .append("circle") // Add circle svg
      .attr("cx", function(d) {
        return xScale(d[0]); // Circle's X
      })
      .attr("cy", function(d) { // Circle's Y
        return yScale(d[1]);
      })
      .attr("r", 7); // radius

    // On click, update with new data
    setInterval(function() {
      var numValues = dataset.length; // Get original dataset's length
      dataset = []; // Initialize empty array
      for (var i = 0; i < trial.frames[cursor].points.length; i++) {
        var frame = trial.frames[cursor].points[i];
        dataset.push([frame.x, frame.y]); // Add new number to array
      }
      cursor++;



      // Update circles
      svg.selectAll("circle")
        .data(dataset) // Update with new data
        .transition() // Transition from old to new
        .duration(120) // Length of animation
        .each("start", function() { // Start animation
          d3.select(this) // 'this' means the current element
            .attr("fill", "red") // Change color
            .attr("r", 5); // Change size
        })

      .ease("linear") // Transition easing - default 'variable' (i.e. has acceleration), also: 'circle', 'elastic', 'bounce', 'linear'
        .attr("cx", function(d) {
          return xScale(d[0]); // Circle's X
        })
        .attr("cy", function(d) {
          return yScale(d[1]); // Circle's Y
        })
        .each("end", function() { // End animation
          d3.select(this) // 'this' means the current element
            .transition()
            .duration(100)
        });


    }, 100);
}

window.onload= function(){
  dataTrial = document.getElementById('trial').innerHTML;
  d3.json(dataTrial, function(error, json) {
    if (error) return console.warn(error);
    trial = json;

    visualization();
  });
}
