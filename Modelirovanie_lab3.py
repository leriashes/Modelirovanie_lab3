#вывод ошибки при неверном формате файла
def WrongFormat():
	print("Неверный формат файла")
	exit()

#печать подстрочной цифры
def PrintNumb(i):
	n = ['₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
	print(n[i], end='')

#печать функции
def PrintFunction(c1, c2, m):
	print(c1, "x₁", sep='', end='')
	if (c2 >= 0):
		print(" + ", sep='', end='')
	else:
		print(" - ", sep='', end='')
	print(abs(c2), "x₂ → ", sep='', end='')
	if (m == 0):
		print("min")
	else:
		print("max")

#печать заголовка таблицы
def PrintHeader(num, oc):
	for i in range(19 + 9 * (num + 2)):
		print("-", end='')

	if (oc):
		for i in range(17):
			print("-", end='')

	print("\n Базис | Св. член |", end='')
	for i in range(round((9 * (num + 2) - 10) / 2)):
		print(" ", end='')
	k = round((9 * (num + 2) - 10) / 2)
	k = (9 * (num + 2) - 10) - round((9 * (num + 2) - 10) / 2)
	print("Переменные", end='')
	for i in range((9 * (num + 2) - 11) - round((9 * (num + 2) - 10) / 2)):
		print(" ", end='')

	if (oc):
		print("| Оцен. отношение\n", end='')
	else:
		print("|")

	print("       |          |", end='')
	for i in range(9 * (num + 2) - 1):
		print("-", end='')
	print("|                \n", end='')

#печать переменных
def PrintPerem(bazis, y):
	print("       |          |", end='')
	for i in range(len(bazis) + 2):
		print("   x", end='')
		PrintNumb(i)
		print("   |", end='')

	for i in range(len(y)):
		print("   y", end='')
		PrintNumb(y[i][0])
		print("   |", end='')

#печать строки таблицы
def PrintRow(letter, numb, svc, perem, oc, ocen):
	print()
	for i in range(19 + 9 * len(perem)):
		print("-", end='')

	if (oc):
		for i in range(17):
			print("-", end='')

	print()

	print("  ", letter, sep='', end='')
	PrintNumb(numb)
	print("   |{: ^10}|".format(round(svc, 2)), end='')

	for p in perem:
		print("{: ^8}|".format(round(p, 2)), end='')

	if oc:
		if (ocen[0] == True):
			ocenka = "∞"
		else:
			ocenka = round(ocen[1], 2)

		print("{: ^16}".format(ocenka), end='')

#печать строки таблицы
def PrintFRow(fsv, fcoef, oc):
	print()
	for i in range(19 + 9 * len(fcoef)):
		print("-", end='')

	if (oc):
		for i in range(17):
			print("-", end='')
	
	print("\n  F    |{: ^10}|".format(round(fsv, 2)), end='')

	for coef in fcoef:
		print("{: ^8}|".format(round(coef, 2)), end='')

	if (oc):
		print("      max")
	else:
		print()
	
#печать таблицы для решения М-методом
def PrintTableM(bazis, svc, perem, y, yrow, fcoef, fsv, mcoef, msv, ocen, row, col):
	PrintHeader(len(bazis) + len(y), round(msv))
	PrintPerem(bazis, y)
	
	for i in range(len(yrow)):
		PrintRow('y', y[i][0], svc[yrow[i][1]], perem[yrow[i][1]], round(msv), ocen[i])
		
		if i == row:
			print(" ← ", end='')


	for i in range(len(bazis)):
		pr = True
		for j in range(len(yrow)):
			if i == y[j][1]:
				pr = False

		if pr:
			PrintRow('x', bazis[i], svc[i], perem[i], round(msv), ocen[i])

			if i == row and round(msv):
				print(" ← ", end='')

	PrintFRow(fsv, fcoef, round(msv))

	for i in range(19 + 9 * len(fcoef)):
		print("-", end='')

	if (round(msv)):
		for i in range(17):
			print("-", end='')

	if (round(msv, 2) != 0):
		print("\n  -Mф  |{: ^10}|".format(str(round(msv, 2)) + "M"), end='')
	else:
		print("\n  -Mф  |{: ^10}|".format(abs(round(msv, 2))), end='')

	for coef in mcoef:
		if (round(coef, 2) != 0):
			print("{: ^8}|".format(str(round(coef, 2)) + "M"), end='')
		else:
			print("{: ^8}|".format(abs(round(coef, 2))), end='')

	if (round(msv)):
		print("      max")
	if (col > -1):
		for i in range(col * 9 + 22):
			print(" ", end='')
		print("↑")
	print("\n\n")
	
#печать таблицы для решения табличным методом
def PrintTable(bazis, svc, perem, fcoef, fsv, ocen, row, col):
	PrintHeader(len(bazis), min(fcoef) < 0)
	PrintPerem(bazis, [])

	for i in range(len(bazis)):
		pr = True
		for j in range(len(yrow)):
			if i == y[j][1]:
				pr = False

		if pr:
			PrintRow('x', bazis[i], svc[i], perem[i], min(fcoef) < 0, ocen[i])

			if i == row and min(fcoef) < 0:
				print(" ← ", end='')

	PrintFRow(fsv, fcoef, min(fcoef) < 0)
  
	if (col > -1):
		for i in range(col * 9 + 22):
			print(" ", end='')
		print("↑")
	print("\n\n")

def Mcount(mcoef, msvc):
	mcoef = []
	for i in range(num + 2):
		s = 0
		for j in range(len(yrow)):
			s += perem[yrow[j][1]][i]
		mcoef.append(s * -1)

	msvc = 0
	for i in range(len(y)):
		mcoef.append(0.0)
		msvc -= svc[y[i][1]]

	return (mcoef, msvc)

f = open('input.txt')
k = 0
m = 0

c = [0, 0] #коэффициенты для x1 и x2
a = []
b = []
num = 0

#чтение файла
for line in f:
	if k == 0:
		if (line == 'min\n'):
			m = 0
			print("Поиск минимума")
		elif (line == 'max\n'):
			m = 1
			print("Поиск максимума")
		else:
			WrongFormat()
	elif k == 1:
		c[0] = float(line)
	elif k == 2:
		c[1] = float(line)
	elif k == 3:
		num = int(line)
	elif k < num + 4:
		s = line.split()
		a.append([])
		for numb in s:
			a[k - 4].append(float(numb))
	elif k < num * 2 + 4:
		b.append(float(line))
	else:
		break

	k += 1

if k == 0:
	print("Файл пуст")
	exit()

#вывод функции
if m == 0:
	print("Z = ", end='')
	PrintFunction(c[0], c[1], m)
	print("F = -Z = ", end='')
	c = [coef * -1 for coef in c]
	PrintFunction(c[0], c[1], m + 1)
else:
	print("F = ", end='')
	PrintFunction(c[0], c[1], m)
print()

y = []

k = 0
for i in range(num):
	if b[i] * a[i][2] < 0:
		y.append([k, i])
		k += 1

yrow = y.copy()

bazis = [i + 2 for i in range(num)]
svc = [b[i] for i in range(num)]
perem = [[] for i in range(num)]
fcoef = [c[0] * -1, c[1] * -1] + [0.0 for i in range(num + len(y))]

for i in range(num):
	for j in range(num + 2):
		if j < 2:
			perem[i].append(a[i][j])
		elif j == i + 2:
			perem[i].append(a[i][2]) 
		else:
			perem[i].append(0.0)

for i in range(num):
	if svc[i] < 0:
		for j in range(num + 2):
			perem[i][j] = - perem[i][j];
		svc[i] = - svc[i];

fsvc = 0
ocen = [[False, 0.0] for i in range(len(bazis))]
row = -1
col = -1

if len(y) > 0:

	for i in range(len(yrow)):
		perem[y[i][1]] += [.0 for j in range(i)] + [-1.0 if svc[y[i][1]] < 0 else 1.0] + [.0 for j in range(len(y) - i - 1)]

	for i in range(len(bazis)):
		pr = True
		for j in range(len(yrow)):
			if i == yrow[j][1]:
				pr = False

		if pr:
			perem[i] += [0.0 for j in range(len(y))]


	mcoef = []
	msvc = 0
	(mcoef, msvc) = Mcount(mcoef, msvc)

	minM = min(mcoef)
	ind = mcoef.index(minM)

	ocen = []
	mo = -1
	
	for i in range(num):
		if perem[i][ind] == 0 or perem[i][ind] * svc[i] < 0 or perem[i][ind] < 0 and svc[i] == 0:
			ocen.append([True])
		else:
			ocen.append([False])
			ocen[i].append(svc[i] / perem[i][ind])
			mo = ocen[i][1]

	row = -1
	for i in range(num):
		if ocen[i][0] == False and ocen[i][1] < mo:
			mo = ocen[i][1]
			row = i

	mc = min(mcoef)
	col = -1
	if (mc != 0):
		col = mcoef.index(mc)

	PrintTableM(bazis, svc, perem, y, yrow, fcoef, fsvc, mcoef, msvc, ocen, row, col)

	while mc != 0:

		bazis.pop(row)
		bazis.insert(row, col)

		oldp = []
		for i in range(len(perem)):
			oldp.append(perem[i].copy())

		oldf = fcoef.copy()
		oldm = mcoef.copy()

		for i in range(len(yrow)):
			if yrow[i][1] == row:
				yrow.pop(i)
				break

		for i in range(len(bazis)):
			for j in range(len(bazis) + len(y) + 2):
				if (i != row):
					perem[i][j] = oldp[i][j] - (oldp[row][j] * oldp[i][col]) / oldp[row][col]
				else:
					perem[i][j] = oldp[i][j] / oldp[row][col]

		for i in range(len(mcoef)):
			fcoef[i] = oldf[i] - (oldp[row][i] * oldf[col]) / oldp[row][col] 
			mcoef[i] = oldm[i] - (oldp[row][i] * oldm[col]) / oldp[row][col]
		
		fsvc = fsvc - (svc[row] * oldf[col]) / oldp[row][col]
		msvc = msvc - (svc[row] * oldm[col]) / oldp[row][col]

		olds = svc.copy()

		for i in range(len(svc)):
			if (i != row):
				svc[i] = svc[i] - (olds[row] * oldp[i][col]) / oldp[row][col]
			else:
				svc[i] = svc[i] / oldp[row][col]
				
		ind = mcoef.index(min(mcoef))

		ocen = []
		mo = -1
	
		for i in range(num):
			if perem[i][ind] == 0 or perem[i][ind] * svc[i] < 0 or perem[i][ind] < 0 and svc[i] == 0:
				ocen.append([True])
			else:
				ocen.append([False])
				ocen[i].append(svc[i] / perem[i][ind])
				mo = ocen[i][1]

		row = -1
		for i in range(num):
			if ocen[i][0] == False and ocen[i][1] <= mo:
				mo = ocen[i][1]
				row = i

		mc = min(mcoef)
		col = -1
		if (mc != 0):
			col = mcoef.index(mc)

		PrintTableM(bazis, svc, perem, y, yrow, fcoef, fsvc, mcoef, msvc, ocen, row, col)

	for i in range(len(y)):
		fcoef.pop()
		for j in range(len(perem)):
			perem[j].pop()

if (min(fcoef) < 0):
	ind = fcoef.index(min(fcoef))
	ocen = []
	mo = -1
	
	for i in range(num):
		if perem[i][ind] == 0 or perem[i][ind] * svc[i] < 0 or perem[i][ind] < 0 and svc[i] == 0:
			ocen.append([True])
		else:
			ocen.append([False])
			ocen[i].append(svc[i] / perem[i][ind])
			mo = ocen[i][1]

	row = -1
	for i in range(num):
		if ocen[i][0] == False and ocen[i][1] <= mo:
			mo = ocen[i][1]
			row = i

	fc = min(fcoef)
	col = -1
	if (fc < 0):
		col = fcoef.index(fc)


PrintTable(bazis, svc, perem, fcoef, fsvc, ocen, row, col)

while min(fcoef) < 0:
	bazis.pop(row)
	bazis.insert(row, col)

	oldp = []
	for i in range(len(perem)):
		oldp.append(perem[i].copy())

	oldf = fcoef.copy()
	
	for i in range(len(bazis)):
		for j in range(len(bazis) + 2):
			if (i != row):
				perem[i][j] = oldp[i][j] - (oldp[row][j] * oldp[i][col]) / oldp[row][col]
			else:
				perem[i][j] = oldp[i][j] / oldp[row][col]

	for i in range(len(fcoef)):
		fcoef[i] = oldf[i] - (oldp[row][i] * oldf[col]) / oldp[row][col] 
		
	fsvc = fsvc - (svc[row] * oldf[col]) / oldp[row][col]

	olds = svc.copy()

	for i in range(len(svc)):
		if (i != row):
			svc[i] = svc[i] - (olds[row] * oldp[i][col]) / oldp[row][col]
		else:
			svc[i] = svc[i] / oldp[row][col]
				
	ind = fcoef.index(min(fcoef))

	ocen = []
	mo = -1
	
	for i in range(num):
		if perem[i][ind] == 0 or perem[i][ind] * svc[i] < 0 or perem[i][ind] < 0 and svc[i] == 0:
			ocen.append([True])
		else:
			ocen.append([False])
			ocen[i].append(svc[i] / perem[i][ind])
			mo = ocen[i][1]

	row = -1
	for i in range(num):
		if ocen[i][0] == False and ocen[i][1] <= mo:
			mo = ocen[i][1]
			row = i

	fc = min(fcoef)
	col = -1
	if (fc < 0):
		col = fcoef.index(fc)

	PrintTable(bazis, svc, perem, fcoef, fsvc, ocen, row, col)


print("\nРЕЗУЛЬТАТ\nF max = ", fsvc, end='')
if m == 0:
	print("\t\tZ min = ", -fsvc)
print()