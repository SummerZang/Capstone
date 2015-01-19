#1.

# Benefit and Cost Function

import math

def benefit(x):
    return math.log(x)

def cost(y):
    return 2*y
    
def profit(z):
    return benefit(z)-cost(z)

print(profit(5))


#2. 
# Benefit and Cost function
import matplotlib.pylab as pl


x=list(range(50,100))


def benefit(number):
    return 2*number+13

def cost(number):
    return -1*number+3
    
"""
set y is outcome from benefit
set z is outcome from cost
"""

y=list(map(benefit,list(x)))
z=list(map(cost,list(x)))
    

"To get profit"

p=list(set(y)-set(z))   

         
pl.ylim([-100,220])
pl.xlim([50,100])
pl.plot(x,y,'b')   
pl.plot(x,z,'r')  
pl.plot(x,p,'g')  
"""
Blue is for benefit
red is for cost
green is for profit
"""



