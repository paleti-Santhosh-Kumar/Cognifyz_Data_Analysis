import pandas as pd

df = pd.read_csv("Dataset/Dataset .csv")

online_count = df['Has Online delivery'].value_counts()
percentage = (online_count / len(df)) * 100

print("Online Delivery Percentage:\n")
print(percentage.round(2))

avg_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\nAverage Ratings:\n")
print(avg_rating.round(2))