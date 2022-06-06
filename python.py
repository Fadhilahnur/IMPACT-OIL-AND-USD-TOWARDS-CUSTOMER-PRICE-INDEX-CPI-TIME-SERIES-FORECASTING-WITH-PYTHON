#=========================================
#Title : This is my first Python Program
#Objective : To estimate least squares
#The simplest machine learning
#Author: Fadhilah Nur Binti Ismail
#Matric Number: A167808
#Date: 1 June 2020 (Monday)
#=========================================

import os #find the path directory
path = os.getcwd()
print(path)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_excel("python.xlsx",
                   sheet_name="data",
                   header=0,index_col=0)

print(df)

#%% Mean, variance and standard deviation

mean = np.mean(df)
var = np.var(df)
st_dev = np.std(df)

print(mean)
print(var)
print(st_dev)

#%% Median, minimum and maximum

median = np.median(df)
minimum = np.min(df)
maximum = np.max(df)
maximum1 = np.max(df['CPI'])

print(median)
print(minimum)
print(maximum)

#%% Plot data

i = np.log(df)

i1 = i.drop(columns=["II","CPI"])
i1.plot()
plt.title("MACRO")
plt.savefig('A167808.tiff')

#%% Least squares

import statsmodels.formula.api as statf

eq1 = statf.ols('GDP~PCON+GCON+IFT+EX+IM',
                data=i1).fit()
                    
print(eq1.summary())

#%% Export results into Latex format

from statsmodels.iolib.summary2 import summary_col
dfoutput = summary_col([eq1],
                       stars=True,
                       float_format = '%0.3f')

print(dfoutput)

dfoutput.as_latex()





