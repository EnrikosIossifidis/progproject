function test() {
	alert("TEST");

	// general parameters
	var topMar = 10;
	var rightMar = 10;
	var leftMar = 10;
	var botMar = 10;
	margin = {top: topMar, right: rightMar, bottom: botMar, left: leftMar}

	var q = d3.queue();
	q.defer(d3.json, "https://enrikosiossifidis.github.io/progproject/data/winesData.json")
	console.log(q);
}
