
import csv

total_cost = 0.0
file = open("/home/ishaan/practical-python/Work/Data/portfolio.csv", "rt")
rows = csv.reader(file)
headers = next(rows)
headers

for row in rows:
	
	print(row)


	shares = int(row[1])
	prices = float(row[2])

	total_cost += shares*prices

	print(total_cost)
