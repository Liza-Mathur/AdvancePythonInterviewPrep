tables = [[k*i for k in range(1,11)] for i in range(1,6)]
print(tables)

string = "My name is Liza Vowel. I am here to count Vowel. Like A like E and I O U"
# normal method - 
dicts = {}
for k in 'aeiou':
    if k in string.lower():
        dicts[k]= string.lower().count(k)
print(dicts)

# dict comprehension
dictComp = {k : string.lower().count(k) for k in 'aeiou' if k in string.lower()}
print(dictComp)

sets = set()
string2 = "My name is liza mathur."
sets = {k for k in string2 if k in 'aeiou'}
print(sets)

'''
Output - 
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]
{'a': 5, 'e': 8, 'i': 6, 'o': 5, 'u': 2}
{'a': 5, 'e': 8, 'i': 6, 'o': 5, 'u': 2}
{'a', 'u', 'e', 'i'}
'''