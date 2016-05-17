function render_week_word(data, slt) {
	var color = d3.scale.linear()
            //.domain([0,20,40,60,80,100,150,180,200,300,400])
            //.domain([80,70,60,50,45,45,40,35,30,25,20])
            .domain([10,20,30,40,50,55,60,65,70,70,70])
            .range(["#ccc", "#bbb", "#aaa", "#999", "#777", "#555", "#333", "#222", "#222", "#222", "#111", "#000"]);

    //console.log(data);
    d3.layout.cloud().size([400, 400])
            .words(data)
            .rotate(0)
            .fontSize(function(d) { return Math.sqrt(d.size) / 4; })

            .on("end", draw)
            .start();

    function draw(words) {
    	d3.select("#cloud").select("svg").remove();
        d3.select("#cloud").append("svg")
                .attr("width", 400)
                .attr("height", 400)

                .attr("class", "wordcloud")
                .append("g")
                // without the transform, words words would get cutoff to the left and top, they would
                // appear outside of the SVG area
                .attr("transform", "translate(150,150)")
                .selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", function(d) { return d.size  + "px"; })
                .style("fill", function(d, i) { return color(i); })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y ] + ")rotate(" + d.rotate + ")";
                })

                .text(function(d) { return d.text; });
    }
}
