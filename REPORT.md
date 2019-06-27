# Report

## Application description
![alt text](https://enrikosiossifidis.github.io/progproject/doc/pictures/wholepic.PNG)

The vizualisation gives you an insight in a dataset which contains wines. The user can make a selection out of this dataset, based on price and year. The chosen data influences the bubble chart (where per bubble the number of wines, from that country, are showed). The chosen country influences the histogram which shows the points of the reviewed wines in that country. The donut chart shows the distribution of varieties within 'point' category of the histogram. When clicked on variety, the top 5 cheapest wines is showed of that selection.

## Technical design:
### High-Level

##### First all data and white- and red varietylist is imported. 

##### Then all components are initialized (e.g. svg's, div's, col's, etc. are appended).

##### First update (before user choices are made) is made with all price categories, years and country US. A random point in the histogram is chosen to plot the donut chart.

##### Hierarchy of components: Price Category - Years- Bubbles - Histogram - Donut - Top 5.
##### Order Update: Price Category or Years is changed -> Update bubbles -> Update hist (with previous chosen country) -> Update Donut graph with random chosen point from histogram.

### Detailed:
#### Price categories: 
##### The chosen price categories are only updated if chosen value changes, because the eventlisterener "change" is used. On "change", it checks if chosen variable is in current selection. If so, delete it from selection, otherwise append the picked variable. Current selection is a global variable. 
#### Timeslider: 
##### The timeslider is updated for every new price category selection. Timeslider is made with d3-simple-slider. On "sliding", the bubble chart is updated with the chosen oldest and last year. If the left buttonyear is clicked, then "(value left button, current slide position year)" is showed, and vice versa for left button. If no button is clicked, all years are showed. Chosen years are stored in loc1, loc2 (both global). Where each represents the location of the year in data selection.

#### Bubbles: 
##### Given price preferences and years, the bubbles are created with d3-hierarchy (with no hierarchy), by updating amount of circles and calculating the radius given number of wines in the chosen dataset. Further on, a large dict of the chosen dataset is created with the function winesPerCountry. Here are calculations made for bubble chart (number of wines), histogram (frequency of points) and donut chart (number of each variety and remembering cheapest top 5). The tips are made with d3. The location of the tip went all crazy, so I restrained to location of the circle where the mouse hovers over. The chosen country is a global variable.

#### Histogram:
##### Histogram is updated by updating x (scaleBand), y (scaleLinear) axis domain bounds, deleting previous bars, appending new bars. When the mouse hovers over a bar, the tooltip calculates the average price of the current bar. The clicked bar is remembered by making it a global variable. 

#### Donut:
##### To make the donut chart, d3-pie is used. The size of each slice is computed by making the angle of the slice depend on # wines of that variety in current selection. The top 5 is retrieved from the given choices and dictionary calculated at the bubble chart.

## Challenges: 

### Learning d3, javascript again:
#### After first picking the right project, re-using d3 and javascript after more than a year (i did the minor, but the project, in 2018/2019) was the next challenge. Especially the asynchronic way of dealing with data in javascript was forgotten. But within a couple of days I was again used to it.

### Way of choosing years
#### I wanted a sort of dynamic and intuitive use of the timeslider (so many options, clear current choice, with little buttons). The solution was the use of 'locking'-year buttons. It certainly took 1/2 days and (a lot of) logic thinking to get this right.  

### Making bubble chart:
#### I first implemented a bubble chart on my own, by letting the circles go in circles around the middle circle (add 360/5 degrees to each step, and enlarge radius to middle circle per 5 steps). I kept it for 1.5 week until i the decided the monday of the last week to use d3-hierarchy. This made a whole lot nicer bubble chart. 

### Calculate preference data
#### One recurring question during the making of the whole project, was to know when, what and how to calculate the necesarry values for each graph in an efficient way. The challenge was to computate as little as possible at each new user choice, (otherwise it gets slow) without losing any information.

### Styling
#### The last days before the deadline I was struggling with getting CSS working on my code. I kept postponing styling to a later moment (gave priority to fixing functionalities), until I was forced to leave the styling as it was, due to lack of time. 

## Decisions: 
### The 'dynamic' time slider (year 'dynamic' choices) was better to do than, for example, two dropdowns/checkboxes to choose your years. Firstly because it esthetically nicer and gives more dynamics to the vizualisation. The trade-off is that the timeslider shows years which are not in included in the dataset because the d3-simple-slider takes step(1). The fix for this is to select the last valid year, and update this when sliding over a new valid year.

### The large circle legenda is chosen for this form because due to lack of time I could not place all circles together on 1 position and add legenda to show value of each circle. This would have save a lot of space.  

### No legenda for donut diagram because I think people intuitively connect the color red to red wines, and white to white. But a small explanation of the grey slice would have stood good. Those are the wines which were not included in the retrieved list of white and red wines.

### No partical colors for countries is chosen because the color would not represent anything. The trade-off is that you can't see that some continents are largely represented (Europe) and some not (Africa, Asia)). But this feels trivial to say, because the countries showed have typically a wine tradition, and the countries not showed, not.    