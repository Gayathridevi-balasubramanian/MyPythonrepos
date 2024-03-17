import pandas as pd
import numpy as np

data = pd.read_csv('AB_NYC_2019.CSV')
bins = [0,20,40,60,80,np.inf]
labels = ['LowReturn','BelowAvgReturn','Avg Return ','Avg Return','High Return']
df = data.loc[:,['name','host_name','neighbourhood','price']].head(10)
print(type(df))
df= pd.DataFrame(df)
print(type(df))
print(df.dtypes)
print(df.head(10))
df['count category'] = pd.cut(df['price'], bins, labels= labels)
print(df)

########################################################################
print("########################################################################")
# Sample DataFrame
df = pd.DataFrame({'price': [10, 25, 40, 60, 80]})

# Define bins and labels
bins = [0, 30, 60, 100]
labels = ['Low', 'Medium', 'High']

# Create 'count category' column based on 'price'
df['price category'] = pd.cut(df['price'], bins, labels=labels)

# Display the DataFrame with the new column
print(df)

############
# mapping the dict to a values in the columns using map function
# see applymapexercises.py
##############

########################################################################
print("########################################################################")
print("########################################################################")
import pandas as pd

# Sample DataFrame
data = {'price': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)

# Define bins and labels for the categorical column
bins = [0, 15, 25, 35]
labels = ['Low', 'Medium', 'High']

# Create a categorical column based on 'price'
df['price category'] = pd.Categorical(pd.cut(df['price'], bins, labels=labels), ordered=True, categories=labels)

# Display the DataFrame
print("Original DataFrame:")
print(df['price category'])


print("########################################################################")
print(df.sort_values(by='price', ascending=False))


print("########################################################################")
print(pd.get_dummies(df['price category']))