import pandas as pd

def meltTable(report: pd.DataFrame):
    df_melted = pd.melt(report,id_vars=['product'],var_name='quarter',value_name='sales')
    # Sort the DataFrame by product and quarter
    df_output = df_melted.sort_values(by=['product', 'quarter']).reset_index(drop=True)

    # Display the result
    print(df_output)
    return df_melted
    
data = {'product': ['Umbrella', 'SleepingBag'],
        'quarter_1': [417, 800],
        'quarter_2': [224, 936],
        'quarter_3': [379, 93],
        'quarter_4': [611, 875]}

df = pd.DataFrame(data)
meltTable(df)