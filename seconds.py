def sec(h,m,s):
 # 1hr = 3600s
 # 1m = 60s
  print "There are", h + m/60. + s /36000., "hours"
  raw_input("\nPress enter to see how many seconds")
  return h*3600 + m*60 + s
  
