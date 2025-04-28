import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


data = {
    'Feature1': [10, 15, np.nan, 20, 25, 30, np.nan, 35],
    'Feature2': [0.1, 0.2, 0.15, np.nan, 0.25, 0.3, 0.35, 0.4],
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'Value': [100, 200, 150, 180, np.nan, 300, 250, 400]
}
df = pd.DataFrame(data)

numerical_cols = df.select_dtypes(include=np.number).columns
imputer_mean = SimpleImputer(strategy='mean')
df[numerical_cols] = imputer_mean.fit_transform(df[numerical_cols])

categorical_cols = df.select_dtypes(include='object').columns
imputer_mode = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_mode.fit_transform(df[categorical_cols])


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Feature1', y='Feature2', hue='Category', data=df)
plt.title('Scatter Plot of Feature1 vs Feature2 (Colored by Category)')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
sns.countplot(x='Category', data=df, palette='viridis')
plt.title('Distribution of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()


if 'Value' in df.columns:
    X = df.drop('Value', axis=1)
    y = df['Value']
else:
    X = df
    y = None

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("\nTraining Features (X_train):")
print(X_train)
print("\nTesting Features (X_test):")
print(X_test)

if y is not None:
    print("\nTraining Target (y_train):")
    print(y_train)
    print("\nTesting Target (y_test):")
    print(y_test)