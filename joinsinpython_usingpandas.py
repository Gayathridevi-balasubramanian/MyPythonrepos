import pandas as pd

df1 = pd.DataFrame({
    'letters': ['a','b','c','d'],
    'numbers': [1,2,3,4]
})

df2 = pd.DataFrame({
    'letters' : ['c','d','e','f'],
    'numbers': [3,4,5,6]
})
print(df1 ,"\n", df2)
print("\n")
#left join using merge
print("left join")
print(df1.merge(df2, how='left', on='numbers'))


#inner join using merge
print("inner join")
print(df1.merge(df2, how='inner', left_on='numbers', right_on='numbers'))

#inner join using merge
print("inner join")
print(df1.merge(df2, how='inner', on='numbers'))

#right join using merge
print("right join")
print(df1.merge(df2, how='right', on='numbers', suffixes=('_x','_hello')))
# also try _mad in the suffixes in the place of _hello

# pd.concat to add two dataframes together
df3 = pd.concat([df1,df2], axis=1)
print(df3)

df3 = pd.concat([df1,df2], axis=0)
print(df3)

df3 = pd.concat([df1,df2], axis=0 ).reset_index(drop = True)
print(df3)


df3 = pd.concat([df1,df2], axis=0 ).reset_index(drop = False)
print(df3)


df3 = pd.concat([df1,df2], axis=0 ).drop_duplicates().reset_index(drop = True)
print(df3)


# new_row = pd.Series(['z',26], index=df1.columns )
# df4 = df1.append(new_row,ignore_index= True)
# print(df4)


df3 = pd.Series(['z',26], index=df3.columns )
print(df3)

#joining along the indexes
print(df2.join(df1, rsuffix='_rightsidetablecolumns'))