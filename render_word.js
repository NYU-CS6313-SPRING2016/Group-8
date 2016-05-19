function render_word(data, name) {
    if(name != "null") {
        document.getElementById("wordTitle").innerHTML = name + "'s Key Words";
    }
        var list = d3.select("#word");
            //d3.selectAll("li").remove();
            list.selectAll("li")
                .remove();
            list.selectAll("li")
                .data(data)
                .enter()
                .append("li")
                .attr("class", "word")
                .text(function(d) {return  d.text + " :";});
        var count = d3.select("#count");
            count.selectAll("li").remove();
            count.selectAll("li")
                .data(data)
                .enter()
                .append("li")
                .attr("class", "count")
                .text(function(d) {return d.size})
                .style("color", "blue");
    
	
}
