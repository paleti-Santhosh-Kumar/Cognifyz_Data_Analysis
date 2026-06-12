import pandas as pd

df = pd.read_csv("Dataset/Dataset .csv")

chains = df['Restaurant Name'].value_counts()

restaurant_chains = chains[chains > 1]

print("Top Restaurant Chains:\n")
print(restaurant_chains.head(10))

chain_rating = df.groupby('Restaurant Name')['Aggregate rating'].mean()

print("\nTop Rated Restaurant Chains:\n")

print(
    chain_rating[restaurant_chains.index]
    .sort_values(ascending=False)
    .head(10)
)