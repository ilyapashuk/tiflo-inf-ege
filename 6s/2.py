﻿from winsound import MessageBeep as beep
from turtle import *

# увеличиваем размер окна
screensize(800,600)
# эта строка задаст параметры, как у канонического исполнителя "Черепаха"
mode('logo')


# поумолчанию тут всё измеряется в пикселях, поэтому нужно для нормального масштаба умножать все длины на какое-то число.
# изменением этой цифры можно менять масштаб чертежа.
mult = 30


# опустить хвост
down()



# сам алгоритм из задания
for n in range(0,7):
	ps = position()
	pss = (ps[0] / mult, ps[1] / mult)
	print('(%.5f, %.5f)' % pss)
	forward(10 * mult)
	right(120)



beep()


# бесконечная блокировка, чтобы окно сразу не закрылось
done()