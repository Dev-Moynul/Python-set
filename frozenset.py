s={2,5,6,7,9,8}
s1=frozenset(s)
print(type(s1))
print(s1)
s2={2,3,4,6,7,10}
s3=frozenset(s2)
print(s3)
print(s1.union(s3))
print(s1.intersection(s3))

data="I love python and also data science"
s4=frozenset(data)
print([list( x ) for x in s4])
print([tuple( x ) for x in s4])
print([set( x ) for x in s4])