# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 12:04:07 2017

@author: ralall
"""

# Define the data
data = set()
count = int(input("Enter the number of data points: "))
for i in range(count):
    x=float(input("X"+str(i+1)+": "))
    y=float(input("Y"+str(i+1)+": "))
    data.add((x,y))
    print data
# Find the average x and y
avgx = 0.0
avgy = 0.0
for i in data:
    avgx += i[0]/len(data)
    avgy += i[1]/len(data)

# Find the sums
totalxx = 0
totalxy = 0

for i in data:
    totalxx += (i[0]-avgx)**2 #totalxy +=(i[0]-avgy)**2
    totalxy += (i[0]-avgx)*(i[1]-avgy)#totalxx +=(i[0]-avgy)*(i[1]-avgx)

# Slope/intercept form
m = totalxy/totalxx
b = avgy-m*avgx

print("Best fit line:")
print("y = "+str(m)+"x + "+str(b))

y = float(input("Enter a value to calculate: "))
print("x = "+str((y-b)/m))

