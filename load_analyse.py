import pandas as pd

df = pd.read_csv('sales_data.csv')
df['Total'] = df['Units'] * df['Price']

# Show total sales by category
category_sales = df.groupby('Category')['Total'].sum().sort_values(ascending=False)
print(category_sales)

# Top-selling product
top_product = df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(1)
print(top_product)
