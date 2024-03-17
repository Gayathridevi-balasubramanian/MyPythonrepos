############
#creating data in csv format into dataframe and to a dictionary data
##############
import pandas as pd
from io import StringIO

csv_data = '''Planet,Mass (kg),Diameter (km),Distance from Sun (million km)
Mercury,3.285e23,4879,57.9
Venus,4.867e24,12104,108.2
Earth,5.972e24,12742,149.6
Mars,6.39e23,6779,227.9
Jupiter,1.898e27,139820,778.5
Saturn,5.683e26,116460,1433.5
Uranus,8.681e25,50724,2872.5
Neptune,1.024e26,49244,4495.1
'''
data = StringIO(csv_data)
print(data)
print(data.getvalue())


print("The dataFrame value are:" ,pd.DataFrame(data))
df = pd.DataFrame(data)

# Specify the file path for the CSV file
csv_file_path = 'planets.csv'

# Convert the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
# f  = open('planets.csv','r')
# for line in f.readlines():
#     print(line)

df = pd.DataFrame.from_records('planets.csv')
print("The operations need performed on the dataframe:")
print(df.dtypes)

# Assuming df is your DataFrame

# Check if the DataFrame is empty
if df.empty:
    print("DataFrame is empty.")
else:
    # Print the data types of each column
    print("The operations need performed on the dataframe:")
    print(df.dtypes)

    # Perform describe operation on all columns
    print("\nDescriptive statistics for all columns:")
    print(df.describe())

print(df.mean)
print(df.median)
print(df.mode)
