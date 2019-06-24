function test() {
	
	// // TO ADD PRICE CATEGORIES	

	// fonktions
	function drawText() {

		// initialize space	
		var container = d3.select("body").append("div")
			.attr("class", "container-fluid")
			.attr("id", "container");

		var textRow = container.append("row")
			.attr("class", "row")
			.attr("id", "WelcomeText");

		// Welcome texts
		var textCol = textRow.append("div")
			.attr("class", "col")
			.attr("id", "textCol");

		textCol.append("h2")
			.text("Find your Vino");

		textCol.append("h4")
			.text("Select Year and Price Category:");
	}


	function choosePriceCat() {

		// set row and column
		var choiceRow = d3.select("#container").append("row")
			.attr("class", "row")
			.attr("id", "UserChoices");

		// set space and variables
		var timeslideCol = d3.select("#UserChoices").append("div")
			.attr("class", "col")
			.attr("id", "userChoiceCol");

		// make price cat column with price categories
		var timeslideText1 = d3.select("#userChoiceCol").append("div")
			.attr("class", "col-sm-2")
			.append("select").attr("id", "priceCatCol")

		// make price object out of pricecategories in data
		var priceDat = {"€":1,"€€":2,"€€€":3,"€€€€":4};

		d3.select("#priceCatCol").selectAll("option")
			.data(Object.keys(priceDat))
		.enter().append("option")
			.attr("value", function(d,i) {return d})
			.text(function(d) {return d});

		// make timeslider with given price cat. choices
		d3.select("select")
  			.on("change",function(i){

  				// update priceChoice list given choice
				choiceCat = priceDat[d3.select("#priceCatCol").node().value];
				updateChoices();
			});

	}

	function updateChoices() {

		// append if not in preference list, else delete from list
		if (!(priceChoices.includes(choiceCat))) {
			priceChoices.push(choiceCat);
		} else {
			choiceIndex = priceChoices.indexOf(choiceCat);
			priceChoices.splice(choiceIndex, 1);

			if (priceChoices.length == 0) {
				priceChoices = [1,2,3,4];
			}
		}

		// make timeslide based on price preferences
		console.log(priceChoices)
		updateTimeSlide();
		updateBubbles();
	}

	function priceChoiceToYear(allData, priceChoices) {

		// combine data from different categories to one dataset of years
		var data = {}
		for (var i in priceChoices) {
			for (var j in allData[priceChoices[i]]) {
				if (!(j in data)) {
					data[j] = {};
				} 
				curCountries = Object.keys(allData[priceChoices[i]][j]); 
				for (var k in curCountries) {

					// append wine to correct year and country
					curWines = allData[priceChoices[i]][j][curCountries[k]];
					if (!(curCountries[k] in data[j])) {
						data[j][curCountries[k]] = curWines;
					} else {
						data[j][curCountries[k]] = data[j][curCountries[k]].concat(curWines);
					}
				}
			}

		}

		return data
	}

	function updateTimeSlide() {

		var data = priceChoiceToYear(allwinesdata, priceChoices)
		d3.select("#timeSlideG").select(".axis").remove();
		d3.select("#timeSlideG").select(".slider").remove();
		timeslideText1 = d3.select("#yeartextCol1");
		timeslideText2 = d3.select("#yeartextCol2");

		width = $(".col-sm-8").width();
		timeslideHeight = $("#textCol").height();
		var sliderSimple = d3
				.sliderBottom()
				.min(d3.min(Object.keys(data)))
				.max(d3.max(Object.keys(data)))
				.width(width-(2*margin.right))
				.step(1)
				.ticks(Object.keys(data).length)
				.on('onchange', val => {

					Curry = val;
					// year 1 is not chosen
					if (timeslideText1.style("color") != "red") {

						// no choice: bubbles with all years
						if (timeslideText2.style("color") != "red") {
							loc1 = 0;
							loc2 = Object.keys(data).length-1;
							updateBubbles();
							timeslideText1.text(val);
							timeslideText2.text(val);
						} else {

							// get locked year 2
							var red2 = timeslideText2.text();	

							// if year1 < year2: bubbles with [curValue, year2]
							if (val <= Number(red2)) {

								// get year 2 location in dataset
								loc2 = Object.keys(data).indexOf(red2);

								// check if curValue in data years
								if (!(val in data)) {

									// if so take last legit curvalue
									// console.log("TIMESLIDE DATA", loc1, loc2, data)
									updateBubbles();
								} else {

									// make bubbles with [curvalue, year 2]
									loc1 = Object.keys(data).indexOf(val.toString());
									// console.log("TIMESLIDE DATA", loc1, loc2, data)
									updateBubbles();

									// update last legit loc with curvalue
									lastvalid = loc1;
								}

							// update year 1 value
							timeslideText1.text(val);
							}
						}
					} else {

						// get index year 1 in data
						loc1 = Object.keys(data).indexOf(timeslideText1.text());

						// only change when year 2 > year 1
						if (val >= Number(timeslideText1.text())) {	

								// if only year 1 locked then return [year 1, curvalue]
								if (timeslideText2.style("color") != "red") {

									// check if curvalue in data years
									if (!(val in data)) {

										// if so take last legit curvalue
										// console.log("TIMESLIDE DATA", loc1, loc2, data)
										updateBubbles();
									} else {

										// make bubbles with [year 1, curvalue]
										loc2 = Object.keys(data).indexOf(val.toString());
										updateBubbles();

										// update last legit loc with curvalue
										lastvalid = loc2;
									}
								} else {

									// make bubbles with year 1, year 2
									loc2 = Object.keys(data).indexOf(timeslideText2.text());
									// console.log("TIMESLIDE DATA", loc1, loc2, data)
									updateBubbles();
								}
							timeslideText2.text(val);
						}
					}
						
				});

		d3.select("#timeSlideG").call(sliderSimple);

	}

	function updateBubbles() {

		var data = priceChoiceToYear(allwinesdata, priceChoices)	
		var chosen = Object.entries(data).slice(loc1,loc2+1);
		var chosenData = {};
		for (var year in chosen) {
			chosenData[chosen[year][0]] = data[chosen[year][0]];
		}

		// set circle attributes
		radius = 30
		width = $("#bubblesSVG").width();
		height = $("#bubblesSVG").height();
		circleXmax = width - radius;
		circleYmax = height - radius;

		// sort data on number of wines per country
		var allDict = winesPerCountry(chosenData);
		var coordinates = circlesLocations(allDict["countryDict"], circleXmax, circleYmax, width, height);
		bubbleData = Object.keys(allDict["countryDict"]);

		// remove uneeded circles
		bubbleCirc = d3.select("#bubbleG").selectAll("circle")
			.data(bubbleData);

		// remove uneeded texts
		bubbleText = d3.select("#bubbleG").selectAll("text")
			.data(bubbleData);

		bubbleCirc.exit().remove();
		bubbleText.exit().remove();
		
		bubbleCirc.enter().append("circle")
			.attr("class", "enterCircle")
				.attr("cx", function(d,i) {return coordinates[0][i];})
				.attr("cy", function(d,i) {return coordinates[1][i];})
				.attr("r", function(d,i) {return coordinates[2][i];})
				.attr("fill", "red")
				.on("click", function(d,i) {
					console.log(d);
					curCountry = d;
					updateHist();
					// makeHist(d, histDonutData["countryPoints"][d]);
					// makeDonut(d, chosenData);
				});

		bubbleText.enter().append("text")
			.attr("class", "enterText")
			.attr("x", function(d,i) {return coordinates[0][i]-25;})
			.attr("y", function(d,i) {return coordinates[1][i];})
			.text(function(d,i) {return coordinates[3][i];})

	}

	// calculate bubble coordinates
	function circlesLocations(data, xMax, yMax, w , h) {

		// rescale #wines to radius
		maxNumber = data[Object.keys(data)[0]];
		minNumber = 1;
		countryExceptFirstList = Object.keys(data).slice(1)

		radiussen = [40];
		xCors = [w/2];
		yCors = [h/2];
		largestrad = 35;
// 
		thetaStep = ((360/5)*2*Math.PI)/180;
		angleStep = thetaStep/(Object.keys(data).length/5)

		var count = 0;
		var magRad = 1;
		var breakcounter = 0;
		var mag = 0;

		// curDir = 
		for (var i in countryExceptFirstList) {

			curNumberWines = data[countryExceptFirstList[i]]
			curRad = 40*(curNumberWines/maxNumber)
			radiussen.push(curRad);

			xCors.push(w/2 + (80*magRad*Math.cos(((thetaStep*i)+(angleStep*mag)))));
			yCors.push(h/2 + (80*magRad*Math.sin(((thetaStep*i)+(angleStep*mag)))));

			// draw help lines
			// var line = d3.select("#bubbleG").append("line")
			// 	.attr("id", "testline"+ i.toString())
			// 	.attr("x1", w/2)
			// 	.attr("x2", w/2 + (80*magRad*Math.cos(((thetaStep*i)+(angleStep*mag)))))
			// 	.attr("y1", h/2)
			// 	.attr("y2", h/2 + (80*magRad*Math.sin(((thetaStep*i)+(angleStep*mag)))))
			// 	.style("stroke", "black");

			if (i > 0 && i % 4 == 0) {

				magRad = magRad+(0.6 - breakcounter);
				mag ++;
				breakcounter = breakcounter + (mag*0.1);

			}
			count ++;
		}
		
		return [xCors,yCors, radiussen, Object.keys(data)];
	}
	
	// calculate and sort number of wines per country
	function winesPerCountry(data) {

		var allDict = {};
		allDict["countryDict"] = {}
		allDict["countryPoints"] = {}
		allDict["countrySort"] = {}
		var countryDict = {};	 

		for (var i in data) {
			countryInYear = Object.keys(data[i])
			for (var j in countryInYear) {
				if (countryInYear[j] != "NaN") {
										
					// get wine point frequency per country over years
					if (!(countryInYear[j] in allDict["countryPoints"])) {
						allDict["countryPoints"][countryInYear[j]] = {};
						allDict["countryPoints"][countryInYear[j]]["points"] = {}
					}
					
					if (!(i in allDict["countryPoints"][countryInYear[j]])) {
							allDict["countryPoints"][countryInYear[j]][i] = [];
					}

					if (!(countryInYear[j] in allDict["countrySort"])) {
						allDict["countrySort"][countryInYear[j]] = {}
					}

					// add wine points to country: year
					for (var wine in data[i][countryInYear[j]]) {
						

						curTitle = Object.keys(data[i][countryInYear[j]])[wine]
						curWine = data[i][countryInYear[j]][curTitle]
						curPoint = curWine["Points"];
						allDict["countryPoints"][countryInYear[j]][i].push(curPoint);
					
						if (!(curPoint in allDict["countryPoints"][countryInYear[j]]["points"])) {
							allDict["countryPoints"][countryInYear[j]]["points"][curPoint] = 0;
						}						

						allDict["countryPoints"][countryInYear[j]]["points"][curPoint] ++;
						
						if (!(curPoint in allDict["countrySort"][countryInYear[j]])) {
							allDict["countrySort"][countryInYear[j]][curPoint] = {"white": 0, "red": 0, "other": 0};
						}

						if (whiteList.includes(curWine["Variety"])) {
							allDict["countrySort"][countryInYear[j]][curPoint]["white"] ++;
						} else if (redList.includes(curWine["Variety"])) {
							allDict["countrySort"][countryInYear[j]][curPoint]["red"] ++;
						} else {
							allDict["countrySort"][countryInYear[j]][curPoint]["other"] ++;	
						}
					}

					if (!(countryInYear[j] in allDict["countryDict"])) {
						allDict["countryDict"][countryInYear[j]] = 0;
					}
					allDict["countryDict"][countryInYear[j]] = allDict["countryDict"][countryInYear[j]] + data[i][countryInYear[j]].length;
				}
			}
		}						

		// sort by number of wines
		sortedCountries = {}
		sorted = Object.keys(allDict["countryDict"]).sort(function(a,b) {
			return allDict["countryDict"][b] - allDict["countryDict"][a];
		})

		for (var k in sorted) {
			sortedCountries[sorted[k]] = allDict["countryDict"][sorted[k]];
		}
		allDict["countryDict"] = sortedCountries
		allAllDict = allDict
		return allDict
	}

	function updateHist() {

		var data = allAllDict["countryPoints"][curCountry]
		var histWidth = $("#bubblesSVG").width();
		var histHeight = $("#bubblesSVG").height();
		var widthFrac = histWidth/10;
		var heightFrac = histHeight/10; 

		// x axis with input points
		var xScale = d3.scaleBand()
			.domain(Object.keys(data["points"]))
			.range([0, widthFrac*9]);
		
		d3.select("#histScaleX")
			.call(d3.axisBottom(xScale));

		// make list of frequencies
		freqs = []

		for (var i in data["points"]) {
			freqs.push(data["points"][i]);
		}

		// y axis with input frquencies
		var yScale = d3.scaleLinear()
			.domain([d3.min(freqs), d3.max(freqs)])
			.range([heightFrac*9, 0]);
		
		d3.select("#histScaleY")
			.call(d3.axisLeft(yScale));

		barWrap = d3.select("#barWrap")
		barWrap.selectAll("rect").remove();
		// console.log(barWrap)
		var counter = 0

		// METHOD WANTED MAAR NIET WIL LUKKEN:
		var keys = Object.keys(data["points"]); 
		barWrap.selectAll("rect")
				.data(keys)
			.enter().append("rect")
				.attr("fill", "steelblue")
				.attr("class", "bar")
			 	.attr("x", function(d,j) {return xScale(d)})
				.attr("y", function(d,j) {
					// console.log(xScale(d), d, j,data["points"][d], yScale(data["points"][d]));
					return yScale(data["points"][d])})
				.attr("width", xScale.bandwidth())
				.attr("height", function(d,j) { return (heightFrac*9)-yScale(data["points"][d])})
				.on("click", function(d,j) {
					console.log(d)
					clickedBar = d;
					updateDonut()});
	}

	function updateDonut() {

		// get current data selection
		var data = allAllDict["countrySort"][curCountry][clickedBar];

		width = $("#donutSVG").width() - margin.right - margin.left;
		height = $("#donutSVG").height() -margin.top - margin.bottom;

		var radius = Math.min(width, height) / 2;

		var dummyData = {wit: [data["white"], "white"], rood: [data["red"], "red"], overig: [data["other"], "grey"]};

		var pie = d3.pie()
			.value(function(d) {return d.value[0];})

		var data_ready = pie(d3.entries(dummyData));

		donutSVG = d3.select("#donutSVG").select(".histG");
		donutSVG.selectAll("path").remove();

		donutSVG.selectAll("slice")
			.data(data_ready)
			.enter().append("path")
			.attr("d", d3.arc()
				.innerRadius(100)
				.outerRadius(radius)
			)		
			.attr("fill", function(d) {return d.data.value[1]})
			.attr("stroke", "black")
			.style("stroke-width", "2px")
			.style("opacity", 0.7)

		donutSVG.exit().remove();
	}

	function initTimeSlide() {


		var timeslideSlider = d3.select("#userChoiceCol").append("div")
				.attr("class", "col-sm-8")
				.attr("id", "yearslideDiv")
				.append("div").attr("id", "yearslideCol");
			
			var timeslideText1 = d3.select("#userChoiceCol").append("div")
				.attr("class", "col-sm-1")
				.append("p").attr("id", "yeartextCol1");

			var timeslideText2 = d3.select("#userChoiceCol").append("div")
				.attr("class", "col-sm-1")
				.append("p").attr("id", "yeartextCol2");

		var width = $(".col-sm-8").width();
		var timeslideHeight = $("#textCol").height();

		var slider = d3
			.select("#yearslideCol")
			.append("svg")
			.attr("width", width)
			.attr("height", timeslideHeight)
			.append("g")
			.attr("id", "timeSlideG")
			.attr("transform", "translate(20,10)");

		d3.select("#yeartextCol1").text(lastvalid)
			.on("click", () => {

				if (timeslideText1.style("color") != "red") {
					if (timeslideText2.style("color") != "red") {
						timeslideText1.style("color", "red");
					} else {
						timeslideText2.style("color", "black");
						loc1 = 0
						loc2 = Object.keys(priceChoiceToYear(allwinesdata, priceChoices)).length-1;
						updateBubbles();
					}
				} else {
						timeslideText1.style("color", "black");				
				};
			});

		d3.select("#yeartextCol2").text(lastvalid)
			.on("click", () => {

				if (timeslideText2.style("color") != "red") {
					if (timeslideText1.style("color") != "red") {
						timeslideText2.style("color", "red");
					} else {
						timeslideText1.style("color", "black");
						loc1 = 0
						loc2 = Object.keys(priceChoiceToYear(allwinesdata, priceChoices)).length-1;
						updateBubbles();
					}
				} else {
					timeslideText2.style("color", "black");				
				};
			});
		}


	function initBubbles() {

		// make canvas
		var bubblesRow = d3.select("#container").append("row")
			.attr("class", "row")
			.attr("id", "bubblesRow");

		var bubblesCol = bubblesRow.append("div")
			.attr("class", "col-sm-5")
			.attr("id", "bubblesCol");

		var betweenCol = bubblesRow.append("div")
			.attr("class", "col-sm-1")
			.attr("id", "betweenCol");

		var width =  $("#bubblesCol").width();
		var height = 500;

		var bubblesSVG = bubblesCol.append("svg")
			.attr("width", width)
			.attr("height", height)
			.attr("id", "bubblesSVG")
			.style("border", "1px solid black");

		var g = bubblesSVG.append("g")
			.attr("id", "bubbleG");

	}

	function initHist() {

		var histWidth = $("#bubblesSVG").width();
		var histHeight = $("#bubblesSVG").height();
		var widthFrac = histWidth/10;
		var heightFrac = histHeight/10; 

		// draw hist canvas and initialize axes
		var histCol = d3.select("#bubblesRow").append("div")
			.attr("class", "col-sm-6")
			.attr("id", "histCol");

		var svgContainer = histCol.append("div")
			.attr("class", "svg-container");

		var svg = svgContainer.append("svg")
			.attr("class", "svg_hist")
			.attr("width", histWidth)
			.attr("height", histHeight)
			.attr("id", "histSVG")
			.style("border", "1px solid black")
		.append("g")
			.attr("class", "histG")
			.attr("transform","translate("+ 2*margin.right + "," + margin.top + ")");

		var horXScale = d3.select(".histG").append("g")
			.attr("class", "histScaleX")
			.attr("transform", "translate(0,"+ (histHeight*0.9).toString() +")")
			.attr("id", "histScaleX");

		var verScale = d3.select(".histG").append("g")
			.attr("class", "histScaleY")
			.attr("id", "histScaleY");

		// bar wrap element
		var barWrap = d3.select(".histG").append("g")
			.attr("class", "barWrap")
			.attr("id", "barWrap");

	}

	function initDonut() {
		
		var donutRow = d3.select("#container").append("row")
			.attr("id", "donutRow")
			.attr("class", "row")

		var fillCol = donutRow.append("div")
			.attr("id", "donutRow")
			.attr("class", "col-sm-3");

		var donutCol = donutRow.append("div")
			.attr("id", "donutRow")
			.attr("class", "col-sm-6");

		var fillCol2 = donutRow.append("div")
			.attr("id", "donutRow")
			.attr("class", "col-sm-3");

		// make donut's canvas ready 
		var donutsvgContainer = donutCol.append("div")
			.attr("class", "svg-container");

		var donutSVG = donutsvgContainer.append("svg")
			.attr("class", "svg_donut")
			.attr("width", 900)
			.attr("height", 500)
			.attr("id", "donutSVG")
			.style("border", "1px solid black")
		.append("g")
			.attr("class", "histG")
			.attr("transform","translate("+ 900 / 2 + "," + 500 / 2 + ")");

	}


	// general parameters
	// margins
	var topMar = 20;
	var rightMar = 20;
	var leftMar = 20;
	var botMar = 20;
	var margin = {top: topMar, right: rightMar, bottom: botMar, left: leftMar}
	var loc1 = 0;
	var loc2 = 0;
	var maxAmount = 0;
	var lastvalid = 1991;
	var priceChoices = [1,2,3,4];
	var Curry = 2007;
	var clickedBar = 0;
	var curCountry = "US";
	var allwinesdata = {};
	var choiceCat = 0;
	var whiteList = [];
	var redList = [];
	var allAllDict = {};
	var curHistData = {};

	$.getJSON("./data/wine_varieties.json", function(json) {

			whiteList = json["white"]
			redList = json["red"]
			
		// load data 
		$.getJSON("./code/test10k.json", function(json) {

			allwinesdata = json;
			loc2 = Object.keys(priceChoiceToYear(json, priceChoices)).length-1;
			var allChoices = priceChoiceToYear(allwinesdata, priceChoices)

			drawText();
			choosePriceCat();
			initTimeSlide();
			updateTimeSlide();

			// make timeslide & year labels
			initBubbles();
			updateBubbles();

			// make pre-choice drawings with US wines
			var usBegin = winesPerCountry(allChoices)["countryPoints"]["US"];

			initHist();
			updateHist();		
			initDonut();
			updateDonut(curCountry, usBegin);
		});
	});

}
