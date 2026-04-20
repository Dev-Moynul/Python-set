set1={1,2,3,4,'ai',(1,5,7,10)}
print(type(set1))
print(set1)
set1.add(100)
print(set1)
set1.update([400,300,500])
print(set1)
set1.remove('ai')
print(set1)

# set1.remove(53) element na thakle error dekhabe

set1.discard(43)
print(set1)
set1.clear()
print(set1)
data={4,7,9,10,'Moynul','queue'}
print(type(data))
print(data)
data.add(34)
print(data)
data.update(['nice','beautiful girl','excelent'])
print(data)
s=frozenset(data)
print(s)
s.add(5)