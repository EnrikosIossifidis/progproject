import pandas as pd 
import numpy as np
import json
import math
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
testdata = data.iloc[:100000]

choicedata = testdata

# insert wine in right year and country
dictWineYears = {i: {j: {} for j in range(1900,2020)} for i in range(1,5)}
varieties = {}
for index, row in choicedata.iterrows():

	# delete wine if no year or price is mentioned
	if not math.isnan(row['price']):
		print(index, row['variety'])
		# calculate the wine's price category
		priceCat = 0
		if row['price'] <= 25:
			priceCat = 1
		elif row['price'] <= 50:
			priceCat = 2
		elif row['price'] <= 75:
			priceCat = 3
		else:
			priceCat = 4

		year = findyear(row)
		if not year:
			choicedata.drop(index)
		else:
			if row['country'] not in dictWineYears[priceCat][year]: 
				dictWineYears[priceCat][year][row['country']] = []
			dictWineYears[priceCat][year][row['country']].append({
			"Title": row['title'],
			"Points": row['points'],
			"Price": row['price'],
			"Variety": row['variety'],
			"Description": row['description']
			})

		if row['variety'] not in varieties:
			varieties[row['variety']] = 1;
		else:
			varieties[row['variety']] += 1;

print(sorted(varieties.items(), key=operator.itemgetter(1)))

# delete empty years
for cat in dictWineYears.keys():
	todel = []
	for key in dictWineYears[cat].keys():
		if len(dictWineYears[cat][key]) == 0:
			todel.append(key)

	for t in todel:
		del dictWineYears[cat][t]

with open('test10.json', 'w') as output:
	json.dump(dictWineYears, output)

# with open('resserd.json', 'w') as fp:
#     json.dumps(dictWineYears)
