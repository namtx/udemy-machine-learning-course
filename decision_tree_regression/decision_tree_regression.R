# author: FRAMGIA\tran.xuan.nam

# Dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Fitting
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Visualizing
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), colour = 'blue') +
  ggtitle('Truth or Bluff') +
  xlab('Level') +
  ylab('Salary')