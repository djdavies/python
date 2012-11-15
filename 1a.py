#!/usr/bin/env python
# Part 1A, Daniel Jake Davies, C1120627

import math # for math.log
import random # random number 0-1

def nextTime(alpha): # define the function
    answer=(alpha*-1)*math.log(1-random.random()) # implement the equation
    return answer # return it back

