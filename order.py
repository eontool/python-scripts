#order a, b and c starting from lowest
def order(a,b,c):

	if(a<b):
		if(a<c):
			if(b<c):
				return a, b, c
			return a, c, b
		return c, a, b
	else:
		if(b<c):
			if(a<c):
				return b, a, c
			return b, c, a
		return c, b, a
		
print order(9,3,6)




