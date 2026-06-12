import pandas as pd

df = pd.read_csv("Dataset/Dataset .csv")

city_count = df['City'].value_counts()

avg_rating = df.groupby('City')['Aggregate rating'].mean()

highest_rating_city = avg_rating.idxmax()
highest_rating = avg_rating.max()

print("City with highest restaurants:")
print(city_count.head(1))

print("\nCity with highest average rating:")
print(highest_rating_city, ":", highest_rating)