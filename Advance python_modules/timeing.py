

import time
def funcone(n):
    return [str(num) for num in range(n)]

res = funcone(10)
print(res)

def  functwo(n):
    return list(map(str,range(n)))

res = functwo(10)
print(res)



#current time before code
start_time = time.time()

# run the code

res = funcone(1000000)
# after code runs

end_time = time.time()

# elapsed time

total = end_time - start_time
print(total)


#current time before code
start_time = time.time()

# run the code

res = functwo(1000000)
# after code runs

end_time = time.time()

# elapsed time

total = end_time - start_time
print(total)



import timeit

stmt = '''
funcone(100)
'''

setup = '''
def funcone(n):
    return [str(num) for num in range(n)]
'''

res = timeit.timeit(stmt,setup,number=1000000)
print(res)  # function one takes how much time to run a number of times

stmt2 = '''
functwo(100)
'''

setup2 = '''
def functwo(n):
    return list(map(str,range(n)))
'''

res = timeit.timeit(stmt2,setup2,number=1000000)
print(res) # function one takes how much time to run a number of times