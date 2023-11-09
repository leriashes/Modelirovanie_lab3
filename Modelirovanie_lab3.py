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


def PrintRow(letter, numb, svc, perem, ocen):
    print()
    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')

    print()

    print("  ", letter, sep='', end='')
    PrintNumb(numb)
    print("   |{: ^10.3}|".format(svc), end='')

    for p in perem:
        print("{: ^6.3}|".format(p), end='')

    if (ocen[0] == True):
        ocenka = "∞"
    else:
        ocenka = ocen[1]

    print("{: ^16.3}".format(ocenka), end='')


def PrintFRow(fsv, fcoef):
    print()
    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')
    
    print("\n  F    |{: ^10}|".format(fsv), end='')

    for coef in fcoef:
        print("{: ^6}|".format(coef), end='')

    print()

    for i in range(46 + round((7 * (len(bazis) + len(y) + 2) - 10) / 2) * 2):
        print("-", end='')
    

def PrintTableM(bazis, svc, perem, y, yrow, fcoef, fsv, mcoef, msv, ocen, row, col):
    PrintHeader(len(bazis) + len(y));
    PrintPerem(bazis, y)
    
    for i in range(len(yrow)):
        PrintRow('y', y[i], svc[y[i]], perem[y[i]], ocen[i])
        
        if i == row:
            print(" ← ", end='')


    for i in range(len(bazis)):
        pr = True
        k = bazis[i] - bazis[0]
        for j in range(len(yrow)):
            if k == y[j]:
                pr = False

        if pr:
            PrintRow('x', bazis[i], svc[i], perem[i], ocen[i])

            if i == row:
                print(" ← ", end='')

    PrintFRow(fsv, fcoef)

    print("\n  -Mф  |{: ^10}|".format(str(msv) + "M"), end='')
    

    for coef in mcoef:
        if (coef != 0):
            print("{: ^6}|".format(str(coef) + "M"), end='')
        else:
            print("{: ^6}|".format(coef), end='')


    print()
    if (col > -1):
        for i in range(col * 7 + 21):
            print(" ", end='')
        print("↑")
    print("\n\n")

    return

def PrintTable(bazis, svc, perem):
    PrintHeader(len(bazis))
    return


def Mcount(mcoef, msvc):
    mcoef = []
    for i in range(num + 2):
        s = 0
        for j in range(len(y)):
            s += perem[y[j]][i]
        mcoef.append(s * -1)

    msvc = 0
    for i in range(len(y)):
        mcoef.append(0.0)
        msvc -= svchlen[y[i]]

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


y = []

for i in range(num):
    if b[i] * a[i][2] < 0:
        y.append(i)

yrow = y.copy()

bazis = [i + 2 for i in range(num)]
svchlen = [b[i] for i in range(num)]
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

if len(y) == 0:
    PrintTable(bazis, svchlen, perem)
else:

    for i in range(len(yrow)):
        perem[y[i]] += [.0 for j in range(i)] + [-1.0 if svchlen[y[i]] < 0 else 1.0] + [.0 for j in range(len(y) - i - 1)]

    for i in range(len(bazis)):
        pr = True
        k = bazis[i] - 2
        for j in range(len(yrow)):
            if k == y[j]:
                pr = False

        if pr:
            perem[k] += [0.0 for j in range(len(y))]


    mcoef = []
    msvc = 0
    (mcoef, msvc) = Mcount(mcoef, msvc)

    minM = min(mcoef)
    ind = mcoef.index(minM)

    ocen = []
    mo = -1
    
    for i in range(num):
        if perem[i][ind] == 0 or perem[i][ind] * svchlen[i] < 0 or perem[i][ind] < 0 and svchlen[i] == 0:
            ocen.append([True])
        else:
            ocen.append([False])
            ocen[i].append(svchlen[i] / perem[i][ind])
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

    PrintTableM(bazis, svchlen, perem, y, yrow, fcoef, 0, mcoef, msvc, ocen, row, col)

    while mc != 0:

        bazis.pop(row)
        bazis.insert(row, col)

        oldp = []
        for i in range(len(perem)):
            oldp.append(perem[i].copy())

        yrow.pop(yrow.index(row))

        for i in range(len(bazis)):
            for j in range(len(bazis) + len(y)):
                if (i != row):
                    perem[i][j] = oldp[i][j] - (oldp[row][j] * oldp[i][col]) / oldp[row][col]
                else:
                    perem[i][j] = oldp[i][j] / oldp[row][col]

            (mcoef, msvc) = Mcount(mcoef, msvc)

    minM = min(mcoef)
    ind = mcoef.index(minM)

    ocen = []
    mo = -1
    
    for i in range(num):
        if perem[i][ind] == 0 or perem[i][ind] * svchlen[i] < 0 or perem[i][ind] < 0 and svchlen[i] == 0:
            ocen.append([True])
        else:
            ocen.append([False])
            ocen[i].append(svchlen[i] / perem[i][ind])
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

        PrintTableM(bazis, svchlen, perem, y, yrow, fcoef, 0, mcoef, msvc, ocen, row, col)