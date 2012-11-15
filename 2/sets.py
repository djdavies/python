#!/usr/bin/env python
A = set([1,2,3,4])
B = set([3,4,5,6])
print "Set A:", A, "Set B:", B
print "\nUnion of set A and B:", A | B
print "Intersection:", A & B
print "Their difference:", A - B
x, y = A - B, B - A
print "Union of (A-B) (B-A):", x | y
print "Interaction of A&A:", A & A
