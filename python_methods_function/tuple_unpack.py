
# example 1
stock_price=[ ('apple',100), ('micro',1000)  ]
for ticker,price in stock_price:
    print(ticker)
    print(price + (0.1*price))

# example using tuple unpacking using functions 
work_hours = [('neel',100000),('neelay',232323)]
def employee_check(work_hours):
    curr_max = 0
    emp_of_month = ''

    for name,hours in work_hours:
        if hours > curr_max:
            curr_max = hours
            emp_of_month = name
    
    return (emp_of_month,curr_max)
name,hours = employee_check(work_hours)
print(name , hours)
res = employee_check(work_hours) # another way to accept return
print(res)
    


