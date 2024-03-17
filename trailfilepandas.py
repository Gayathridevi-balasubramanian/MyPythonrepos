import pandas as pd

# Import pandas


# Create a simple DataFrame (you can replace this with your data)
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print("To print the names alone:")
print(df['Name'])
print("To manipulate the columns")
df['Name_city'] = df['Name'] + '   ' + df['City']
print(df['Name_city'])
print("To extract data with the conditions:")
print(df['Age'] > 30)
print(df[df['Age'] > 30])


# to export the csv file
df.to_csv('tdataframe.csv', index = False)


iris = pd.read_csv('tdataframe.csv')
print(iris.shape)
print(iris.head(1))
print(iris.tail(1))

print("DataFrames datatypes: dtypes")
print(iris.dtypes)
print(iris.loc[1:2])
print(iris.iloc[1,0])
print(iris.index)
print("the loc prints the required rows and columns mentioned in that")
print(iris.loc[[1,2],['Name_city']])

# Creating a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])

# Using loc to select specific rows and columns by labels
selected_data = df.loc[['row1', 'row3'], ['A', 'C']]

print(selected_data)