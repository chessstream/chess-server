function createPercentages(whiteInit, blackInit){

  //Config
  whiteColor = "#DD0000";
  blackColor = "#00DD00";
  barHeight = "40px";
  duration = 750;

  
  total = blackInit+whiteInit;
  white = whiteInit/total;
  black = blackInit/total;
  
  var svg = d3.select("#percent-win").append("svg");

  svg.append("g")
    .attr("class", "winPercentGraph");
  
  
  totalWidth = $(".winPercentGraph").parent().width();
  w = {val: white, color: whiteColor, name: "White"};
  b = {val: black, color: blackColor, name: "Black"};
  data = [w, b];
  var items = svg.select(".winPercentGraph")
    .selectAll(".bar")
    .data(data)
    .enter()
    .append("g")
    .attr("class", "bar");
    //.attr("transform", function(d, i) { return "translate("+i*(1-d.val)*totalWidth+", 0)";});

  items.append("rect")
    .attr("fill", function(d) {return d.color;})
    .attr("height", barHeight)
    .transition()
    .ease("bounce")
    .duration(duration)
    .attrTween("x", function(d, i){
      var gen = d3.interpolate(i*totalWidth, i*(1-d.val)*totalWidth);
      return function(t){
        return gen(t);
      };
    })
    .attrTween("width", function(d, i){
      var gen = d3.interpolate(0, d.val*totalWidth);
      return function(t){
        return gen(t);
      };
    });
  items.append("text")
    .attr("transform", function(d, i) {return "translate("+(d.val*totalWidth/2 + i*(1-d.val)*totalWidth)+", 20)";})
    //.attr("dy", "0.5em")
    .attr("fill", "#000000")
    .transition()
    .delay(duration)
    .text(function(d) {return d.name;});

}

function updatePercentages(whiteInit, blackInit){
  //Config
  whiteColor = "#DD0000";
  blackColor = "#00DD00";
  barHeight = "40px";
  duration = 500;

  
  total = blackInit+whiteInit;
  white = whiteInit/total;
  black = blackInit/total;
  
  
  
  totalWidth = $(".winPercentGraph").parent().width();
  w = {val: white, color: whiteColor, name: "White"};
  b = {val: black, color: blackColor, name: "Black"};
  data = [w, b];
 
  console.log(data);

  d3.selectAll(".bar rect")
    .data(data);
    
  console.log(d3.selectAll(".bar rect").data());

  d3.selectAll(".bar text")
    .text(function(d){return "";})
    .data(data);

  d3.selectAll(".bar rect")
    .transition()
    .ease("linear")
    .duration(duration)
    .attrTween("x", function(d, i, a){ 
      return d3.interpolate(a, i*(1-data[i].val)*totalWidth);
    })
    .attrTween("width", function(d, i, a){
      return d3.interpolate(a, data[i].val*totalWidth);
    })

  d3.selectAll(".bar text")
    .attr("transform", function(d, i) {return "translate("+(d.val*totalWidth/2 + i*(1-d.val)*totalWidth)+", 20)";})
    //.attr("dy", "0.5em")
    .attr("fill", "#000000")
    .transition()
    .delay(duration)
    .text(function(d) {return d.name;});


}
  
