




l = [2,3,4,5,3,3,4,4]

l.append(3)

print(l.count(3))

x = [1,2,3]

print(l.extend(x)) # adding the elements from another list 

print(l)

print(l.index(3))

print(l.insert(1,'inserted'))
print(l)

ele = l.pop() # pass the index 
print(ele)

ele = l.remove(3) # remove first occurence of the value

print(ele)


l.reverse()

l.sort()





