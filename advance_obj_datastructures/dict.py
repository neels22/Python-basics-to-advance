


d = {'k1':1,'k2':2}

print({x:x**2 for x in range(10)})


print( {k:v**2 for k,v in  zip(['a','b'],  range(10) ) }    )


print(d.items())

for k in d.items():
    print(k)


for k in d.keys():
    print(k)
for k in d.values():
    print(k)




