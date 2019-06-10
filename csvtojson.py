import pandas as pd 
import numpy as np
import json
import operator
from operator import itemgetter


def findyear(wine):

	# find the integer in wine title
	words = row['title'].split()
	numbers = [int(word) for word in words if word.isdigit()]
	year = [number for number in numbers if number > 1900 and number < 2019]

	# year wine house is always < year wine produced
	if len(year) == 2:
		return max(year)
	elif len(year) == 1:
		return year[0]
	else:
		return False

# import data
data_path = 'C:/Users/enrik/Desktop/PROMPROJECT/Data/winemag-data-130k-v2.csv'
data = pd.read_csv(data_path)
testdata = data.iloc[:1000]

choicedata = data

# insert wine in right year and country
dictWineYears = {i: {} for i in range(1900, 2020, 1)}
for index, row in choicedata.iterrows():

	# delete wine if no year is mentioned
	year = findyear(row)
	if not year:
		choicedata.drop(index)
	else:
		if row['country'] not in dictWineYears[year]: 
			dictWineYears[year][row['country']] = []
		
		dictWineYears[year][row['country']].append({

		"Title": row['title'],
		"Points": row['points'],
		"Price": row['price'],
		"Variety": row['variety'],
		"Description": row['description']
	})

# delete empty years
todel = []
for key in dictWineYears.keys():
	if len(dictWineYears[key]) == 0:
		todel.append(key)

for t in todel:
	del dictWineYears[t]

with open('winesData.json', 'w') as output:
	json.dump(dictWineYears, output)

# with open('resserd.json', 'w') as fp:
#     json.dumps(dictWineYears)