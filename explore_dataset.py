
import pandas as pd

# 1. Load the dataset
data = pd.read_csv("student-mat.csv", sep=";")

# 2. Display the first five records
print("First five records:")
print(data.head())

# 3. Show dataset size
print("\nDataset shape:")
print(data.shape)

# 4. Show column names
print("\nColumn names:")
print(data.columns)

# 5. Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# 6. Display basic statistics
print("\nBasic statistics:")
print(data.describe())

# 7. Average final grade by weekly study time
print("\nAverage final grade by study time:")
print(data.groupby("studytime")["G3"].mean().round(2))

# 8. Average final grade by past failures
print("\nAverage final grade by past failures:")
print(data.groupby("failures")["G3"].mean().round(2))

# 9. Display the top 10 students by final grade
print("\nTop 10 students by final grade:")
print(
    data.sort_values("G3", ascending=False)[
        ["studytime", "failures", "absences", "G1", "G2", "G3"]
    ].head(10)
)

# 10. Show the distribution of final grades
print("\nFinal grade distribution:")
grade_distribution = pd.cut(
    data["G3"],
    bins=[-1, 5, 10, 15, 20],
    labels=["0–5", "6–10", "11–15", "16–20"]
)

print(grade_distribution.value_counts().sort_index())

# 11. Check correlation between grades
print("\nCorrelation between G1, G2, and G3:")
print(data[["G1", "G2", "G3"]].corr().round(2))