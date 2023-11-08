import numpy as np

def WrongFormat():
    print("Неверный формат файла")
    exit()

def PrintNumb(i):
    n = ['₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
    print(n[i], end='')

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

def PrintHeader(num):
    for i in range(46 + round((7 * (num + 2) - 10) / 2) * 2):
        print("-", end='')

    print("\n Базис | Св. член |", end='')
    for i in range(round((7 * (num + 2) - 10) / 2)):
        print(" ", end='')
    print("Переменные", end='')
    for i in range(round((7 * (num + 2) - 10) / 2)):
        print(" ", end='')
    print("| Оцен. отношение\n", end='')

    print("       |          |", end='')
    for i in range(round((7 * (num + 2) - 10) / 2) * 2 + 10):
        print("-", end='')
    print("|                \n", end='')

def PrintPerem(bazis, y):
    print("       |          |", end='')
    for i in range(len(bazis) + 2):
        print("  x", end='')
        PrintNumb(i)
        print("  |", end='')

    for i in range(len(y)):
        print("  y", end='')
        PrintNumb(y[i])
        print("  |", end='')
    
    print()

    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')
    print()

def PrintRow(letter, numb, svc, perem, ocen):
    print("  ", letter, sep='', end='')
    PrintNumb(numb)
    print("   |{: ^10}|".format(svc), end='')

    for p in perem:
        print("{: ^6}|".format(p), end='')

    infin = False

    if (ocen[0] == True):
        ocenka = "∞"
    else:
        ocenka = ocen[1]

    print("{: ^16}".format(ocenka))

    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')
    print()

def PrintFRow(fsv, fcoef):
    print("  F    |{: ^10}|".format(fsv), end='')

    for coef in fcoef:
        print("{: ^6}|".format(coef), end='')
    
    print()

    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')
    print()

def PrintTableM(bazis, svc, perem, y, fcoef, fsv, mcoef, ocen):
    PrintHeader(len(bazis) + len(y));
    PrintPerem(bazis, y)
    
    for i in range(len(y)):
        PrintRow('y', y[i], svc[y[i]], perem[y[i]] + [0 for j in range(i)] + [-1 if svc[y[i]] < 0 else 1] + [0 for j in range(len(y) - i - 1)], ocen[i])

    for i in range(len(bazis)):
        pr = True
        k = bazis[i] - 2
        for j in range(len(y)):
            if k == y[j]:
                pr = False

        if pr:
            PrintRow('x', bazis[i], svc[k], perem[k] + [0 for j in range(len(y))], ocen[i])

    PrintFRow(fsv, fcoef)

    print("  -Mф  |   -M     |", end='')

    for coef in mcoef:
        if (coef != 0):
            print("{: ^6}|".format(str(coef) + "M"), end='')
        else:
            print("{: ^6}|".format(coef), end='')

    print("\n\n")

    return

def PrintTable(bazis, svc, perem):
    PrintHeader(len(bazis));
    return

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


y = []

for i in range(num):
    if b[i] * a[i][2] < 0:
        y.append(i)

bazis = [i + 2 for i in range(num)]
svchlen = [b[i] for i in range(num)]
perem = [[] for i in range(num)]
fcoef = [c[0] * -1, c[1] * -1] + [0 for i in range(num + len(y))]

for i in range(num):
    for j in range(num + 2):
        if j < 2:
            perem[i].append(a[i][j])
        elif j == i + 2:
            perem[i].append(a[i][2]) 
        else:
            perem[i].append(0)

if len(y) == 0:
    PrintTable(bazis, svchlen, perem)
else:
    mcoef = []

    for i in range(num + 2):
        s = 0
        for j in range(len(y)):
            s += perem[y[j]][i]
        mcoef.append(s * -1)

    for i in range(len(y)):
        s = 1

        if (svchlen[y[i]] <= 0):
            s = -1

        mcoef.append(s * -1.0)

    minM = min(mcoef)
    ind = mcoef.index(minM)

    ocen = []

    for i in range(num):
        if perem[i][ind] == 0 or perem[i][ind] == 0 * svchlen[i] < 0:
            ocen.append([True])
        else:
            ocen.append([False])
            ocen[i].append(svchlen[i] / perem[i][ind])


    PrintTableM(bazis, svchlen, perem, y, fcoef, 0, mcoef, ocen)


   # while minM != 0:
