#!/usr/bin/env python
result, dist, char_low = "", "", ""
chars = raw_input("Enter the string to convert: ")
for i in range(0, len(chars)):
	char_low = chars[i].lower() # reminder: need to check if string is.alpha()
	if char_low <= 'm':
		dist = 13
	else:
		dist = -13
	result += chr(ord(chars[i]) + dist)
print result
