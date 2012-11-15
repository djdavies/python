#!/usr/bin/env python
# Part 1B, Daniel Jake Davies, C1120627

import math # for math.log
import random # random number 0-1

# define the function
def partB(alpha,beta):
    ta = 0 # next customer arrival
    ts = 0 # time until customer has finished
    c = 0 # current time
    q = 1 # current length of the queue
    m = 0 # maximum var
    
    while c <= 480: # time less than or equal to 8 hours
        if ta < ts:
            ts -= ta
            c = c+ta
            q += 1
            m = max([m,q])
            ta = (alpha*-1)*math.log(1-random.random())
            
            while q == 0:
                q += 1
                c = c + ta
                ta = (alpha*-1)*math.log(1-random.random())
                                
        else:
            ta = ta - ts
            c = c + ts
            q -= 1
            ts = (beta*-1)*math.log(1-random.random())
          
            while q == 0:
                q += 1
                c = c + ta
                ta = (alpha*-1)*math.log(1-random.random())
                
    return m
  
    

        
                    
        
