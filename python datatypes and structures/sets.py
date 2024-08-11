

# unordered collection of unique objects
# 

my_set = set()

my_set.add(1)

print(my_set) # output -> {1}
# this doesnt mean they are dictionaries remebers they have key value here its only value

my_set.add(2)
my_set.add(2)
my_set.add(3)
my_set.add(3)

print(my_set)

####
print(set([1,1,2,3])) # output: {1,2,3}
