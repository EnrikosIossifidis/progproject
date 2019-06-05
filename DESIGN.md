
    a diagram with an overview of the technical components of your app (visualizations, scraper etc etc)

    as well as descriptions of each of the components and what you need to implement these

## Design Document

### List of data sources

Wine data:
https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4


The following information is needed from the dataset (including way of filtering and transforming):
* wine number (first column): Assign wine number to wine.
* country of wine (second column): Retrieve wine's country from dataset and assign it to wine.
* points (fifth column): Retrieve wine's points from dataset and assign it to wine.
* price (sixth column): Retrieve wine's price from dataset and assign it to wine.
* year (twelfth column): Filter year uit of wine's title by checking which word in title is an integer.
* sort of wine (thirteenth column): Retrieve sort of wine from dataset and assign it to wine.



For the dynamic bubble chart with different bubble sizes, some aspects of the two examples below will be used:
https://bl.ocks.org/HarryStevens/27a440b621960899f4584034919aa9f7
https://bl.ocks.org/maegul/7d8e7342c649fdc077a6984e52da4b62

Optional
* Most used wine characteristics (third column): Count all words in data selection of the user and make a top 5 of terms that are typical wine descriptor words.

### List of APIs or D3 plugins

* d3-beeswarm
