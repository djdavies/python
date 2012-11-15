# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import random

# The selection sort
def selection_sort(list):
    # Loop through the entire array
    for curPos in range( len(list) ):
        # Find the position that has the smallest number
        # Start with the current position
        minPos = curPos
        # Scan right
        for scanPos in range(curPos+1, len(list) ):
            # Is this position smallest?
            if list[scanPos] < list[minPos]:
                # It is, mark this position as the smallest
                minPos = scanPos
        
        # Swap the two values
        temp = list[minPos]
        list[minPos] = list[curPos]
        list[curPos] = temp

def insertion_sort(list):
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for keyPos in range(1, len(list)):
        # Get the value of the element to insert
        keyValue = list[keyPos]
        # Scan to the left
        scanPos = keyPos - 1
        # Loop each element, moving them up until
        # we reach the position the 
        while (scanPos >=0) and (list[scanPos] > keyValue):
            list[scanPos+1] = list[scanPos]
            scanPos = scanPos - 1
        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[scanPos+1] = keyValue

        
# This will point out a list
def print_list(list):
    for item in list:
        print( "%3d" % item,end="" )
    print()
    
# Create a list of random numbers
list = []
for i in range(10):
    list.append(random.randrange(100))

# Try out the sort
print_list(list)
insertion_sort(list)        
print_list(list)
