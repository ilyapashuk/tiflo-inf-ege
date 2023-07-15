# номер первого задания в блоке 27416 (решу егэ)

def step(k):
	return (
		(k[0] + 1,k[1]),
		(k[0], k[1] + 1),
		(k[0] * 2,k[1]),
		(k[0], k[1] * 2)
	)

def check(k): return sum(k) >= 77

def g(k,n,sw,lim):
	if check(k): return not sw
	if n >= lim: return False
	r = [g(kk,n + 1,not sw,lim) for kk in step(k)]
	cmp = None
	if sw: cmp = any
	else: cmp = all
	return cmp(r)


def gg(k,n,sw,lim):
	if check(k): return not sw
	if n >= lim: return False
	r = [gg(kk,n + 1,not sw,lim) for kk in step(k)]
	cmp = any
	return cmp(r)