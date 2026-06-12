import pandas as pd

df = pd.read_csv("Dataset/Dataset .csv")

cuisines = df['Cuisines'].dropna().str.split(', ')
all_cuisines = cuisines.explode()

top3 = all_cuisines.value_counts().head(3)

percentage = (top3 / len(df)) * 100

print("Top 3 Cuisines:\n")
print(top3)

print("\nPercentage:\n")
print(percentage)