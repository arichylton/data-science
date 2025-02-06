import numpy as np
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import statsmodels.api as sm

data = pd.read_csv('./Simple_linear_regression.csv') 

y = data['GPA']
x1 = data['SAT']

plt.scatter(x1, y)
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()


