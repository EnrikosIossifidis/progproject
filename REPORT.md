# Report

## Application description
The visualization gives you an insight in a dataset which contains wine reviews. The user can make a selection out of this dataset, by picking a price category and a period of years. The chosen data influences the bubble chart (where the country bubble's radius depends on the number of wines). After clicking the country bubble, the histogram beneath shows the frequency of the points that were given to the selected wine. Hovering over a bar gives the average price of the wines in that "point"-category. A click on a bar makes the donut chart, on the right, show the distribution of varieties within the 'point' category of the histogram. When clicked on variety, the top 5 cheapest wines is showed within that selection.
###

![alt text](https://enrikosiossifidis.github.io/progproject/doc/pictures/wholepic.png)

## Technical design:
### High-Level

When index.html is loaded, main() is called from load_script.js. In this file you will first see a bunch of init- and update functions. After the functions, the global variables are declared (with begin setting: All price categories, "US" as country chosen and a random bar picked from US's histogram).
###
Then:
###
First: white- and red varieties list and all json data are imported. 

Second: Each component is initialized (appending svg's, div's, col's, etc.). 

Third: First update is called within begin values. After that the components are updated by user's choices.

Hierarchy of components: Price Category - Years- Bubbles - Histogram - Donut - Top 5.

##### Order Update: 
Price Category or Years is changed -> Update bubbles -> Update hist (with previous chosen country) -> Update Donut graph with random chosen point from histogram.

### Detailed:

After setting global variables and loading data:

#### Initialize navigation bar (addNavigation)

#### Initailize welcome texts with initText(). This function calls getText() to retrieve text data.

#### Initialize Price categories: 
Inserts svg,divs etc. first. Then insertPriceLegend() is called to insert the price category legend. The event listener "change" is add to update priceChoices given user choice (updateChoices()).

#### Update Price Categories: 
 Updatechoices checks if chosen variable is in current selection. If so, delete it from selection, otherwise append the picked variable to the selection. Current selection is a global variable. After that updateTimeSlide() is called to update year extrema of selection.

#### Initialize Timeslider: 
Timeslider is initialized with rows and columns, d3-simple-slider, 'year buttons'. Plus the event listener to the year buttons to change from color. 

#### Update Timeslider:
If left button clicked: Black-> Red if other not Red, Black->Black if other Red, Red->Black if other Black. Chosen years are stored in loc1, loc2 (both global). Where each represents the index of the year in data selection.

#### Initialize Bubbles: 
Standard d3 inserts, bubble legenda (initLegendCircles()) and a tooltip for bubbles is created (createToolTip(tooltipLoc).

#### Initialize Histogram:
Standard d3 inserts, axes and tooltip

#### Update Histogram:
Histogram is updated by updating x (scaleBand) and y (scaleLinear) axis domain bounds, deleting previous bars and appending new bars. The data is chosen from the current selection object and selecting by clicked country and clicked bar. When the mouse hovers over a bar, the tooltip calculates the average price of the current bar. The clicked bar is remembered by making it a global variable. 

#### Bubbles: 
Given price preferences and years, the bubbles are created with d3-hierarchy (with no hierarchy), by updating amount of circles and calculating the radius given the number of wines in the chosen dataset. Further on, an object of the chosen dataset is created with the function winesPerCountry. Here, calculations are made for the bubble chart (number of wines), histogram (frequency of points) and donut chart (number of each variety and remembering cheapest top 5). The tips are made with d3-tip. The location of the tip went all crazy, so I restrained it to location of the circle where the mouse hovers over. The chosen country is a global variable.

#### Donut:
To make the donut chart, d3-pie is used. The size of each slice is computed by making the angle of the slice depend on # wines of that variety in current selection. The top 5 is retrieved from the given choices and dictionary calculated at the bubble chart.

## Challenges: 

### Getting necessary data:
All wanted data was retrieved from the dataset. The wine's year was a bit tricky to find out since it was only mentioned in the wine's title. 

### Learning d3, javascript again:
After first picking the right project, re-using d3 and javascript after more than a year (I started the minor in 2018/2019, but could not do the project) was the next challenge. Especially the asynchronic way of dealing with data in javascript was forgotten. But within a couple of days I was again used to it.

### Way of choosing years
I wanted a sort of dynamic and intuitive use of the timeslider (so many options, clear current choice, with little buttons). The solution was the use of 'locking'-year buttons. It certainly took 1/2 days and (a lot of) logic thinking to get this right.  

### Making bubble chart:
I first implemented a bubble chart on my own, by letting the circles go in circles around the middle circle (add 360/5 degrees to each step, and enlarge radius to middle circle per 5 steps). I kept it for 1.5 week until i the decided the monday of the last week to use d3-hierarchy, because it did not show the bubbles as wanted. This made a whole lot nicer bubble chart. Nevertheless, a nice dynamically moving bubble chart with d3-force, as mentioned in the design document, was one step too far too accomplish. Lot of time was spent on the self-designed document.

### Calculate preference data
One recurring question during the making of the whole project, was to know when, what and how to calculate the necesarry values for each graph in an efficient way. The challenge was to computate as little as possible at each new user choice, (otherwise it gets slow) without losing any information.

### Styling
The last days before the deadline I was struggling with getting CSS working on my code. Therefore I could not complete the goals set in the design document (make bars and donut slices dynamically change and move). I kept postponing styling to a later moment (gave priority to fixing functionalities), until I was forced to leave the styling as it was, due to lack of time. 

## Decisions: 
The 'dynamic' time slider (year 'dynamic' choices) was better to do than, for example, two dropdowns/checkboxes to choose your years. Firstly because it esthetically nicer and gives more dynamics to the visualization. The trade-off is that the timeslider shows years which are not in included in the dataset because the d3-simple-slider takes step(1). The fix for this is to select the last valid year, and update this when sliding over a new valid year.
###
The large circle legenda is chosen for this form because due to lack of time I could not place all circles together on 1 position and add legenda to show value of each circle. This would have save a lot of space.  
###
No legenda for donut diagram because I think people intuitively connect the color red to red wines, and white to white. But a small explanation of the grey slice would have stood good. Those are the wines which were not included in the retrieved list of white and red wines.
###
No partical colors for countries is chosen because the color would not represent anything. The trade-off is that you can't see that some continents are largely represented (Europe) and some not (Africa, Asia)). But this feels trivial to say, because the countries showed have typically a wine tradition, and the countries not showed, not.    