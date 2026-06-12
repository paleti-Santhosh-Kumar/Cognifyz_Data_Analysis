import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/Dataset .csv")

rating_count = df['Aggregate rating'].value_counts().sort_index()

print("Rating Distribution:")
print(rating_count)

avg_votes = df['Votes'].mean()

print("\nAverage Votes:")
print(round(avg_votes,2))

rated = df[df['Aggregate rating'] > 0]

most_common = rated['Aggregate rating'].value_counts().idxmax()

print("\nMost common rating (excluding 0):")
print(most_common)

plt.figure(figsize=(10,5))
plt.hist(df['Aggregate rating'], bins=10)

plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Restaurant Rating Distribution")

plt.savefig("restaurant_rating_distribution.png")

print("\nChart saved as restaurant_rating_distribution.png")