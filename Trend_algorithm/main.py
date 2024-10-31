import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example initial data
# X is the input (time step or feature), y is the output (target value)
X = np.array([[1], [2], [3], [4], [5]])  # time steps
y = np.array([2, 3, 5, 7, 11])  # corresponding values (e.g., trends like a stock price, etc.)

# Create the model
model = LinearRegression()

# Train the model on initial data
model.fit(X, y)

# Predict the next value
next_X = np.array([[6]])  # For example, time step 6
predicted_y = model.predict(next_X)
print(f"Predicted next value (step 6): {predicted_y[0]}")

# Suppose we now receive new data for step 6
# Simulate new data (in reality, this data would come from real observations)
new_data_X = np.array([[6]])
new_data_y = np.array([13])  # Let's assume the true value for step 6 is 13

# Feedback loop: Update the model with the new data
X = np.append(X, new_data_X).reshape(-1, 1)  # Add new input to training data
y = np.append(y, new_data_y)  # Add new output to training data

# Retrain the model with the new data
model.fit(X, y)

# Predict the next value (step 7) after retraining
next_X = np.array([[7]])
predicted_y = model.predict(next_X)
print(f"Predicted next value (step 7): {predicted_y[0]}")

# Measure how well the model is doing (optional)
mse = mean_squared_error(y, model.predict(X))
print(f"Mean Squared Error after feedback: {mse}")
