# Polynomial Regression

dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Linear Regression
linear_regressor = lm(formula = Salary ~ .,
                      data = dataset)

# Polynomial Regression
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
dataset$Level5 = dataset$Level^5
dataset$Level6 = dataset$Level^6
poly_regressor = lm(formula = Salary ~ .,
                    data = dataset)

# Visualizing
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(linear_regressor, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth or Bluff (Linear Regression)') +
  xlab('Level') +
  ylab('Salary')

# Visualizing Polynomial Regression
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_regressor, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth or Bluff (Polynomial Regression)') +
  xlab('Level') +
  ylab('Salary')

# Predicting new value with Linear Regression
y_pred = predict(linear_regressor, data.frame(Level = 6.5))

# Predicting new value with Polynomial Regression
y_pred = predict(poly_regressor, data.frame(Level = 6.5,
                                            Level2 = 6.5^2,
                                            Level3 = 6.5^3,
                                            Level4 = 6.5^4,
                                            Level5 = 6.5^5,
                                            Level6 = 6.5^6))