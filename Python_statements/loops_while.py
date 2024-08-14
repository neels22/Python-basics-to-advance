

# while some condition is true execute the block of code
# can pair with else 

x= 0
while x < 5:
    print(f"current x is: {x}")
    x+=1
else:
    print("x is not less than 5")


# break -- comes out of the loop -- closest enclosing loop
# continue -- skips that iteration
# pass --does nothing at all to avoid errors

for i in 'asd':
    if i =='s':
        break
    print(i)

for i in 'asdf':
    if i == 'd':
        continue
    print(i)

for item in 'heell':
    pass 

x = 0 
while x < 5:
    if x == 3 :
        break
    print(x)
    x += 1