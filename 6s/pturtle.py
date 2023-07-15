from math import sin,cos,radians


head = 0.0

def rhead(): return 90.0 - head

def chead():
	global head
	if head >= 360.0: head -= 360.0


def right(d):
	global head
	head += float(d)
	chead()


x = 0.0; y = 0.0

def forward(n):
	global x,y
	y += n * sin(radians(rhead()))
	x += n * cos(radians(rhead()))

def backward(n):
	global x,y
	y -= n * sin(radians(rhead()))
	x -= n * cos(radians(rhead()))


def position(): return (x,y)


def heading(): return head


def goto(xx,yy):
	global x,y
	x = xx
	y = yy