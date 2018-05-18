# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:17:28 2018

@author: ASUS
"""

x = 100

num_guess = 0
threshold = 0.001

low = 0
high = x

ans = (low+high)/2

error = abs(ans**2 - x)

while error > threshold:
    print('Low', low, 'High', high, 'Ans', ans)
    if (ans**2 < x):
        low = ans
    else:
        high = ans
    ans = (low+high)/2
    error = abs(ans**2 - x)
            
print(ans, error)