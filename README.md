#### Enrikos Iossifidis 10805672
https://enrikosiossifidis.github.io/progproject/
## Find Your Vino

## Problem Statement
Everyone has met a person once who talks about wines like he is the only connaisseur in the world who knows something of it or had a (special) occassion where you were searching and searching for just the right wine for the right price. The only problem is that there are millions of wines, so you get easily drown in the stream of wine supply and end up with a disappointed feeling and even more dissapointing wine...

## Solution:

This vizualisation attempts to give a clear view of where you will find per sort wine, the most and the best ones (of which are reviewed). 

## Screen shots:

### Begin screen:
![alt text](https://enrikosiossifidis.github.io/progproject/doc/pictures/welcome_text_user_choices.PNG)

#### Here you can choose:

#### Price category:
Your choice only changes when you pick a different category (so two times choosing 1 does not do anything). If category in selected, then chosen category will be deleted. If category chosen not in current selection, the chosen category will be added.

##### Years:
No ' year button' clicked, shows all years within price category. If you want a period FROM - Choose Year, then click the left 'button' such that it is red, and slide to the right. If you want period Chosen Year - UNTIL, click the left 'button' such that it is red and slide to the left.

### Bubble chart screen:
![alt text](https://enrikosiossifidis.github.io/progproject/doc/pictures/bubble_chart.PNG)

Here the bubbles are update for each price/year reference. The size of the bubble depends on the number of wines from the country in the chosen dataset. Click a bubble to update the histogram.

### Histogram and Variety Donut:

![alt text](https://enrikosiossifidis.github.io/progproject/doc/pictures/hist_donut_best_cheapest.PNG)

The clicked bubble country is shown in a histogram. The x axis represents the points it. Click on a bar to update the donut chart. 

Click on a slice of the donut chart to show the top 5 cheapest wines (we are students) in your chosen category!

### Data Sources:

#### Wine Data:
https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4

#### Red wine list:
http://www.all-about-wine.com/red-wine-list.html

#### White wine list:
http://www.all-about-wine.com/white-wine-list.html

### External Components

* d3-tip
* d3-simple slider
* d3-hierarchy
* d3-pie






