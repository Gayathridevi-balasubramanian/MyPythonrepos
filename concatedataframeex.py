import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame):
    return  pd.concat([df1, df2], axis=0)
    
# Sample data for df1
data1 = {'student_id': [1, 2, 3],
         'name': ['Alice', 'Bob', 'Charlie'],
         'age': [20, 22, 21]}

# Create DataFrame df1
df1 = pd.DataFrame(data1)

# Sample data for df2
data2 = {'student_id': [4, 5, 6],
         'name': ['David', 'Eve', 'Frank'],
         'age': [19, 23, 20]}

# Create DataFrame df2
df2 = pd.DataFrame(data2)

# Display the DataFrames
print("DataFrame df1:")
print(df1)

print("\nDataFrame df2:")
print(df2)

print("\nConcate two tables\n")
s = concatenateTables(df1,df2)
print(s)
