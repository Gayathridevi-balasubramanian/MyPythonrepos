import pandas as pd
# cleaning and processing the text data
name = pd.Series(['Pomeray, CODY  ','   wagner; Jarry','smith , Ray'])
names = name.str.replace(';',',')
print(names)
print(names.describe())
print(names.str.len())
#strip() to trim the spaces in the front and end of the strings
print(names.str.strip())
names = names.str.strip()
print(names.str.len())
# lower() to turn into the lower case letters
print("lower function")
print(names.str.lower())
print("upper function")
print(names.str.upper())
print("Captilize function")
print(names.str.capitalize())
print("split function")
names = names.str.split(',') 
print(names[0])
print(names[1])
print("reverse function")
n = pd.Series([i[::-1] for i in names])
print(n)
print("append function")
print([' '.join(i) for i in n])


