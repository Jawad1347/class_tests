# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:19:25 2021

@author: CR2-4
"""

url = "https://raw.githubusercontent.com/amankharwal/US-presidents-heights/master/president_heights.csv"
import pandas as pd
df = pd.read_csv(url)

df.isna().sum()
# =============================================================================
# order         0
# name          0
# height(cm)    0
# dtype: int64
# =============================================================================

df.describe()
# =============================================================================
#         order       height(cm)
# count  42.000000   42.000000
# mean   22.476190  179.738095
# std    13.152461    7.015869
# min     1.000000  163.000000
# 25%    11.250000  174.250000
# 50%    22.000000  182.000000
# 75%    33.750000  183.000000
# max    44.000000  193.000000
# =============================================================================
import numpy as np
print("25th percentile =", np.percentile(df.iloc[:,-1], 25)) # 174.25
print("Median =", np.median(df.iloc[:,-1])) # 182.0
# =============================================================================
# 25th percentile = 174.25
# Median = 182.0
# 75th percentile = 183.0
# =============================================================================
print("75th percentile =", np.percentile(df.iloc[:,-1], 75)) # 183.0

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(df.iloc[:,-1])
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()
