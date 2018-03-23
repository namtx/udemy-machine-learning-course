#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:17:38 2018

@author: FRAMGIA\tran.xuan.nam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# taking care of missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])