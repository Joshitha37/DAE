import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some synthetic data for regression
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model_supervised = LinearRegression()
model_supervised.fit(X_train, y_train)

# Make predictions on the test set
y_pred_supervised = model_supervised.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred_supervised)
print(f"Supervised Learning (Linear Regression) Mean Squared Error: {mse:.2f}")
print(f"Supervised Learning (Linear Regression) Intercept: {model_supervised.intercept_[0]:.2f}")
print(f"Supervised Learning (Linear Regression) Coefficient: {model_supervised.coef_[0][0]:.2f}")

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred_supervised, color='red', linewidth=2, label='Linear Regression Prediction')
plt.xlabel('Feature (X)')
plt.ylabel('Target (y)')
plt.title('Supervised Learning: Linear Regression')
plt.legend()
plt.grid(True)
plt.show()