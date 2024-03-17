import pandas as pd

temps = pd.DataFrame({
    "sequence":[1,2,3,4,5],
    "measurement_type" : ['actual','actual','actual',None,'estimated'],
    "temperature_f":[67.24,84.56,91.61, None, 49.64]
})

print(temps)

print("to identity the null data : use isna() function")
print(temps.isna())


print("Handling the missing values: ")
print("cumulative sum in the dataframe: ",temps['temperature_f'].cumsum())
print("Handling the missing values using skipna, it nulls all the values after encountering the first null: ")
print("cumulative sum in the dataframe: ",temps['temperature_f'].cumsum(skipna=False))


print("groupby function handling null values with the parameter dropna=False ")
print(temps.groupby(by="measurement_type",dropna=False))
print("\n dropna add the null data also in the calculation")
print(temps.groupby(by="measurement_type",dropna=False).max())
print(temps.groupby(by="measurement_type" ).max())

print("To  drop columns and rows with the null values")
print(temps.dropna())
print(temps.dropna(axis=0))
print(temps.dropna(axis=1))


print("\nFilling the null values using fillna(0)")
print(temps.fillna(0))

print("\n using fillna using the pad method")
print(temps.fillna(method="pad"))

print("\n Using the Interpolate() to fill in with striaght line estimation of the values")
print(temps.interpolate())
#print(temps.interpolate(method=match))
