
# ordered sequencing of elements 
# support indexing and slicing 
# reverse indexing also works


##################### 

my_list = [1,2,3]
print(my_list[1])
print(len(my_list))

##################### 

# slicing
print(my_list[1:])

# concatenate lists
another_list = ["neel",3.3,100]
new_list = my_list + another_list
print(new_list)

# modification
new_list[0] = "hello"
print(new_list)

# appending at the end
new_list.append('six')
print(new_list)

# removing from the end
ele = new_list.pop()
print(ele) #popped item
print(new_list)

# sorting lists
new_list = ['a','e','x','b','c']
print(new_list.sort()) # sorts the list in alphabetical order returns None
print(new_list)
# NoneType is return value of functions that doesnt return anything -- sort doesnt return anything 

# reversing the list using .reverse
new_list.reverse()
print(new_list)

# Nested lists
nest = [1,2,['hello',33]]
print(nest[2][1])





















