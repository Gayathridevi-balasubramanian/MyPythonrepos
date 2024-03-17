import pandas as pd

df = pd.DataFrame({
    "Region":['North','West','East','South','North','West','East','South'],
    "Team":['one','one','one','one','two','two','two','two'],
    "Squad":['A','B','C','D','E','F','G','H'],
    "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
    "Cost":[5200,5100,4400,5300,1250,1300,2100,50]
                })
print(df)
print("\n\nAfter applying the apply() on all the columns to calculate new values or another columns")
df['Profit'] = df.apply(lambda x:'Profit' if (x['Revenue']-x['Cost'] >= 0) else 'Loss', axis=1)
print(df)

#create a dictionary
team_map = {
    "one":"Red",
    "two": "Blue"
}
df['Team Color'] = df['Team'].map(team_map)
print("Applying a map function based on value of the another column")
print(df)

# applies on all the elements in the dataframe
print(df.applymap(lambda x: len(str(x))))
print(df.map(lambda x: len(str(x))))

#if all else fails, use a for loop

new_list = []
new_list1 =[]
for i in range(0, len(df)):
    rev = df['Revenue'][i]/df['Revenue'].sum()
    new_list.append(rev)

for i in range(0, len(df)):
    rev = df['Revenue'][i]/df[df['Region']==df.loc[ i , 'Region']]['Revenue'].sum()
    new_list1.append(rev)

df['Revenue share '] = new_list
print(df.sort_values(by='Region'))

df['Revenue share of the Region'] = new_list
print(df.sort_values(by='Region'))



