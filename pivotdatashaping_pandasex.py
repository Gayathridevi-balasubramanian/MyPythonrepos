######################################
''' converts rows into the columns
    Identity column for index (row) you want to convert
    Identity column for columns (columns) you want to convert
    Identity column for variables (values representing rows and columns) you want to convert
    '''
######################################
import pandas as pd

def pivotTable(weather: pd.DataFrame):
    return  weather.pivot(index='month', columns='city', values='temperature').fillna(0)


# Sample data
data = {'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso'],
        'month': ['January', 'February', 'March', 'April', 'May', 'January'],
        'temperature': [13, 23, 38, 5, 34, 20]}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print(pivotTable(df))