"""
1.
Hozz létre három tömböt - listát!
1. érdemjegyeket tartalmazzon
2. az iskola osztályainak elnevezését tartalmazza
3. diákok adatait tartalmazza
"""

osztalyzatok = [1, 2, 3, 4, 5]
osztalyok = ['9.A', '9.B',  '10.A', '10.B',  '11.A', '11.B',  '12.A', '12.B', '1/13b']
diakok = [ ['Kiss', 'Anna', '9.A'], ['Nagy', 'Eszter', '12.B'], ['Kovács', 'Ákos', '1/13b']]

"""
2.
Az előző feladatban létrehozott tömbök hermadik elemét adjuk az adott tömb
1. az első elem értékéül
2. a második elem értékéül
3. az utolsó elem értékéül
"""

osztalyzatok[0] = osztalyzatok[2]
osztalyok[1] = osztalyok[2]
diakok[-1] = diakok[2]

"""
3.
Írasd ki a tömbjeid hosszát és az elemeit egy sorban szóközzel elválaszva!
"""
print (len(osztalyzatok), end=" ")
print('*'.join(osztalyok))
for x in osztalyzatok:
    print(x, end= ", ")
print()

"""
4.
Távolítsd el a tömbökből az első elemet!
1. Az első tömbre használd a del parancsot
2. A második tömbre használd a pop() metódust és távolítsd el az utolsó elemet
3. A harmadik tömbre használd a remove() metódust
"""

del osztalyzatok[0]
osztalyok.pop(0)
osztalyok.pop()
diakok.remove(diakok[0])
print(diakok)

"""
5.
Adott az alábbi lista: [21, 32, 13, 44, 75] 

1. lépés: írjunk egy kódsort, amely megkérdezi a felhasználót, hogy melyik elemet mdosítsa a program.
Az adott elemet módosítsd a felhasználó által megadott számra.

2. lépés: írjunk egy kódsort, amely eltávolítja az utolsó elemet a listából.

3. lépés: írjunk egy kódsort, amely kiírja a meglévő lista hosszát.

3. lépés: Írjunk kódot, mely kiírja sorban a lista elemeit. Soronként egye-egy elemet.
"""
szamok = [21, 32, 13, 44, 75]

index = int(input("Hanyadik elemet szeretnéd módosítani? "))
uj_szam = int(input("Mi legyen az új érték? "))

szamok[index-1] = uj_szam
print(szamok)

"""
6.
Hozz létre egy programot, mely bekéri, hogy hány elemet szeretnél megadni, majd
létrehoz egy listát és
feltölti a tömböt a felhasználó által megadott értékekkel
A lista elemeinek sorrendje egyezzen meg a felhasználó által megadott értékek sorrendjével!
"""
db = int(input("Hány elemet szeretnél megadni?"))

tomb = []

for i in range(db):
    tomb.append(input("Kérem az értéket: "))

print(tomb)

"""
7.
Hozz létre egy programot, mely
bekéri, hogy hány elemet szeretnél megadni, majd
létrehoz egy listát és
feltölti a iistát a felhasználó átal megadott értékekkel
A lista elemeinek sorrendje fordítottja legyen a felhasználó által megadott értékek sorrendjének!
"""

db = int(input("Hány elemet szeretnél megadni? "))

lista = [None] * db

for i in range(db, 0, -1):
    lista[i] = input("Kérem az értéket: ")

#lista.reverse()
print(lista)
