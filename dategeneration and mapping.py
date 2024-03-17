import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
date_range = pd.period_range(start='1/1/2019', freq='1d', periods=50)
print(date_range)
df= pd.DataFrame(date_range, columns=['day'])
print(df)
# df['value 1'] = np.random.randint(20,45)
df['value 1'] = np.random.randint(20,45, size=len(df))
print(df)
df['value 2'] = np.random.random_sample((len(df),)) # using sample() alone will generate the same value throughout the column
print(df)
df = df.head(40)
df.plot()
plt.show()

df.plot.area(stacked=False)
plt.show()

df.plot.bar(x='day', subplots=True, color=['orange','yellow'])
plt.show()

df.plot.bar()
plt.show()

df.plot.hist()
plt.show()

iris = pd.read_csv('iris.csv')
iris.plot.hist()
plt.show()

iris.plot.hist(by='species')
plt.show()

iris[['sepal_length','sepal_width']].plot.hist()
plt.show()
# Sample DataFrame
data = {'price': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)


iris.plot.scatter(x='sepal_length', y='sepal_width',c=['orange'])
plt.show()

iris.plot.line()
plt.show()
colors = {"versicolor":"red",
          "setosa":"green",
          "virginica":"blue"}
iris['colors'] = iris['species'].map(colors)
iris.plot.scatter(x='sepal_width', y='sepal_length',color=iris['colors'])

scatter_matrix(iris,figsize=(15,9))
# Generate a random sample for 'value 2'
df['value 2'] = np.random.random_sample((5,))

# Display the DataFrame
print("Updated DataFrame:")
print(df)