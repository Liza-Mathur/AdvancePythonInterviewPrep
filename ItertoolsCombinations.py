from itertools import combinations

list1 = [1,2,3,4,5]

k = combinations(list1, 4)
print(k)
for tups in k:
    print(tups)