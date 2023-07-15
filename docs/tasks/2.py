# Copyright (2023) ilyapashuk<ilusha.paschuk@gmail.com>

import itertools

# выражение из задания, переписанное на python

def f(w,x,y,z): return not (y <= x) or (z <= w) or not z

# составим таблицу истинности данного выражения, не задавая пока конкретный порядок столбцов
table = []

# здесь можно было бы использовать 4 вложенных цикла for

for w,x,y,z in itertools.product((True,False),repeat=4):
	v = {'w':w,'x':x,'y':y,'z':z,'v':f(w,x,y,z)}
	table.append(v)


# вводим предоставленный фрагмент
# Внимание! иногда для корректной работы решения бывает необходимо располагать строки не в том порядке, в котором они даны изначально. Если решение не отрабатывает с первого раза, следует пробовать разные варианты размещения строк.
ztable = [
	(None,False,None,None,False),
	(False,True,None,None,False),
	(True,None,None,False,False)
]

# вспомогательная функция, сравнивающая строки таблиц
def lcomp(i,ii):
	for q,r in zip(i,ii):
		if q == None: continue
		if q != r: return False
	return True

# перебираем все возможные варианты расстановки букв
for l in itertools.permutations('wxyz'):
	# формируем таблицу истинности выражения с учётом проверяемого на данной итерации порядка букв
	ltable = []
	for i in table:
		vv = [i[k] for k in l]
		vv.append(i['v'])
		ltable.append(vv)
	res = 0
	# проходим по каждой из строк данного фрагмента, чтобы найти соответствующую строку полной таблицы истинности
	for i in ztable:
		r = False
		for ii in ltable.copy():
			if lcomp(i,ii):
				r = True
				# следующая строка необходима, так как в условии задачи указано, что дан фрагмент из различных строк таблицы истинности, то есть одна и таже строка полной таблицы не может соответствовать нескольким строкам данного фрагмента.
				ltable.remove(ii)
		if r: res += 1
	if res >= len(ztable): print(l)