mortgage = 500000
rate = 0.05
total_payment = 0.0
monthly_payment = 2684.11

while mortgage>0:
    mortgage = mortgage + mortgage*rate/12 - monthly_payment
    total_payment = total_payment + monthly_payment

print("total:",total_payment) 
