# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:19:42 2017

@author: ralall
"""
import matplotlib.pyplot as plt
from sklearn import linear_model




def line(d):
    plt.scatter(d["days"],d["energy"],color='black')
    plt.xlabel("days")
    plt.ylabel("energy")
    reg=linear_model.LinearRegression()
    reg.fit(d["days"],d["energy"])
    m=reg.coef_[0]
    b=reg.intercept_
    print("slope=",m, "intercept=",b)
    plt.scatter(d["days"],d["energy"],color='black')
    predicted_values = [reg.coef_ * i + reg.intercept_ for i in d["days"]]
    plt.plot(d["days"], predicted_values, 'b')
    plt.xlabel("days")
    plt.ylabel("energy")