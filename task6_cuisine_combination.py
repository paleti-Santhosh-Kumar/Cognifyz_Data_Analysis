import pandas as pd

df = pd.read_csv("Dataset/Dataset .csv")

cuisine_combo = df['Cuisines'].dropna()

top_combo = cuisine_combo.value_counts().head(10)

print("Top Cuisine Combinations:\n")
print(top_combo)

rating_combo = df.groupby('Cuisines')['Aggregate rating'].mean()

print("\nTop Rated Cuisine Combinations:\n")
print(rating_combo.sort_values(ascending=False).head(10))