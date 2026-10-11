
import pandas as pd

# Load the dataset
data = pd.read_csv("student-mat.csv", sep=";")

# Display the first five records
print(data.head())

# Show dataset size
print("Dataset shape:", data.shape)

# Show column names
print(data.columns)

# Check missing values
print(data.isnull().sum())

# Display basic statistics
print(data.describe())

# Average final grade by weekly study time
print("\nAverage final grade by study time:")

print(
    data.groupby("studytime")["G3"].mean().round(2)
)

# Average final grade by number of past failures
print("\nAverage final grade by past failures:")

print(
    data.groupby("failures")["G3"].mean().round(2)
)

# Show the students with the highest final grades
print("\nTop 10 final grades:")

print(
    data.nlargest(10, "G3")[["studytime", "failures", "absences", "G3"]]
)
