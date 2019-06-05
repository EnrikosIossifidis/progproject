

    a list of data sources if you will get data from an external source, including information on how your are going to filter and transform the data for your project

    a diagram with an overview of the technical components of your app (visualizations, scraper etc etc)

    as well as descriptions of each of the components and what you need to implement these

    a list of APIs or D3 plugins that you will be using to provide functionality in your app

### List of data sources

https://www.kaggle.com/zynicide/wine-reviews/downloads/wine-reviews.zip/4

The following information is needed from the dataset (including way of filtering and transforming):
* wine number (first column): Assign wine number to wine.
* country of wine (second column): Retrieve wine's country from dataset and assign it to wine.
* points (fifth column): Retrieve wine's points from dataset and assign it to wine.
* price (sixth column): Retrieve wine's price from dataset and assign it to wine.
* year (twelfth column): Filter year uit of wine's title by checking which word in title is an integer.
* sort of wine (thirteenth column): Retrieve sort of wine from dataset and assign it to wine.

optional
* Most used wine characteristics (third column): Count all words in data selection of the user and make a top 5 of terms that are typical wine descriptor words.

### List of APIs or D3 plugins
