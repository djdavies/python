def dayFromDate(d, m, y):

	"""
	>>> dayFromDate(15,10,2010)
	5
	>>> dayFromDate(1,1,2000)
	6
	>>> dayFromDate(31,12,2050)
	6
	>>> dayFromDate(1,1,10000)
	6
	>>> type(dayFromDate(15,10,2010))
	<type 'int'>
	"""
	m -= 2
	if m < 1:
		m += 12 
		y -= 1
	C = y % 100 # year of century
	D = y / 100 # century
	W = (13 * m - 1) / 5
	X = C / 4
	Y = D / 4
	Z = W + X + Y + d + C - 2 * D
	day = Z % 7
	#dayOfWeek = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
	#return "day ", (day), "which is a ", (dayOfWeek[(day)])
	return day 

	



