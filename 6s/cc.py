import math

def checkpr(x1,y1,x2,y2,x,y):
	r = ((x - x1) / (x2 - x1)) - ((y - y1) / (y2 - y1))
	# float сравнение с нулём
	if math.isclose(r,0.0,abs_tol=1e-9): return 0
	if r < 0.0: return -1
	if r > 0.0: return 1
	return None



def c1(x,y):
	x1 = 0.0; y1 = 0.0
	x2 = 0.0; y2 = 10.0
	if math.isclose(x1,x,abs_tol=1e-9): return 0
	if x < x1: return -1
	if x > x1: return 1
	return None


def c2(x,y):
	x1 = 0.0; y1 = 0.0
	x2 = 8.66025; y2 = 5.0
	return checkpr(x1,y1,x2,y2,x,y)


def c3(x,y):
	x1 = 0.0; y1 = 10.0
	x2 = 8.66025; y2 = 5.00
	return checkpr(x1,y1,x2,y2,x,y)

def cp(x,y):
	return (c1(x,y),c2(x,y),c3(x,y))
