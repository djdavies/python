faFile = open("facup.txt","r")
teams = faFile.readlines() # read into a list
faFile.close() 

teams.sort() # sort them alphabetically

# enumeration prints them with numbers
for i, x in enumerate(teams): # has to be a list to enumerate
    print i, x
