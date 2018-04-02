import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# X_train, y_train, X_test, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2018)

# linear regression
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

# polynomial regression
from sklearn.preprocessing import PolynomialFeatures
polynomial_regressor = PolynomialFeatures(degree = 7)
X_poly = polynomial_regressor.fit_transform(X)
linear_regressor_2 = LinearRegression()
linear_regressor_2.fit(X_poly, y)

# Visualizing
plt.scatter(X, y, color = 'red')
plt.plot(X, linear_regressor.predict(X))
plt.plot(X, linear_regressor_2.predict(X_poly))
plt.show()
