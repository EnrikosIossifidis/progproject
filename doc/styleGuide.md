# Style Guide:

### Tabs and spaces: 
1 enter after each function, for loop, if + tab on next line


### White space: 
One white space between each function + one above each comment line 

### Naming of variables and functions: 
Use of camelcase

### Proper naming of variables and functions:

A short description (camelcase) of what the variables holds, or what the function does.

### Code grouping organization: 

##### 1) declare all general variables, 
##### 2) Initialize each feature (price cats, timeline, bubbles, histogram, donut) 
##### 3) update each feature.
##### 4) split calculations in update into new function

### Patterns to be used:

#### Standard d3 update (for bubbles, top 5 text): (selectAll-exit().remove()-update-append new)
#### Other update (histogram bars, donut slices): remove old, draw new pieces.