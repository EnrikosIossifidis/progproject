function winesPerCountry(data, whiteList, redList) {

	var allDict = {};
	allDict["countryDict"] = {}
	allDict["countryPoints"] = {}
	allDict["countrySort"] = {}
	var countryDict = {};	 

	for (var year in data) {
		countryInYear = Object.keys(data[year])
		for (var j in countryInYear) {
			if (countryInYear[j] != "NaN") {
									
				// get wine point frequency per country over years
				if (!(countryInYear[j] in allDict["countryPoints"])) {
					allDict["countryPoints"][countryInYear[j]] = {};
					allDict["countryPoints"][countryInYear[j]]["points"] = {}
				}
				
				if (!(year in allDict["countryPoints"][countryInYear[j]])) {
						allDict["countryPoints"][countryInYear[j]][year] = [];
				}

				if (!(countryInYear[j] in allDict["countrySort"])) {
					allDict["countrySort"][countryInYear[j]] = {}
				}

				// add wine points to country: year
				for (var wine in data[year][countryInYear[j]]) {
					

					curTitle = Object.keys(data[year][countryInYear[j]])[wine]
					curWine = data[year][countryInYear[j]][curTitle]
					curPoint = curWine["Points"];
					allDict["countryPoints"][countryInYear[j]][year].push(curPoint);
				
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
				allDict["countryDict"][countryInYear[j]] = allDict["countryDict"][countryInYear[j]] + data[year][countryInYear[j]].length;
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