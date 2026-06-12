import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/Dataset .csv")

price_count = df['Price range'].value_counts().sort_index()

percentage = (price_count / len(df)) * 100

print("Price Range Distribution:")
print(price_count)

print("\nPercentage:")
print(percentage)

plt.figure(figsize=(8,5))
plt.bar(price_count.index, price_count.values)

plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution")

plt.savefig("price_range_distribution.png")

print("\nChart saved as: price_range_distribution.png")