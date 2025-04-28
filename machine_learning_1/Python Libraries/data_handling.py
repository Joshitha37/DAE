import pandas as pd
import numpy as np


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [60000, 75000, 55000, 80000, np.nan],
    'Experience': [3, 5, 1, 4, 7]
}


df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


print("\nDataFrame Info:")
print(df.info())


print("\nDescriptive Statistics:")
print(df.describe())


print("\nFirst 3 rows:")
print(df.head(3))


print("\nLast 2 rows:")
print(df.tail(2))


print("\nCity column:")
print(df['City'])


print("\nName and Age columns:")
print(df[['Name', 'Age']])


mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print("\nDataFrame after handling missing Salary:")
print(df)


df['Salary_USD'] = df['Salary'] * 1.10  
print("\nDataFrame with Salary in USD:")
print(df)


def categorize_experience(exp):
    if exp < 3:
        return 'Junior'
    elif exp < 6:
        return 'Mid-Level'
    else:
        return 'Senior'

df['Experience_Level'] = df['Experience'].apply(categorize_experience)
print("\nDataFrame with Experience Level:")
print(df)


experienced_employees = df[df['Experience'] > 3]
print("\nExperienced Employees (Experience > 3):")
print(experienced_employees)


sorted_by_age = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:")
print(sorted_by_age)


average_salary_by_city = df.groupby('City')['Salary_USD'].mean()
print("\nAverage Salary by City (USD):")
print(average_salary_by_city)