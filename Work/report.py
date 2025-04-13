# report.py
#
# Exercise 2.4

import csv 

def read_portfolio(filename):
	portfolio = []
	total = 0.0	
	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			money = {
				'name': row[0],
				'shares' : int(row[1]),
				'prices' : float(row[2])
				}
			portfolio.append(money)

		return portfolio

def read_prices(filename):
	paisa = []
	total_two=0.0
	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			if len(row)>=2 and row[0].strip() and row[1].strip():
				try:
					bucks = {
						'names': row[0],
						'prices': float(row[1])
						}
					paisa.append(bucks)

				except ValueError:
					print('hahahah')
		return paisa


portfolio = read_portfolio('/home/ishaan/practical-python/Work/Data/portfolio.csv')
paisa = read_prices('/home/ishaan/practical-python/Work/Data/prices.csv')


Money = {item['names']:item['prices'] for item in paisa}

total_cost = 0.0
for s in portfolio:
	total_cost += s['shares']*s['prices']

print(total_cost)	

total_value =  0.0
for s in portfolio:
	if s['name'] in Money:
		total_value += s['shares']*Money[s['name']]
	else:
		print('error')
print(total_value)

print('gain',total_value - total_cost)
