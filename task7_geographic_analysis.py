import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/Dataset .csv")

plt.figure(figsize=(10,6))

plt.scatter(
    df['Longitude'],
    df['Latitude'],
    alpha=0.5
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Geographic Distribution")

plt.savefig("geographic_distribution.png")

print("Chart saved as geographic_distribution.png")