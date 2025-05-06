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