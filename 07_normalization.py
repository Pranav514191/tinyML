import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("../Datasets/dataset.csv")

features = ["Ax", "Ay", "Az", "Gx", "Gy", "Gz"]

# Check data types
print(df[features].dtypes)

# Find non-numeric values
for col in features:
    numeric = pd.to_numeric(df[col], errors="coerce")
    bad = numeric.isna()

    if bad.any():
        print(f"\nProblem in column: {col}")
        print(df.loc[bad, col])

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("../Datasets/dataset.csv")

# Select IMU features
features = ["Ax", "Ay", "Az", "Gx", "Gy", "Gz"]

# Normalize
scaler = MinMaxScaler()

df[features] = scaler.fit_transform(df[features])

# Display first five rows
print(df.head())