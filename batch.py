import test
from data import *
from Cerinte.C2 import sterge_tip, sterge_zi, sterge_interval
from Cerinte.C4 import suma_per_tip, ziua_cu_suma_maxima

def showexc(func): # apeleaza functia
    def inner(*params):
        try: func(*params)
        except Exception as e: print(e)
    return inner

@showexc
def add(cmd, l): # adauga o cheltuiala in lista
    c = Cheltuiala.fromStr(cmd)
    l.append(c)

@showexc
def update(cmd, l): # actualizeaza o cheltuiala existenta cu noi date
    c = cmd.split(' ')
    c1 = Cheltuiala(c[0], c[1], c[2])
    c2 = Cheltuiala(c[3], c[4], c[5])
    if not c1 in l: raise Exception("Cheltuiala nu exista in lista!")
    i = l.index(c1)
    l[i] = c2

@showexc
def del_zi(cmd, l): # sterge toate cheltuilelile dintr-o zi
    zi = Cheltuiala(cmd, 1, "altele").zi
    c = Cheltuiala(zi, 2, "altele")
    sterge_zi(l, zi)

@showexc
def del_tip(cmd, l): # sterge toate cheltuielile de un anumit tip
    c = Cheltuiala(1, 1, cmd)
    sterge_tip(l, cmd)

@showexc
def cauta_tip(cmd, l): # cauta toate cheltuielile de un anumit tip
    c = Cheltuiala(1, 1, cmd)
    rez = l.where(tip=cmd)
    print(rez)

@showexc
def cauta_suma(cmd, l): # cauta cheltuielile mai mari decât o sumă dată
    c = Cheltuiala(1, cmd, "altele")
    s = c.suma
    rez = l.where(function = lambda c: c.suma>s)
    print(rez)

@showexc
def print_l(cmd, l): # afiseaza lista de cheltuieli
    print(l)

@showexc
def raport_suma_per_tip(cmd, l): # totalul cheltuielilor de un anumit tip
    c = Cheltuiala(1, 1, cmd)
    print(suma_per_tip(l, c.tip))

@showexc
def raport_zi_suma_maxima(cmd, l): # ziua in care suma este maxima
    print(ziua_cu_suma_maxima(l))

@showexc
def raport_suma(cmd, l): # toate cheltuielile cu suma data
    c = Cheltuiala(cmd, 1, "altele")
    rez = l.where(suma=cmd)
    print(rez)

@showexc
def raport_ordonare(cmd, l):
    l.lista.sort(key=lambda elem: elem.tip)
    print(l)

def batch_show(): # interfata batch
    l = Cheltuieli()
    cmds = {
        "add": add,
        "update": update,
        "remove zi": del_zi,
        "remove tip": del_tip,
        "cauta tip":cauta_tip,
        "print": print_l,
        "cauta suma": cauta_suma,
        "raport suma per tip": raport_suma_per_tip,
        "raport zi cu suma maxima": raport_zi_suma_maxima,
        "raport suma": raport_suma,
        "raport ordonare tip": raport_ordonare
    }
    while True:
        cmd = input(">")
        sir = cmd.split(" * ")
        for s in sir:
            for key, fct in cmds.items():
                if s[:len(key)] == key:
                    fct(s[len(key)+1:], l)
                    break
            else: print("Comanda nu a fost gasita!")

batch_show()