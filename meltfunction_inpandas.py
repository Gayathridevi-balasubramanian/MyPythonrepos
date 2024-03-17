import pandas as pd

# Create a sample DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'math_score': [90, 85, 95],
    'english_score': [80, 88, 92],
    'history_score': [75, 89, 78]
}
# melt converts the columns as the one columns
# and values as the another columns
df = pd.DataFrame(data)

# Original DataFrame
print("Original DataFrame:")
print(df)

# Melt the DataFrame, keeping 'id' and 'name' as identifier variables
melted_df = pd.melt(df, id_vars=['id', 'name'], var_name='subject', value_name='score')

# Display the melted DataFrame
print("\nMelted DataFrame:")
print(melted_df)
