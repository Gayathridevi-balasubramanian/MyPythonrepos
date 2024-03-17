import pandas as pd

Data = pd.read_csv('AB_NYC_2019.CSV')
print(Data.dtypes)

print(Data['host_name'])

# to select only certain values to manipulate
stadate = Data[['host_name','neighbourhood_group','last_review','number_of_reviews','reviews_per_month']].head(10)
print(stadate)

# stack function to create a new datatype
stdata = stadate.set_index(['host_name','neighbourhood_group','last_review'])
stacked = pd.DataFrame(stdata.stack())
print("Stacked Data")
print(stacked)


# unstacking to the required level
print(stacked.unstack('neighbourhood_group'))

# to reverse this we need to use the unstack function 
print( stacked.unstack())
