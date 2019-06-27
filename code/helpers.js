function insertPriceLegend() {

	prices = ["1: $1 - $25, ","2: $25 - $50, ","3: $50 - $75, ","4: > $75"];
	pricecatcol = d3.select("#priceLegend")

	pricecatcol.selectAll("text")
		.data(prices)
		.enter().append("text")
		.text(function(d, i) {return d})
		.attr("class", "legendaPrice");
}

function getText(welcometext) {
	var client = new XMLHttpRequest();
	client.open('GET', './doc/'+welcometext+'.txt');
	client.onreadystatechange = function() {
		d3.select("#"+welcometext).text(client.responseText);
	}		
	client.send();
}

function addNavigation() {

	var container = d3.select("body").append("div")
		.attr("class", "container-fluid")
		.attr("id", "container");

	var navRow = container.append("div")
		.attr("class", "row")
		.attr("id","navrow")
		.append("div").attr("class", "col").attr("id", "navCol")

	navdata = [["Introduction","WelcomeText"], ["Choose Price category & years","UserChoicesPrice"], ["Bubble Chart", "bubblesRow"], ["Histogram & Donut","histdonutRow"]];
	var navigationBar = navRow.append("nav")
		.attr("class","navbar navbar-expand-lg navbar-dark sticky-top")
		.attr("id", "navigationbar")
		.append("div").attr("class", "row")
		.append("ul")
		.attr("class", "navbar-nav")
		.selectAll("li")
		.data(navdata)
		.enter().append("div").attr("class","col-sm-3").append("li").attr("class","nav-item")
		.append("a").attr("class", "nav-link")
		.text(function(d) {return d[0]})
		.attr("href", function(d) {return "#"+d[1]});
	}


function initLegendCircles() {
		var sizes = [15,25,50,75,100,120];
		var text = [" 1 - 25", "25 - 100", "100 - 250", "250 - 1000", "1000 - 2500", "> 2500"];
		var sizesSum = 0;
		for (var s in sizes) {
			sizesSum = sizesSum + (2*sizes[s]);
		}

		var width =  135*2;
		var height = sizesSum + margin.top*2;

		var circexempSVG = d3.select("#circExamples").append("svg")
			.attr("width", width)
			.attr("height", height)
			.attr("id", "circexempSVG");

		var x = [margin.top*2, margin.top*2+sizes[0]+margin.top]
		var lasthight = margin.top;
		for (var i in sizes) {
			circexempSVG.append("g")
				.attr("id", "circG"+i)
			.append("circle")
				.attr("r", sizes[i])
				.attr("cx", $("#circexempSVG").width()/2)
				.attr("cy", lasthight)
				.style("fill", "steelblue")
				.style("border", "4px solid black");

			d3.select("#circG"+i).append("text")
				.text(text[i])
				.style("fill", "black")
				.attr("class", "exampletext")
				.attr("transform", "translate("+$("#circexempSVG").width()/2+","+lasthight+")");
			lasthight = lasthight + (2*sizes[i]) + margin.top*1.25;
		}
	}

function calcAVG(pricelist) {

		var sum = 0;
		for (var i in pricelist) {
			if (pricelist[i] != "NaN") {
				sum = sum + pricelist[i];
			}
		}

		return sum/pricelist.length

}

function getMaximum(arry) {

	count = 0;
	if (arry.length > 0) {
		var highest = [arry[0]["Points"],count];
		for (var i in arry) {
			if (arry[i]["Points"] > highest[0]) {
				highest = [arry[i]["Points"],count];
			}
			count ++;
		}
		return highest
	} else {
		return [0,0]
	}
}


function createToolTip(tooltipLoc) {

		Tooltip = d3.select(tooltipLoc).append("div")
		    .style("opacity", 1)
		    .attr("translate", "transform("+ (-margin.left/2)+",0)")
		    .attr("class", "tooltip")
		    .style("background-color", "white")
		    .style("border", "solid")
		    .style("border-width", "2px")
		    .style("border-radius", "5px")
		    .style("padding", "5px")
	}

