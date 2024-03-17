import pandas as pd

emissions = pd.DataFrame({"Country": ['China','United States','India'],
                         "Year": ['2018','2018','2018'],
                         "Co2 emi": [10060000000.0,541000000000.0,265000000000.0]
                          })

print(emissions)
# set_option is not working because of improper python installation
pd.set_option('display.max_rows',2)
print(emissions)

pd.set_option('display.max_columns',2)
print(emissions)
pd.options.display.float_format = '{:,.2f}'.format
print(emissions)

