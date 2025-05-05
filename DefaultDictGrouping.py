from collections import defaultdict

data = [
    ('fruit', 'apple'),
    ('fruit', 'banana'),
    ('vegetable', 'carrot'),
    ('fruit', 'mango'),
    ('vegetable', 'spinach')
]

keys = set()
result = {}
for (k,v) in data:
    if k in keys: 
        result[k].append(v)
    else:
        keys.add(k)
        result[k] = [v]
    
print(result)

defDict = defaultdict(list)
for k,v in data:
    defDict[k].append(v)

print(defDict)