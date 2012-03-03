#!/usr/bin/env python
import turtle as trtl
from time import sleep

# Draws a star
def fractal(length = 100):
    if length < 10:
        return
    trtl.fd(length)
    fractal(length*0.3)
    trtl.left(144)
    trtl.fd(length)
    fractal(length*0.3)
    trtl.left(144)
    trtl.fd(length)
    fractal(length*0.3)
    trtl.left(144)
    trtl.fd(length)
    fractal(length*0.3)
    trtl.left(144)
    trtl.fd(length)
    fractal(length*0.3)
    trtl.left(144)
    return

fractal(200)
sleep(15)
