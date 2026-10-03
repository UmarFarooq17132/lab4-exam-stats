import pandas as pd
import numpy as np
from scipy import stats

# Input data
scores = pd.Series([72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69])

# (a) Display descriptive statistics
print("--- Descriptive Statistics ---")
print(scores.describe())

# (b) Skewness and Kurtosis (after dropping missing values)
clean_scores = scores.dropna()
print("\nSkewness:", stats.skew(clean_scores))
print("Kurtosis:", stats.kurtosis(clean_scores))

# (c) Report count of missing values
missing_count = scores.isnull().sum()
print("\nMissing values:", missing_count)

# (d) Fill missing scores with column mean
mean_value = scores.mean()
filled_scores = scores.fillna(mean_value)

print("\nFilled scores:")
print(filled_scores)