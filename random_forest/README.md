#### Step 1

Pick a random K data points from the Training set.
#### Step 2

Build the decision tree associated the these K data points.
#### Step 3

Choose the number Ntree of trees you want to build and repeat STEP 1 & 2
#### Step 4

For a new data point, make each one of your Ntree trees predict the value of Y
to for the the data point in question, and assign the new data point the average
across all of the predicted Y values.

