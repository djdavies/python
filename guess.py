#!/usr/bin/env python

bottom = 3
top = 15
guess = int(round((bottom + top) / 2))
interval = int(round((bottom + top) / 4))
guessed = False
guesses = 0
guesslist = []

print "Think of a number between ", bottom, "and ", top, ". The computer will guess it."

while not guessed:
    if guess in guesslist:
        print "\n\nI've guessed this already, are you sure?"
        continue
    guesslist.append(guess)
    print "\nMy guess is ", guess, "\n\t\tHigher, lower or bang on?"
    if guess > top or guess < bottom:
        print "\t\t\tHave you been cheating? :P"
    response = str(raw_input('higher, lower, bang: '))
    if response == "bang":
        guessed = True
    elif response == "higher":
        print "\t\tDamn."
        guess += interval
    elif response == "lower":
        print "\t\tGah."
        guess -= interval
        
    if interval <= 5 and interval > 1:
        interval -= 1
    elif interval > 5:
        interval = int(round(interval * 0.5))	
    guesses += 1

print "\n\nWooo, I got it in ", guesses
