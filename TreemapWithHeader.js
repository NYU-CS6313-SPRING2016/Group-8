function render_treemap(data, slt) {
   

    
    d3.select("#treemap svg").remove();

    var supportsForeignObject = true;
    var chartWidth = 700;       // treemap width
    var chartHeight = 500;      // treemap height
    var xscale = d3.scale.linear().range([0, chartWidth]);
    var yscale = d3.scale.linear().range([0, chartHeight]);
    var color = d3.scale.category10();
    var headerHeight = 20;
    var headerColor = "#999999";
    var transitionDuration = 500;
    var root;
    var node;

    var treemap = d3.layout.treemap()
        .round(false)
        .size([chartWidth, chartHeight])
        .sticky(true)
        .value(function(d) {
            return Math.sqrt(Math.pow(d.value, 1.5));
        });

    var chart = d3.select("#treemap")
        .append("svg:svg")
        .attr("width", 700)
        .attr("height", 500)
        .append("svg:g");

        node = root = data;
        var nodes = treemap.nodes(data);

        var children = nodes.filter(function(d) {
            return !d.children;     // leaves, nodes which don't have children
        });
        var parents = nodes.filter(function(d) {
            return d.children;      // nodes who are not leaves
        });

        // create parent cells
        var parentCells = chart.selectAll("g.cell.parent")
            .data(parents, function(d) {
                return "p-" + d.name;
            });
        var parentEnterTransition = parentCells.enter()
            .append("g")
            .attr("class", "cell parent")
            .on("click", function(d) {
                zoom(d);
            });
        parentEnterTransition.append("rect")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) { return d.dy; })
            .style("fill", "#999999");
        parentEnterTransition.append('foreignObject')
            .attr("class", "foreignObject")
            
        // update transition
        var parentUpdateTransition = parentCells.transition().duration(transitionDuration);
        parentUpdateTransition.select(".cell")
            .attr("transform", function(d) {
                return "translate(" + d.dx + "," + d.y + ")";
            });
        parentUpdateTransition.select("rect")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) { return d.dy; })
            .style("fill", "#999999");
        parentUpdateTransition.select(".foreignObject")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) {return d.dy; })      // added "0.01, "
            
            .text(function(d) {
                return d.name;        // sector name
            });
        // remove transition
        parentCells.exit()
            .remove();

        // create children cells
        var childrenCells = chart.selectAll("g.cell.child")
            .data(children, function(d) {
                return "c-" + d.name;       // symbol name
            });
        // enter transition
        var childEnterTransition = childrenCells.enter()
            .append("g")
            .attr("class", "cell child")
            .attr("id", function(d){ return d.s_id })
            .style('stroke-width', '2px')
            .style('stroke', '#aaaaaa')
            .style('stroke-opacity', 0.5)
            /*---------------------------------------------------------- change one below------------------------------------------------------------*/
            .on("click", function(d) {    // disable this, can't zoom into sectors
//                zoom(node === d.parent ? root : d.parent);
                    if (node !== d.parent) {
                        zoom(d.parent);
                    } else {
                        d3.selectAll("g.cell.child").style('stroke-width', '2px')
                                                    .style('stroke', '#aaaaaa')
                                                    .style('stroke-opacity', 0.5);
                        d3.select(this).style('stroke', 'black')
                                        .style('stroke-width', '3px')
                                        .style('stroke-opacity', 1);
                        console.log(d);         
                        changestock(d, d.name, slt);
                    }
            })
            .on("dblclick", function(d){
                zoom(node === d.parent?root : d.parent);
            })
            
            /* remain to be inspected
            .on("mouseover", function(d) {
                $("#" + d.s_id).css("background", "#424242");
                $("#treemap #" + d.s_id + " rect").css("stroke-width","6");
            })
            .on("mouseout", function(d) {
                $("#" + d.s_id).css("background", "#777777");
                $("#treemap #" + d.s_id + " rect").css("stroke-width","1");
            })*/        // change one, delete
            ;

        childEnterTransition.append("rect")
            .classed("background", true)
            .style("fill", function(d) {
                return color(d.parent.name);
            });
        childEnterTransition.append('foreignObject')
            .attr("class", "foreignObject")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) {
                return Math.max(0.01, d.dy);
            })
            
/*------------------------------------------------------text alignment problem is here!------------------------------------------------------*/
//            .append("text")
//            .attr("x",function(d) {return d.x + d.dx/2})
//            .attr("y",function(d) {return d.y + d.dy/2})
//            .attr("text-anchor","middle")
//            .attr("font-size", "10")
//            .attr("font-weight", "normal")
            .text(function(d) {
                return d.name;        // symbol name
            })
;

        // if (supportsForeignObject) {
        //     childEnterTransition.selectAll(".foreignObject")
        //         .style("display", "none");
        // } else {
        //     childEnterTransition.selectAll(".foreignObject .labelbody .label")
        //         .style("display", "none");
        // }

        // update transition
        var childUpdateTransition = childrenCells.transition().duration(transitionDuration);
        childUpdateTransition.select(".cell")
            .attr("transform", function(d) {
                return "translate(" + d.x  + "," + d.y + ")";
            });
        childUpdateTransition.select("rect")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) {
                return d.dy;
            })
            .style("fill", function(d) {
                return color(d.parent.name);
            });
        childUpdateTransition.select(".foreignObject")
            .attr("width", function(d) {
                return Math.max(0.01, d.dx);
            })
            .attr("height", function(d) {
                return Math.max(0.01, d.dy);
            })
           
            .text(function(d) {
                return d.name;      // sector name
            })

        // exit transition
        childrenCells.exit()
            .remove();
