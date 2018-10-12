from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Create inputs
x_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 6, 8, 10]

# Create Linear Regression Model
regr = linear_model.LinearRegression()

# Model Training
regr.fit(x_train, y_train)

# Model Testing
x_test = [[1], [5]]
y_test = regr.predict(x_test)

# Print Results of Model
print("Based on your inputs ", end='')
print(x_test, end='')
print(", the model predicts: ", end='')
print(y_test)

# Print Model (Equation)
print("Your model is in the form y = {:.3}x + {:.3}".format(regr.coef_[0], regr.intercept_))