import pandas as pd
import seaborn as sns

df = pd.read_csv('D:\pythonprogrammingfiles\AB_NYC_2019.csv')
print(df.head(10))
print(df.dtypes)

            
# plotting

print(df['availability_365'].value_counts().head(10).plot(kind='bar'))
s = sns.barplot(data=df.head(10), x='name', y='number_of_reviews',)
print(s)

df.head(10)
distinctvalues = df['neighbourhood_group'].unique()
print(distinctvalues)
distinctvalues
#sorting our result
order1 = df['neighbourhood_group'].value_counts().index
df['room_type'].unique()
sns.countplot(data = df, x = 'neighbourhood_group' , order= order1 , hue= 'room_type')

df['room_type'].unique()