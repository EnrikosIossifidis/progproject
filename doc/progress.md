### Monday Week 1
Made and pushed project proposal (Line graph, heat map and circle graph). It was a solution for policy makers to find the best route for co2 emission reduction regarding coal and gas based power plants.

### Tuesday Week 1
Gathered data and calculated minor parameters for the data vizualisation. But after discussing with Nigel about the project, we decided it did not fit the purpose of the course. 

### Wednesday Week 1
Made plan proposal and design document of new proposal.

New plan: Data vizualisation of wine reviews from all over the world and from all price categories. New proposal: User's choices: Timeslide, Pick Price Category. Vizualisations:  ##Bubble chart## of countries, where bubble size represents number of wines in chosen dataset from that country. When the user clicks on a bubble, a ##Histogram## appears with x-axis: score category (100-90, 90-80, etc.), y-axis: frequency. Beneath the histogram a  ##Donut Graph## is viewed which shows the distribution of wine sorts wihtin score category (Optional: User can choose score category with dropdown menu, otherwise mean is showed).

### Thursday Week 1
Finished design document and started with preparing data. The data from the source was per row a wine with including review. There was no 'year'-column. It was mentioned in the 'Wine title'-column, so I needed to filter the year out. This happens in csvtojson.py.

### Friday Week 1
Next up was sorting the data by year and organize the wines within each year by country.

### Monday Week 2
Started with making the index.html page and javascript file. Trying to make the bubble chart. (But mostly refreshing HTML, JS, D3 knowledge because it's +1 year ago that I last touched it.)

### Tuesday Week 2
Value showed bubble chart is # times a country appears in data selection. Try to make bubble chart by placing next country at slightly different angle in a "ring" of countries (each ring with different radius from centre) 

### Wednesday Week 2
Further working on bubble chart (fixing angles and radius and calculating bubble coordinates). And begin to self-made timeslider

### Thursday Week 2
Trying to make axes of histograms. There is a hard bug why axises just won't appear.

### Friday Week 2
Axises appeared! Now trying to update scales when different bubble is clicked

### Monday Week 3
Axises values change when different bubble is clicked. Rest of the day trying to make bars.

### Tuesday Week 3
Bars fixed. Further on the old self-made timeslide is thrown away. New timeslide (plug-in). Trying to adjust bubble chart data on basis of chosen years.

### Wednesday Week 3
Make bubbles change with chosen years. Further on a begin is made to donut chart. And price categories is added.

### Thursday Week 3
Timeslider updates when different price categories are picked. Further on: Fixing problems with passing on data and choices between: picked price categories -> years -> bubbles -> hist -> donut.

### Friday Week 3
Donut chart is minimal working. Further working on fixing data bugs when passing on user choices (especially years-> bubbles, bubbles -> hist). 

### Monday Week 4
Whole data stream works and is complete. Only issue is that bubble chart is not working optimal and esthetically not so pretty as examples on the internet. So i'm going to let me inspire on the web and change the bubble chart.

### Tuesday Week 4
Made whole bubble chart. Works smoothly, very content!

### Wednesday Week 4
Fixed final bugs. Unfortunately CSS editing did not work and assistance was not available so no nice effects...

### Thursday Week 4
### Friday Week 4
PRESENTATIE