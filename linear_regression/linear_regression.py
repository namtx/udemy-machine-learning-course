#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 10:03:15 2018

@author: FRAMGIA\tran.xuan.nam
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/4, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predictions

y_pred = regressor.predict(X_test)

# Visualizing 
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train))
plt.title('Salary vs Experience (Training Set)')
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.show()

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train))
plt.title('Salary vs Experience (Test Set)')
plt.ylabel('Salary')
plt.xlabel('Years of Experience')
plt.show()