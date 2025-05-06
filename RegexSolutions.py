import regex as re

email = "My email is liza.mathur0803@hcl.com and lisamathur@gmail.com I like it"

print(re.findall("[a-zA-Z0-9.]+@[a-zA-Z0-9.]+", email))
# print(re.search(".+@.+", email)) - Not working properly

# print(re.search(".+[^\\s]@.+[^\\s]", email).group())


hastagsString = "My name is #Liza and I am writing a #hastag string"
print(re.findall("#[A-Za-z0-9.]+", hastagsString))

numsString = "My number is 09 and 2 asnd 4"
print(re.sub("[0-9]", "#", numsString))

'''
Output of the code is - 
['liza.mathur0803@hcl.com', 'lisamathur@gmail.com']
['#Liza', '#hastag']
My number is ## and # asnd #
'''

