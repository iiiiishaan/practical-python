
total_cost = 0.0
file = open("/home/ishaan/practical-python/Work/Data/portfolio.csv", "rt")
headers = next(file).split(',')
headers

for line in file:
	row = line.split(",")
	print(row)


	shares = int(row[1])
	prices = float(row[2])

	total_cost += shares*prices

	print(total_cost)
