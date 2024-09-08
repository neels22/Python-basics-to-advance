


s = set()

s.add(3)
s.add(2)
s.add(4)

s.clear()
print(s)

s = {1,2,3,4,5,4,47,5}
print(s)

# sc= s.copy()
sc = {3,4}
print(sc)


print(s.difference(sc))

s1 = {1,2,3}
s2 = {2,3,4,5}

print(s1.difference_update(s2))  # removes common elements
print(s1)


s.discard(3)
print(s)

####



s1 = {1,2,3}
s2 = {2,3,4,5}
print('\n')
print(s1.intersection(s2))


print(s1.intersection_update(s2)) # first set equal to intersection
print(s1)


#######


s1 = {1,2,3}
s2 = {2,3,4,5}
s3 ={5}
print('\n')
print(s1.isdisjoint(s2))

print(s1.issubset(s2))

print(s2.issuperset(s1))


print(s1.symmetric_difference(s2))

#####

print(s1.union(s2))


print(s1.update(s2))
print(s1)