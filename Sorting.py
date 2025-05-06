namesList = ['priyanshu','kratika','sushm','lizz']
sortedNames = sorted(namesList, key = lambda x : x[-1])
print(sortedNames)

data = [
  {"name": "Alice", "details": {"age": 25}},
  {"name": "Bob", "details": {"age": 22}},
  {"name": "Charlie", "details": {"age": 30}},
]

dataSorted = sorted(data, key = lambda x : x['details']['age'])
print(dataSorted)

"""
Output - 
['kratika', 'sushm', 'priyanshu', 'lizz']
[{'name': 'Bob', 'details': {'age': 22}}, {'name': 'Alice', 'details': {'age': 25}}, {'name': 'Charlie', 'details': {'age': 30}}]
"""