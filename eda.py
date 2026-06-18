import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_200_records.csv")

# Basic Information
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Rating Distribution
print("\nRating Counts:")
print(df["Rating"].value_counts())

# Clean Price Column
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
)

# Convert to float
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nPrice Statistics:")
print(df["Price"].describe())

# Top 10 Expensive Books
top_books = df.sort_values(by="Price", ascending=False).head(10)

print("\nTop 10 Expensive Books:")
print(top_books[["Title", "Price"]])

# Graph 1 - Rating Distribution
plt.figure(figsize=(8, 5))
df["Rating"].value_counts().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Graph 2 - Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"].dropna(), bins=10)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()