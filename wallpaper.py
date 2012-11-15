#!/usr/bin/env python
# Wallpaper algorithm
import sys, random, time
rand = random.randrange(0,999)
# Main function
def wallpaper(corna, cornb, side):
   for i in range(150): # side of wall, 30
      for j in range(150):
         x = corna + i * side / 100.0
         y = cornb + j * side / 100.0
         c = int(x*x + y*y)
         if c % 2 == 0:
#            sys.stdout.write(u"\u7675")
            sys.stdout.write(u"\u2588")
         else:
            sys.stdout.write(" ")
      sys.stdout.write("\n")

while True:
#wallpaper(0,0,100) # default setting
	rand = random.randrange(0,999)
	wallpaper((rand),(rand),(rand))
