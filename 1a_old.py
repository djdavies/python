import random, math

# alpha: interarrival time
# beta: service time

def nextTime(alpha, beta):
        x = random.random() # random number between 0-1
        a = -alpha * (math.log(1 - x))
        b = -alpha * (math.log(1 - x))
    return a,b
    
                    
    
    
    
    