/*---------------------------------------------------------- change two below------------------------------------------------------------*/
// specific feature for original example, doesn't matter
/*        d3.select("select").on("change", function() {
            console.log("select zoom(node)");
            treemap.value(this.value == "size" ? size : count)
                .nodes(root);
            zoom(node);
        });*/       // change two, delete
/*---------------------------------------------------------- change three below------------------------------------------------------------*/
        childrenCells.on("mouseenter", function(d) {
                 //       highlight(d.name);
                        d3.select("#tooltip").style({
                            visibility: "visible",
                            top: d3.event.clientY,
                            left: (d3.event.clientX + 10),
                            opacity: 1,
                        }).text("Symbol: " + d.name + '\nTitle: ' + d.title + '\nSector: '+ d.parent.name+ '\nExchange: ' + d.exchange)     // inside the text parameter we do not call another function
                    })
                    .on("mouseleave", function(d) {
                 //       unHighlight();
                        d3.select("#tooltip").style({
                            visibility: "hidden",
                            opacity: 0,
                        });
                    });     // change three, added

        zoom(node);
    // });


    function size(d) {
        return d.size;
    }


    function count(d) {
        return 1;
    }


    //and another one
    function textHeight(d) {
        var ky = chartHeight / d.dy;
        yscale.domain([d.y, d.y + d.dy]);
        return (ky * d.dy) / headerHeight;
    }


    function getRGBComponents (color) {
        var r = color.substring(1, 3);
        var g = color.substring(3, 5);
        var b = color.substring(5, 7);
        return {
            R: parseInt(r, 16),
            G: parseInt(g, 16),
            B: parseInt(b, 16)
        };
    }


    function idealTextColor (bgColor) {
        var nThreshold = 105;
        var components = getRGBComponents(bgColor);
        var bgDelta = (components.R * 0.299) + (components.G * 0.587) + (components.B * 0.114);
        // return ((255 - bgDelta) < nThreshold) ? "#000000" : "#ffffff";
        return ((255 - bgDelta) < nThreshold) ? "#ffffff" : "#ffffff";
    }


    function zoom(d) {
        treemap
            .padding([headerHeight/(chartHeight/d.dy), 4, 4, 4])
            .nodes(d);

        // moving the next two lines above treemap layout messes up padding of zoom result
        var kx = chartWidth  / d.dx;
        var ky = chartHeight / d.dy;
        var level = d;

        xscale.domain([d.x, d.x + d.dx]);
        yscale.domain([d.y, d.y + d.dy]);

        if (node != level) {
            if (supportsForeignObject) {
                chart.selectAll(".cell.child .foreignObject")
                    // .style("display", "none");
                    .style("display", "");
            } else {
                chart.selectAll(".cell.child .foreignObject ")
                    .style("display", "none");
            }
        }

        var zoomTransition = chart.selectAll("g.cell").transition().duration(transitionDuration)
            .attr("transform", function(d) {
                return "translate(" + xscale(d.x) + "," + yscale(d.y) + ")";
            })
            .each("end", function(d, i) {
                if (!i && (level !== self.root)) {
                    chart.selectAll(".cell.child")
                        .filter(function(d) {
                            return d.parent === self.node; // only get the children for selected group
                        })
                        .select(".foreignObject")
                        .style("color", function(d) {
                            return idealTextColor(color(d.parent.name));
                        });

                    if (supportsForeignObject) {
                        chart.selectAll(".cell.child")
                            .filter(function(d) {
                                return d.parent === self.node; // only get the children for selected group
                            })
                            .select(".foreignObject")
                            .style("display", "");
                    } else {
                        chart.selectAll(".cell.child")
                            .filter(function(d) {
                                return d.parent === self.node; // only get the children for selected group
                            })
                            .select(".foreignObject")
                            .style("display", "");
                    }
                }
            });

        zoomTransition.select(".foreignObject")
            .attr("width", function(d) {
                return Math.max(0.01, kx * d.dx);
            })
            .attr("height", function(d) {
                return d.children ? (ky*d.dy) : Math.max(0.01, ky * d.dy);
            })
            
            .text(function(d) {
                if (d.children) {
                    return d.name;      // sector name
                } else if ((d.dx > 35 && d.dy > 20) || (kx*d.dx > 35 && ky*d.dy > 20)) {
                    return (d.name);        // symbol name
                }
                // return d.children ? d.sector : d.s_symbol;
            })
            .attr("text_anchor", "middle");

        // update the width/height of the rects
        zoomTransition.select("rect")
            .attr("width", function(d) {
                return Math.max(0.01, kx * d.dx);
            })
            .attr("height", function(d) {
                return d.children ? (ky*d.dy) : Math.max(0.01, ky * d.dy);
            })
            .style("fill", function(d) {
                if (d.children) {
                    return "#999999";
                } else if (d.sentiment.sentiment_value > 0) {
                    return "#AAEB9D";   // bull 7FE381
                } else {
                    return "#F78F8F";   // bear
                }        
                // return d.children ? "#777777" : color(d.parent.name);
            });

        node = d;

        if (d3.event) {
            d3.event.stopPropagation();
        }
    }

}
            