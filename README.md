#### Enrikos Iossifidis 10805672

### Find Your Vino

### Problem Statement
Everyone has met a person once who talks about wines like he is the only connaisseur in the world who knows something of it or had a (special) occassion where you were searching and searching for just the right wine for the right price. The only problem is that there are millions of wines, so you get easily drown in the stream of wine supply and end up with a disappointed feeling and even more dissapointing wine...

### Solution:

This vizualisation attempts to give a clear view of where you will find per sort wine, the most and the best ones (of which are reviewed). 

### Screen shots:

### Begin screen:
![alt text](https://raw.githubusercontent.com/enrikosiossifidis/progproject/doc/welcome_text_user_choices.png)

#### Here you can choose:

#### Price category:
Your choice only changes when you pick a different category (so two times choosing 1 does not do anything). If category in selected, then chosen category will be deleted. If category chosen not in current selection, the chosen category will be added.

#### Years:
No ' year button' clicked, shows all years within price category. If you want a period FROM - Choose Year, then click the left 'button' such that it is red, and slide to the right. If you want period Chosen Year - UNTIL, click the left 'button' such that it is red and slide to the left.

### Bubble chart screen:
![alt text](https://raw.githubusercontent.com/enrikosiossifidis/progproject/doc/bubble_chart.png)

Here the bubbles are update for each price/year reference. The size of the bubble depends on the number of wines from the country in the chosen dataset. Click a bubble to update the histogram.

### Histogram and Variety Donut:

![alt text](https://raw.githubusercontent.com/enrikosiossifidis/progproject/doc/hist_donut_best_cheapest.png)

#### The clicked bubble country is shown in a histogram. The x axis represents the points it. Click on a bar to update the donut chart. 

#### Click on a slice of the donut chart to show the top 5 cheapest wines (we are students) in your chosen category!

### Data Sources:

https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4

### External Components

* d3-tip
* d3-simple slider

### Similar example: 

#### Packed bubble chart and timeline:
http://vallandingham.me/bubble_cloud/#mind 

They have implemented it by using by using bootstrap, css and coffeescript package. My ambitions are to first make a self made static packed bubble chart with self made tip. And that the bubbles' sizes change if you swipe over the timeline. And I want to give myself a try to program an easy cluster algorithm. To make it smooth and dynamic is optional for me.

#### Histogram:
http://bl.ocks.org/nnattawat/8916402

They used no extraordinary libraries other than d3 and css.

#### Dynamic donut chart:
https://bl.ocks.org/mbhall88/22f91dc6c9509b709defde9dc29c63f2

Complexer than the histogram, but I think it is not impossible to make a changing donut charts by myself.

### Hardest parts:

* Creating a bubble chart where size of a country's bubble changes over time, but where the group of bubbles stays together.
* Make the donut chart dynamically change form and labels.




