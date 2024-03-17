import pandas as pd

print("To generate a series of dates")

daterange = pd.period_range('1/1/2024',freq='30d', periods = 4)
print(daterange)

print("##########################")
print(daterange.array)


print("##########################")
# to generate the dateframe
date_df = pd.DataFrame(data= daterange, columns=['sample date'])
#date_df = pd.DataFrame(daterange )
print(date_df)

print("##########################")
# this is similar to the lag function
date_df['date_difference'] = date_df['sample date'].diff(periods= 1)
print(date_df)

print("##########################")
# this is to find the first day of the month
date_df['first of month'] = date_df['sample date'].values.astype('datetime64[M]')
# [M] - represents the month
print(date_df)

print("##########################")
print(date_df.dtypes)
print(".dt functions")
date_df['date conversion'] = date_df['sample date'].dt.to_timestamp()
print(date_df.dtypes)
print(date_df)

print("##########################")
#print({date_df['sample date'] - date_df['first of month'] })
print(date_df['first of month'] - date_df['date conversion'] )

print("##########################")
diff = date_df['first of month'] - pd.Timedelta('15d')
print(diff)
print("##########################")
print(date_df['first of month'].dt.day_name())
print("##########################")
print(date_df['first of month'].dt.dayofweek)
print("##########################")
print(date_df['first of month'].dt.days_in_month)