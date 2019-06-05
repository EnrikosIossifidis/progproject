#### Enrikos Iossifidis 10805672

## Project proposal: Wine Selecter

### Problem Statement
Everyone has met a person once who talks about wines like he is the only connaisseur in the world who knows something of it or had a (special) occassion where you were searching and searching for just the right wine for the right price. The only problem is that there are millions of wines, so you get easily drown in the stream of wine supply.    

### Solution:

This vizualisation attempts to give a clear view of where you will find per sort wine, the most and the best ones (of which are reviewed). 

### Minimum valuable product

* The user can pick a year (with a timeslide) and price category (checkbox for each category)
* Bubble chart with a bubble per country. The size of the bubble depends on how many wines are from the country in the dataset, which is based on user's choices. 
* The bubble size per country changes per year and price category, but the total cluster of bubbles stays together.
* A bubble's tip shows the name of the country and amount of wines from that country in the data selection.
* Histogram that shows how many wines there are in each price category in the country that is clicked in the bubble chart. The bars from the histogram change dynamically.
* Donut chart which shows that shows the distribution of type of grapes in a country which are reviewed.

#### Optional

* The bubbles move dynamically.
* A bubble's tip shows beside name and amount of wines (minimum) also the top 5 of most used wine characteristics to describe the wine.
* Make the donut chart into rose chart. With the frequency of wine sort as the breadth of the circle's slice and the height of the average wine sort score.

### Data Sources:

https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4

### External Components

* d3-tip
* d3-tooltip
* d3-bar
* d3-labeler

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




