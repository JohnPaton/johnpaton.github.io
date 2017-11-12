title: Remapping the world with word vectors
slug: remapping-the-world
date: 2017-10-30 20:00:00 UTC+01:00
tags: natural language, dataviz, d3.js
status: draft
description:
type: text
author: John Paton
summary: 


<!--
<style>

.links line {
  stroke: #999;
  stroke-opacity: 0.6;
}

.nodes circle {
  stroke: #fff;
  stroke-width: 1.5px;
}

</style>
-->
<svg width="600" height="500"></svg>

<script src="https://d3js.org/d3.v4.min.js"></script>
<script>

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("charge", d3.forceManyBody().strength(-150))
    .force("collide", d3.forceCollide().radius(rad))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .velocityDecay(0.7);

function rad(d){
    return Math.max(2, 25* Math.pow(d.area, 1/3));
};

d3.json("/static/graph.json", function(error, graph) {
  if (error) throw error;

  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", 2)
      .attr("stroke", "#999")
      .attr("stroke-opacity", function(d) {return 0.5*Math.pow(d.strength, 2); });


//function(d) { return color(d.region); })

  var node = svg.append("g")
      .attr("class", "nodes")
      .selectAll(".node")
      .data(graph.nodes)
      .enter()
      .append("g")
        .attr("class","node")
        .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

    node.append("circle")
        .attr("r", rad)
        .attr("fill", "red")


    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  //   .selectAll("circle")
  //   .data(graph.nodes)
  //   .enter().append("circle")
  //     .attr("cx", function(d) {return d.x; })
  //     .attr("cy", function(d) {return d.y; })
  //     .attr("r", rad)
  //     .attr("fill", "red")
  //     .call(d3.drag()
  //         .on("start", dragstarted)
  //         .on("drag", dragged)
  //         .on("end", dragended));

  node.append("text")
      .text(function(d) { return d.commonName; })
        .attr("alignment-baseline","middle")
        .attr("text-anchor", "right")
        .attr("dx", rad)
        .attr("font-family","sans-serif")
        .attr("font-size","9pt")
        .attr("opacity","0.5")

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link", d3.forceLink()
                             .links(graph.links)
                             .strength(function(d) {return 5*(Math.pow(d.strength, 4)); })
                             .distance(function(d) {return 200*(1-Math.pow(d.strength, 2)); }));

    function boxx(d){
        return Math.min(Math.max(rad(d), d.x), width-rad(d)-100);
    }

    function boxy(d){
        return Math.min(Math.max(rad(d), d.y), height-rad(d)-5);
    }

  function ticked() {
    link
        .attr("x1", function(d) { return boxx(d.source); })
        .attr("y1", function(d) { return boxy(d.source); })
        .attr("x2", function(d) { return boxx(d.target); })
        .attr("y2", function(d) { return boxy(d.target); });

    node
        .attr("transform", function(d) { return "translate(" + boxx(d) + "," + boxy(d) + ")"; })
        .attr("cx", function(d) { boxx(d); })
        .attr("cy", function(d) { boxy(d) });
  }
});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

</script>
