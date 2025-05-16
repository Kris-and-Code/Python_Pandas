import csv
import random
import datetime

categories = ['Electronics', 'Clothing', 'Food', 'Books']
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Category', 'Product', 'Units', 'Price'])
    for _ in range(100):
        category = random.choice(categories)
        product = f"{category[:3]}_{random.randint(100,999)}"
        units = random.randint(1, 10)
        price = round(random.uniform(10, 100), 2)
        date = datetime.date.today() - datetime.timedelta(days=random.randint(0, 30))
        writer.writerow([date, category, product, units, price])
