import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model_regression = LinearRegression()
model_regression.fit(X_train, y_train)


y_pred_regression = model_regression.predict(X_test)


mse = mean_squared_error(y_test, y_pred_regression)
print(f"Linear Regression Mean Squared Error: {mse:.2f}")


r2 = r2_score(y_test, y_pred_regression)
print(f"Linear Regression R-squared: {r2:.2f}")

print(f"Linear Regression Intercept: {model_regression.intercept_[0]:.2f}")
print(f"Linear Regression Coefficient: {model_regression.coef_[0][0]:.2f}")


plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred_regression, color='red', linewidth=2, label='Linear Regression Prediction')
plt.xlabel('Feature (X)')
plt.ylabel('Target (y)')
plt.title('Trained Linear Regression Model with Performance Evaluation')
plt.legend()
plt.grid(True)
plt.show()