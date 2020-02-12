from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import random
style.use('fivethirtyeight')
'''
xs=np.array([1,2,3,4,5,6],dtype=np.float64);
ys=np.array([5,4,6,5,6,7],dtype=np.float64);
'''
def create_dataset(hm,variance,step=2,correlation=False):
   val=1
   ys=[]
   for i in range(hm):
       
       y=val+random.randrange(-variance,variance);
       ys.append(y)
       if correlation and correlation=='pos':
           val+=step;
       elif correlation and correlation=='neg':
           val-=step;
       
   xs = [i for i in range(len(ys))]
   return np.array(xs,dtype=np.float64), np.array(ys,dtype=np.float64)
def best_fit_slope(xs,ys):
  m= (((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)*mean(xs))-mean(xs**2)))
  return m
def intercept(xs,ys):
    b= (mean(ys)-(m)*(mean(xs)));
    return b;
def squared_error(y,y_line):
     return (sum((y_line-y)**2))
 
def coefficient_of_determination(yo,y_line):
     y_meanline=[mean(yo) for y in yo];
     sqred_err_regr=squared_error(yo,y_line);
     sqred_err_mean=squared_error(y_meanline,yo);
     return( 1- (sqred_err_regr/sqred_err_mean))

xs,ys=create_dataset(6,3)
m= best_fit_slope(xs,ys)
b=intercept(xs,ys);
line=[];
for x in xs:
     line.append((m*x)+b)
plt.scatter(xs,ys);
plt.plot(xs,line)
r=coefficient_of_determination(ys,line)
print(m,b,r)