# импорт кода из o.py
from o import *

for s in range(1,129):
	# Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
	if g(s,0,False,2) and not gg(s,0,True,1):
		print(s)
		break