function mouseover() {
	Tooltip
		.style("opacity", 1)
	d3.select(".tooltip")
		.style("stroke", "black")
		.style("opacity", 1);
}

function tipBubble(curval, tooltipLoc) {

	d3.select(tooltipLoc).select(".tooltip")
      .html("LAND: " + curval["data"].Land+"<br>"+ "AANTAL:"+ curval["data"].Aantal)
      .style("left", function() {
      	var leftBound = curval.x+($("#bubblesCol").width()/12) - curval.r;
      	var rightBound = curval.x+($("#bubblesCol").width()/12) + curval.r;
      	if (d3.mouse(this)[0]+70 > rightBound) {
      		return rightBound+"px";
      	} else if (d3.mouse(this)[0]+70 < leftBound) {
      		return leftBound+"px";
      	} else {
      		return d3.mouse(this)[0]+70+"px";
      	}})
      .style("top", function() {
      	var upBound = curval.y+(margin.top/2) - curval.r; 
      	var bottomBound = curval.y+(margin.top/2) + curval.r; 
      	if (d3.mouse(this)[0]+70 < upBound) {
      		return upBound+"px";
      	} else if (d3.mouse(this)[0]+70 > bottomBound) {
      		return bottomBound+"px";
      	} else {
      		return d3.mouse(this)[0]+70+"px";
      	};

      });
}

function tipHist(tooltipLoc, allAllDict, curCountry ,curval,x,y) {

	var numbertotal = allAllDict["countryPoints"][curCountry]["points"][curval];
	var white = calcAVG(allAllDict["countrySort"][curCountry][curval].white[1]);
	var red = calcAVG(allAllDict["countrySort"][curCountry][curval].red[1]);
	var other = calcAVG(allAllDict["countrySort"][curCountry][curval].other[1]);

	var priceavg = Math.round((white + red + other)/3);

	d3.select(tooltipLoc).select(".tooltip")
      .html("Average Price: $"+ priceavg)
      .style("left", x+"px")
      .style("top", y+"px");
}

function mouseleave() {
	Tooltip
      .style("opacity", 0)
    d3.select(".tooltip")
      .style("stroke", "none")
      .style("opacity", 1);
}


function cheapestUpdate(allAllDict, curCountry, clickedBar, curval) {

	chosencolor = curval["data"].key;

	// new data
	cheapest = d3.select(".cheapestG").selectAll("text")
		.data(allAllDict["countrySort"][curCountry][clickedBar][chosencolor][2]);

	// delete unnecessary 
	cheapest.exit().remove();

	// update existing
	cheapest
		.text(function(d) {return d["Title"]+", Price: "+ d["Price"]})
		.attr("y", function(d, i) {return i*20});

	// enter new
	cheapest
		.enter().append("text")
			.text(function(d) {return d["Title"]+" , "+ d["Price"]})
			.attr("y", function(d,i) {return i*20});
}

function insertPriceLegend() {

// first element 0 becuase enter().append() doesn't take first element 
// of prices for a strange reason
prices = ["1: $1 - $25, ","2: $25 - $50, ","3: $50 - $75, ","4: > $75"];
pricecatcol = d3.select("#priceLegend")

pricecatcol.selectAll("text")
	.data(prices)
	.enter().append("text")
	.text(function(d, i) {return d})
	.attr("class", "legendaPrice");
}

function updateChoices(priceChoices, choiceCat) {

	// append if not in preference list, else delete from list
	if (!(priceChoices.includes(Number(choiceCat)))) {
		priceChoices.push(Number(choiceCat));
	} else {
		choiceIndex = priceChoices.indexOf(Number(choiceCat));
		priceChoices.splice(choiceIndex, 1);

		if (priceChoices.length == 0) {
			priceChoices = [1,2,3,4];
		}
	}

	// make timeslide based on price preferences
	console.log(priceChoices)
}

var margin = {top: 20, bottom:20, right:20, left:20};