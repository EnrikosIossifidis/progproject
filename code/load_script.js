function main() {
	

	// ESSENTIAL HELPER FUNCTIONS (for small see helpers.js)
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
							allDict["countrySort"][countryInYear[j]][curPoint] = {"white": [0,[],[]], "red": [0,[],[]], "other": [0,[],[]]};
						}

						// calculate top 5 per point frequency
						if (whiteList.includes(curWine["Variety"])) {
							cur = allDict["countrySort"][countryInYear[j]][curPoint]["white"]; 
							
							// update point avgprice & point frequency list
							cur[0] ++;
							cur[1].push(curWine["Price"]);

							// update top 5 list
							max = getMaximum(cur[2]);
							if (max[0] == 0) {
								cur[2].push(curWine);
							} else if (cur[2].length < 5 ) {
								cur[2].push(curWine);
							} else {
								if (curWine["Points"] > max[0]) {
									cur[2].splice(max[1],1);
									cur[2].push(curWine);
								}
							}

						} else if (redList.includes(curWine["Variety"])) {
							cur = allDict["countrySort"][countryInYear[j]][curPoint]["red"]; 
							
							// update point avgprice & point frequency list
							cur[0] ++;
							cur[1].push(curWine["Price"]);

							// update top 5 list
							max = getMaximum(cur[2]);
							if (max[0] == 0) {
								cur[2].push(curWine);
							} else if (cur[2].length < 5 ) {
								cur[2].push(curWine);
							} else {
								if (curWine["Points"] > max[0]) {
									cur[2].splice(max[1],1);
									cur[2].push(curWine);
								}
							}
	
						} else {
							cur = allDict["countrySort"][countryInYear[j]][curPoint]["other"]; 
							
							// update point avgprice & point frequency list
							cur[0] ++;
							cur[1].push(curWine["Price"]);

							// update top 5 list
							max = getMaximum(cur[2]);
							if (max[0] == 0) {
								cur[2].push(curWine);
							} else if (cur[2].length < 5 ) {
								cur[2].push(curWine);
							} else {
								if (curWine["Points"] > max[0]) {
									cur[2].splice(max[1],1);
									cur[2].push(curWine);
								}
							}
	
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

	// INITIALIZING FUNCTIONS
	function initText() {

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
			.text("Enrikos Iossifidis");

		textCol.append("h2")
			.text("Find your Vino! ");
		
		textCol.append("h3")
			.text("Problems with finding the right wine for the right price? Find Your Vino helps you! \n First: Pick your price category. Second: Pick your favorite years. Third: Pick your favorite country. Fourth: Pick a score your wine must have. Fifth: Choose your variety. Sixth: Choose and Enjoy your Vino!");
	}

	function choosePriceCat() {

		// set row and column
		var choiceRow = d3.select("#container").append("row")
			.attr("class", "row")
			.attr("id", "UserChoicesPrice");

		var pricecat = d3.select("#UserChoicesPrice").append("div")
			.attr("class", "col")
			.attr("id", "priceCat");

		pricecat.append("h3")
			.text("Select price category:")

		// make price cat column with price categories
		var pricedropdown = pricecat.append("div")
			.attr("class", "col-sm-2")
			.append("select")
			.attr("id", "pricedropdown")
			.attr("class", "dropdown");

		var curSelect = pricecat.append("div")
			.attr("class", "col-sm-6")
			.append("text").attr("class", "curPriceSelection");

		var priceLegend = pricecat.append("div")
			.attr("class", "col-sm-4")
			.attr("id", "priceLegend");

		insertPriceLegend();

		// initialize dropdown
		var priceDat = [1,2,3,4];

		// append categories
		pricedropdown.selectAll("option")
			.data(priceDat)
		.enter().append("option")
			.attr("value", function(d,i) {return d})
			.text(function(d) {return d});

		// make timeslider with given price cat. choices
		d3.select("select")
  			.on("change",function(i){

  				// update priceChoice list & timeslide given choice
				choiceCat = pricedropdown.node().value;
				updateChoices(priceChoices, choiceCat);
				curSelect.text("Current Price Categories: "+ priceChoices);
				updateTimeSlide();
			});

		curSelect.text("Current Price Categories: "+priceChoices);

	}

	function initTimeSlide() {

		// set row and columns
		var yearRow = d3.select("#container").append("row")
			.attr("class", "row")
			.attr("id", "UserChoicesYears");
		
		var timeslideRow = yearRow.append("row")
			.attr("class", "row")
			.attr("id", "timesliderRow");

		var timeslideSlider = timeslideRow.append("div")
			.attr("class", "col")
			.attr("id", "yearslideDiv")
			.append("div").attr("class", "col-sm-12").attr("id", "yearslideCol");
			
		var rowYearChoices = yearRow.append("row")
			.attr("class", "row")
			.attr("id", "yearsChosen");

		// append year choice 'buttons'
		var timeslideText1 = d3.select("#yearslideDiv").append("div")
			.attr("class", "col-sm-6")
			.attr("id", "yeartext1")
			.attr("tranform", "translate("+ $("#yeartext1").width()/2+",0)")
			.append("p")
			.attr("id", "yeartextCol1")
			.attr("class", "yearChoice1");

		var timeslideText2 = d3.select("#yearslideDiv").append("div")
			.attr("class", "col-sm-6")
			.attr("id", "yeartext2")
			.attr("tranform", "translate("+ $("#yeartext2").width()/2+",0)")
			.append("p")
			.attr("id", "yeartextCol2")
			.attr("class", "yearChoice2");

		var width = $(".col-sm-12").width();
		var timeslideHeight = $("#textCol").height()/2;

		// append svg
		var slider = d3
			.select("#yearslideCol")
			.append("svg")
			.attr("width", width)
			.attr("height", timeslideHeight)
			.append("g")
			.attr("id", "timeSlideG")
			.attr("transform", "translate(20,10)");


		// change 'button' colors when clicked
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

		var circExamples = bubblesRow.append("div")
			.attr("class", "col-sm-2")
			.attr("id", "circExamples");

		circExamples.append("h4")
			.text("Bubble chart legenda");

		initLegendCircles();

		var bubblesCol = bubblesRow.append("div")
			.attr("class", "col-sm-10")
			.attr("id", "bubblesCol");

		bubblesCol.append("h4")
			.text("Bubble chart with # of wines per country");

		var width =  $("#bubblesCol").width();
		var height = $("#circExamples").height();

		// set svg
		var bubblesSVG = bubblesCol.append("svg")
			.attr("width", width)
			.attr("height", height)
			.attr("id", "bubblesSVG");

		var g = bubblesSVG.append("g")
			.attr("id", "bubbleG")
			.attr("transform", "translate("+width/5+","+margin.top*1.5+")");

		// begin tooltiploc is bubble canvas so no change need
		createToolTip(tooltipLoc);
	}

	function initHist() {

		// initalize rows & columns
		var histDonutRow = d3.select("#container").append("div")
			.attr("class", "row")
			.attr("id", "histdonutRow");

		var histDonutCol = histDonutRow.append("div")
			.attr("class", "col")
			.attr("id", "histDonutCol");

		var histCol = histDonutCol.append("div")
			.attr("class", "col-sm-5")
			.attr("id", "histCol");

		histCol.append("h4")
			.text("Histogram of Wine points in Country")

		var svgContainer = histCol.append("div")
			.attr("class", "svg-container");

		// initialize svg, g's and axis
		var histWidth = $("#histCol").width();
		var histHeight = $("#bubblesSVG").height()/2;
		var widthFrac = histWidth/10;
		var heightFrac = histHeight/10; 

		var svg = svgContainer.append("svg")
			.attr("class", "svg_hist")
			.attr("width", histWidth)
			.attr("height", histHeight)
			.attr("id", "histSVG")
		.append("g")
			.attr("class", "histG")
			.attr("transform","translate("+ 2*margin.right + "," + margin.top + ")");

		var horXScale = d3.select(".histG").append("g")
			.attr("class", "histScaleX")
			.attr("transform", "translate(0,"+ histHeight*0.9 +")")
			.attr("id", "histScaleX");

		var verScale = d3.select(".histG").append("g")
			.attr("class", "histScaleY")
			.attr("id", "histScaleY");

		// bar wrap element
		var barWrap = d3.select(".histG").append("g")
			.attr("class", "barWrap")
			.attr("id", "barWrap");

		tooltipLoc = "#histCol"
		createToolTip(tooltipLoc);

	}

	function initDonut() {

		var donutCol = d3.select("#histDonutCol").append("div")
			.attr("id", "donutCol")
			.attr("class", "col-sm-7");

		donutCol.append("h4")
			.text("Donut chart with variety of wines on clicked")

		// make donut's canvas ready 
		var donutsvgContainer = donutCol.append("div")
			.attr("class", "svg-container");

		var donutSVG = donutsvgContainer.append("svg")
			.attr("class", "svg_donut")
			.attr("width", $("#donutCol").width())
			.attr("height", $("#histCol").height())
			.attr("id", "donutSVG");

		donutSVG.append("g")
			.attr("class", "donutG")
			.attr("transform","translate("+ $("#donutCol").width() / 5 + "," + $("#histCol").height() / 2.25 + ")");

		donutSVG.append("g")
			.attr("class", "cheapestG")
			.attr("transform","translate("+ $("#donutCol").width() / 1.6+ "," + $("#histCol").height() / 3 + ")");

		tooltipLoc = "#donutRow2"
	}


	// UPDATE FUNCTIONS

	function updateTimeSlide() {

		// update data for year update 
		pricedataChoice = priceChoiceToYear(allwinesdata, priceChoices); 
		var data = pricedataChoice;

		// remove old timeslide
		d3.select("#timeSlideG").select(".axis").remove();
		d3.select("#timeSlideG").select(".slider").remove();

		// update standard 'buttons' with oldest year
		timeslideText1 = d3.select("#yeartextCol1");
		timeslideText2 = d3.select("#yeartextCol2");
		timeslideText1.text(Object.keys(pricedataChoice)[0]);
		timeslideText2.text(Object.keys(pricedataChoice)[0]);
		
		// make new slider 
		width = $(".col-sm-12").width();
		timeslideHeight = $("#textCol").height();
		var sliderSimple = d3
				.sliderBottom()
				.min(d3.min(Object.keys(data)))
				.max(d3.max(Object.keys(data)))
				.width(width-(2*margin.right))
				.step(1)
				.ticks(Object.keys(data).length)
				.on('onchange', val => {

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
									updateBubbles();
								} else {

									// make bubbles with [curvalue, year 2]
									loc1 = Object.keys(data).indexOf(val.toString());
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
									updateBubbles();
								}
							timeslideText2.text(val);
						}
					}
						
				});

		d3.select("#timeSlideG").call(sliderSimple);
		loc2 = Object.keys(data).length - 1;
		updateBubbles();

	}

	function updateBubbles() {

		// update data
		var data = pricedataChoice;	
		var chosen = Object.entries(data).slice(loc1,loc2+1);
		var chosenData = {};
		for (var year in chosen) {
			chosenData[chosen[year][0]] = data[chosen[year][0]];
		}
		winesPerCountry(chosenData);

		// prep data for bubble hierarchy
		var dataset = {"children": []};
		for (var i in allAllDict["countryDict"]) {
			dataset["children"].push({"Land": i, "Aantal": allAllDict["countryDict"][i]})
		}
		var diameter = Number(d3.select("#bubblesSVG").attr("height"));
		var color = d3.scaleOrdinal(d3.schemeCategory10);
		var nodes = d3.hierarchy(dataset)
			.sum(function(d) {
				return d.Aantal});

		var bubble = d3.pack(dataset)
			.size([diameter, diameter])
			.radius(function(d) {
				if (d.value <= 25) {
					return 15
				} else if (d.value <= 100) {
					return 25 
				} else if (d.value <= 250) {
					return 50
				} else if (d.value <= 1000) {
					return 75
				} else if (d.value <= 2500) {
					return 100
				} else {
					return 120
				}
			})
			.padding(1.5);

		var svg = d3.select("#bubbleG")
		var circle = svg.selectAll("circle")
			.data(bubble(nodes).descendants().splice(0,1)[0]["children"]);

		var text = svg.selectAll("text")
			.data(bubble(nodes).descendants().splice(0,1)[0]["children"]);

		// remove old circles and texts
		circle.exit().remove();
		text.exit().remove();

		// Update circles and texts
		circle
			.attr("r", function(d) {return d.r})
			.attr("cx", function(d) {return d.x})
			.attr("cy", function(d) {return d.y});

		text
			.attr("x", function(d) {return d.x})
			.attr("y", function(d) {return d.y})
			.text(function(d) {
				if (d.r > 40) {
					return d["data"].Land
				}
			})

		// append (if necessary) new circles and texts
		circle.enter().append("circle")
			.attr("r", function(d) {
				curRaddd = d.r;
				return d.r;
			})
			.attr("cx", function(d) {return d.x})
			.attr("cy", function(d) {return d.y})
			.style("fill", function(d,i) {
				return color(Math.floor(Math.random()*50));
			})
			.on("click", function(d) {
				curCountry = d["data"].Land;
				updateHist();
			})
			.on("mouseover", function() {
					tooltipLoc = "#bubblesCol";
					mouseover()})
			.on("mousemove", function(d) {
				tipBubble(d, tooltipLoc);
			})
			.on("mouseleave", mouseleave());	
			
		text.enter().append("text")
			.attr("opacity", 0.0001)
			.attr("x", function(d) {return d.x})
			.attr("y", function(d) {return d.y})
			.text(function(d) { 
				if (d.r > 40) {
					return d["data"].Land
				}
			})
			.attr("opacity", 1);

		d3.select(self.frameElement)
			.style("height", diameter + "px");

		updateHist();

	}

	function updateHist() {

		var data = allAllDict["countryPoints"][curCountry]
		var histWidth = $("#histCol").width();
		var histHeight = $("#bubblesSVG").height()/2;
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
			.domain([0, d3.max(freqs)])
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
					clickedBar = d;
					updateDonut()})
				.on("mouseover", function() {
					tooltipLoc = "#histCol";
					mouseover()})
				.on("mousemove", function(d) {
					tipHist(tooltipLoc,allAllDict, curCountry, d,d3.select(this).attr("x"),d3.select(this).attr("y"));})
				.on("mouseleave", mouseleave());

		updateDonut();
	} 

	function updateDonut() {

		// get current data selection
		pointsArray = Object.keys(allAllDict["countrySort"][curCountry]);
		if (clickedBar == 0) {
			clickedBar = pointsArray[Math.floor(Math.random()*pointsArray.length)];
		}	

		data = allAllDict["countrySort"][curCountry][clickedBar];

		width = $("#donutSVG").width()/1.1 - margin.right - margin.left;
		height = $("#donutSVG").height()/1.1 -margin.top - margin.bottom;

		var radius = Math.min(width, height) / 2;
		var dummyData = {white: [data["white"][0], "white"], red: [data["red"][0], "red"], other: [data["other"][0], "grey"]};

		var pie = d3.pie()
			.value(function(d) {return d.value[0];})

		var data_ready = pie(d3.entries(dummyData));

		donutSVG = d3.select("#donutSVG").select(".donutG");
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
			.on("click", function(d) {cheapestUpdate(allAllDict, curCountry, clickedBar, d);});

		donutSVG.exit().remove();
	}

	// general parameters
	// margins
	var margin = {top: 20, right: 20, bottom: 20, left: 20};
	var loc1 = 0;
	var loc2 = 0;
	var lastvalid = 1991;
	var priceChoices = [1,2,3,4];
	var clickedBar = 0;
	var curCountry = "US";
	var allwinesdata = {};
	var choiceCat = 0;
	var whiteList = [];
	var redList = [];
	var allAllDict = {};
	var pricedataChoice = {};
	var curToolTipVal = 0;
	var tooltipLoc = "#bubblesCol";
	var Tooltip = [];

	$.getJSON("./data/wine_varieties.json", function(json) {

			whiteList = json["white"]
			redList = json["red"]
			
		// load data 
		$.getJSON("./data/test10k.json", function(json) {

			allwinesdata = json;
			loc2 = Object.keys(priceChoiceToYear(json, priceChoices)).length-1;

			initText();
			choosePriceCat();
			initTimeSlide();
			initBubbles();
			initHist();
			initDonut();

			updateTimeSlide();
			updateHist();	
			updateDonut();
		});
	});

}
