'''
    modul de test al functiilor non-ui
    - TestCheltuiala
    - TestCheltuieli
    - TestFunctii
'''

import data
from Cerinte import C2
from Cerinte.C5 import filtru1, filtru2
from Cerinte.C4 import suma_per_tip, ziua_cu_suma_maxima

class TestCheltuiala: # testeaza metodele clasei Cheltuiala
    def test_verify_ziua(self): # testeaza exceptiile aruncate pentru ziua gresita ca valoare
        try:
            data.Cheltuiala(32, 11, "altele") # o zi mai mare
            assert False
        except ValueError as err:
            if str(err) == "Ziua trebuie sa fie cuprinsa intre 1 si 31!\n":
                pass
            else:
                print(err)
        try:
            data.Cheltuiala(0, 11, "altele") # o zi mai mica
            assert False
        except ValueError as err:
            if str(err) == "Ziua trebuie sa fie cuprinsa intre 1 si 31!\n":
                pass
            else:
                print(err)
    def test_convert_ziua(self): # testeaza exceptiile aruncate pentru ziua gresita ca tip de date
        assert data.Cheltuiala("11", 22.9, "altele") # - corect
        try:
            data.Cheltuiala(("11", "22"), 11, "altele")  # zi - tuple
            assert False
        except TypeError as err:
            if str(err) == "Ziua trebuie sa fie un numar intreg!\n":
                pass
            else:
                print(err)
        try:
            data.Cheltuiala(11.2, 11, "altele")  # zi - numar real
            assert False
        except TypeError as err:
            if str(err) == "Ziua trebuie sa fie un numar intreg!\n":
                pass
            else:
                print(err)
    def test_verify_suma(self): # testeaza exceptiile aruncate pentru suma gresita ca valoare
        assert data.Cheltuiala(13, "11", 'telefon') # corect
        try:
            data.Cheltuiala(13, 0, "altele") # suma - nula
            assert False
        except ValueError as err:
            if str(err) == "Suma nu poate fi negativa sau nula!\n": pass
            else: print(err)
        try:
            data.Cheltuiala(13, -11, "altele") # suma - negativ intreg
            assert False
        except ValueError as err:
            if str(err) == "Suma nu poate fi negativa sau nula!\n": pass
            else: print(err)
        try:
            data.Cheltuiala(2, -0.1, "altele") # suma - negativ real
            assert False
        except ValueError as err:
            if str(err) == "Suma nu poate fi negativa sau nula!\n": pass
            else: print(err)
        try:
            data.Cheltuiala(2, 11.101, "altele") # suma - mai mult de 2 zecimale
            assert False
        except ValueError as err:
            if str(err) == "Suma are mai mult de 2 zecimale!\n": pass
            else: print(err)
    def test_convert_suma(self):# testeaza exceptiile aruncate pentru suma gresita ca tip de date
        assert data.Cheltuiala(2, "22.4", 'telefon') # corect
        try:
            data.Cheltuiala(12, "AB", "altele") # suma - sir de caractere
            assert False
        except TypeError as err:
            if str(err) == "Suma trebuie sa fie un numar intreg sau real!\n": pass
            else: print(err)
        try:
            data.Cheltuiala(11, data.Cheltuiala(11, 13, "mancare"), "altele") # suma - o cheltuiala
            assert False
        except TypeError as err:
            if str(err) == "Suma trebuie sa fie un numar intreg sau real!\n": pass
            else: print(err)
    def test_verify_tip(self): # testeaza exceptiile aruncate pentru valori gresite al tipului
        # tipul gresit ca valoare
        try:
            data.Cheltuiala(13, 11, "gunoi")  # tipul inexistent
            assert False
        except ValueError as err:
            if str(err) == "Acest tip de cheltuieli nu exista!\n":
                pass
            else:
                raise Exception(err)
        try:
            data.Cheltuiala(2, 0.1, "alte")  # tipul inexistent
            assert False
        except ValueError as err:
            if str(err) == "Acest tip de cheltuieli nu exista!\n":
                pass
            else:
                raise Exception(err)
    def test_convert_tip(self):# testeaza exceptiile aruncate pentru tipul de cheltuieli gresit ca tip de date
        try:
            altele = 13
            data.Cheltuiala(12, 11, altele)  # tip - o variabila definita cu alt scop
            assert False
        except TypeError as err:
            if str(err) == "Tipul trebuie sa fie un cuvant!\n":
                pass
            else:
                print(err)
        try:
            data.Cheltuiala(11, 12, data.Cheltuiala(11, 13, "mancare"))  # tipul - o cheltuiala
            assert False
        except TypeError as err:
            if str(err) == "Tipul trebuie sa fie un cuvant!\n":
                pass
            else:
                print(err)
    def test_egalitate(self): # testeaza egalitatea a doua cheltuieli
        c1 = data.Cheltuiala(1, 29.27, 'altele')
        c2 = data.Cheltuiala(2-1, 28+1.27, 'alt'+"ele")
        c3 = data.Cheltuiala(2, 29.27, 'altele')
        c4 = data.Cheltuiala(1, 29.26, 'altele')
        c5 = data.Cheltuiala(1, 29.27, 'telefon')

        try: assert (c1 == c2) # True
        except AssertionError as ex: print("Functia = nu returneaza adevarat pentru seturi de valori corecte!")
        try:
            assert  c1 == c3 # False, difera ziua
            raise NameError("Functia = returneaza adevarat pentru seturi de valori incorecte!")
        except AssertionError: pass

        try:
            assert c1 == c4 # False, difera suma
            raise NameError("Functia = returneaza adevarat pentru seturi de valori incorecte!")
        except AssertionError: pass

        try:
            assert c1 == c5 # False, difera tipul
            raise NameError("Functia = returneaza adevarat pentru seturi de valori incorecte!")
        except AssertionError: pass
    def test_actualizare(self): # testeaza functia de actualizare
        c = data.Cheltuiala(1, 29.29, 'intretinere')
        try:
            c.actualizare(2, 100, 'intretinere') # actualizare corecta
            assert False
        except AssertionError: pass
        try:
            c.actualizare(-1, 100, 'altele') # zi gresita
        except ValueError: pass
        try:
            c.actualizare(1, 100, 'telefon') # suma gresita
        except ValueError: pass
        try:
            c.actualizare(1, 2, 'Telefon') # tip gresit
        except ValueError: pass
    def test_str(self): # testeaza conversia la str
        c = data.Cheltuiala(2, 10, 'intretinere')
        assert str(c) == "2 10 intretinere"
        c = data.Cheltuiala(10, 9.99, 'telefon')
        assert str(c) == "10 9.99 telefon"
        c = data.Cheltuiala(25, 100.34, 'mancare')
        assert str(c) == "25 100.34 mancare"
        c = data.Cheltuiala(30, 2000.2, 'altele')
        assert str(c) == "30 2000.2 altele"

    def __init__(self):# testeaza functiile clasei cheltuieli
        # constructori corecti
        c1 = data.Cheltuiala(2, 23.15, "mancare")
        c2 = data.Cheltuiala(29, 12, "telefon")
        c3 = data.Cheltuiala.fromStr("2 30 altele")
        # testam get-ul field-urilor
        assert c1.zi == 2
        assert c2.suma == 12
        assert c3.tip == 'altele'
        # teste pentru date introduse gresit
        self.test_verify_ziua() # ziua introdusa gresit ca valoare
        self.test_verify_suma() # suma introdusa gresit ca valoare
        self.test_verify_tip()  # tipul introdus gresit ca valoare
        self.test_convert_ziua()  # ziua introdusa gresit ca tip de date
        self.test_convert_suma()  # suma introdusa gresit ca tip de date
        self.test_convert_tip()  # tipul introdus gresit ca tip de date
        # teste pentru functia =
        self.test_egalitate()
        # teste pentru actualizare
        self.test_actualizare()
        # test pentru conversia la sir de caractere
        self.test_str()

class TestCheltuieli: # testeaza metodele clasei cheltuieli
    def test_init(self): # testeaza constructorul
        c = data.Cheltuiala(1, 2, 'mancare')
        l = data.Cheltuieli() # fara parametrii
        assert len(l.lista)==0
        l = data.Cheltuieli(1, 2, 4.5, 'altele')  # parametrii incorecti
        assert len(l.lista) == 0
        l = data.Cheltuieli(c, c, c, c, c, c) #parametrii Cheltuiala
        assert len(l.lista)==6
        l = data.Cheltuieli([c, "<class=Cheltuiala>", c], c, [c, 1]) # parametrii liste de cheltuieli
        assert  len(l.lista)==4
    def test_iterable(self): # testeaza functiile len, iter, get, set, add, remove, index, append aplicate unui obiect Cheltuieli
        l = data.Cheltuieli(data.Cheltuiala(2, 3, 'mancare'), data.Cheltuiala(2, 3, 'intretinere'))
        assert len(l) == 2                        # len
        l += data.Cheltuiala(2, 3, 'intretinere') # add
        assert len(l) == 3
        l += data.Cheltuieli(data.Cheltuiala(2, 3, 'mancare'), data.Cheltuiala(2, 3, 'intretinere')) # list add
        assert len(l) == 5
        l += 2              # add gresit - lista nu se modifica
        assert len(l) == 5
        assert l.index(data.Cheltuiala(2, 3, 'mancare')) == 0 # index-ul unei valori
        l.removeAt(0)       # remove 0 - sterge din lista elementul cu indexul 0
        assert len(l) == 4
        assert l.index(data.Cheltuiala(2, 3, 'mancare')) == 2  # index-ul dupa ce lista s-a modificat
        assert l[0] == data.Cheltuiala(2, 3, 'intretinere')
        l.remove(data.Cheltuiala(2, 3, 'intretinere'))
        for c in l: # for loop
            assert c.suma == 3
            assert c.zi == 2
            c.actualizare(2, 2.25, 'altele')
        assert l[2].suma-2.25<0.001  # get
        l[2].tip = 'mancare'         # set
        assert l[2].tip == "mancare" #get
        l.append(data.Cheltuiala(2, 10, "altele"))
        assert len(l) == 4
        assert l[5] == None                         # set gresit - nu arunca eroare, returneaza None
    def test_whereEQ(self): # testeaza functiile where, si eq
        l = data.Cheltuieli(data.Cheltuiala(1, 2.3, 'telefon'), data.Cheltuiala(5, 7.7, 'telefon'), data.Cheltuiala(22, 10, 'mancare'), data.Cheltuiala(9, 2.3, 'mancare'), data.Cheltuiala(1, 40, 'altele'))
        assert l.where(zi=1) == [l[0], l[4]]
        assert l.where(tip='telefon') == data.Cheltuieli(l[0], l[1])
        assert l.where(suma=2.3) == [l[0], l[3]]
        assert l.where(function=lambda c: c.zi<=10) == [l[0], l[1], l[3], l[4]]
    def test_str(self): # testeaza functia str
        l = data.Cheltuieli(data.Cheltuiala(1, 2.3, 'telefon'), data.Cheltuiala(25, 117.7, 'mancare'))
        sep = '\n'
        assert str(l) == str(l[0])+sep+str(l[1])+sep
        l += data.Cheltuieli(data.Cheltuiala(1, 2.3, 'telefon'), data.Cheltuiala(25, 117.7, 'mancare'))
        assert str(l) == str(l[0])+sep+str(l[1])+sep+str(l[2])+sep+str(l[3])+sep
    def __init__(self):
        # rulam testele definite anterior
        self.test_init()
        self.test_iterable()
        self.test_whereEQ()
        self.test_str()

class TestFunctii: # testeaza functiile de calcul folosite in modulele cerintelor
    def test_sterge_zi(self): # testeaza functia sterge_zi din modulul C2.py
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'telefon'),
                            data.Cheltuiala(2, 10, 'telefon'),
                            data.Cheltuiala(2, 30, 'altele'),
                            data.Cheltuiala(3, 30, 'telefon'))
        C2.sterge_zi(l, 2)
        assert len(l) == 1
        assert l[0] == data.Cheltuiala(3, 30, 'telefon')
        l.append([data.Cheltuiala(2, 30, 'telefon'),
                  data.Cheltuiala(2, 30, 'telefon'),
                  data.Cheltuiala(2, 30, 'telefon'),
                  data.Cheltuiala(2, 30, 'telefon')])
        assert len(l) == 5
        C2.sterge_zi(l, 2)
        assert len(l) == 1
        assert l[0] == data.Cheltuiala(3, 30, 'telefon')
    def test_sterge_interval(self): # testeaza functia sterge_interval din modulul C2.py
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'telefon'),
                            data.Cheltuiala(30, 10, 'telefon'),
                            data.Cheltuiala(5, 30, 'altele'),
                            data.Cheltuiala(9, 30, 'telefon'),
                            data.Cheltuiala(11, 30, 'telefon'))
        C2.sterge_interval(l, 1, 10)
        assert l == [data.Cheltuiala(30, 10, 'telefon'), data.Cheltuiala(11, 30, 'telefon')]
        l.append([data.Cheltuiala(2, 30, 'telefon'),
                  data.Cheltuiala(31, 30, 'telefon'),
                  data.Cheltuiala(4, 30, 'telefon'),
                  data.Cheltuiala(10, 30, 'telefon')])
        C2.sterge_interval(l, 1, 10)
        assert l == [data.Cheltuiala(30, 10, 'telefon'), data.Cheltuiala(11, 30, 'telefon'), data.Cheltuiala(31, 30, 'telefon')]
    def test_sterge_tip(self): # testeaza functia sterge_tip din modulul C2.py
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'telefon'),
                            data.Cheltuiala(2, 10, 'telefon'),
                            data.Cheltuiala(2, 30, 'altele'),
                            data.Cheltuiala(3, 30, 'telefon'))
        C2.sterge_tip(l, 'telefon')
        assert l == [data.Cheltuiala(2, 30, 'altele')]
        l.append([data.Cheltuiala(3, 4, 'intretinere'),
                  data.Cheltuiala(2, 30, 'mancare'),
                  data.Cheltuiala(2, 30, 'mancare'),
                  data.Cheltuiala(2, 30, 'mancare'),
                  data.Cheltuiala(2, 30, 'mancare')])
        assert len(l) == 6
        C2.sterge_tip(l, 'mancare')
        assert len(l) == 2
        assert l == [data.Cheltuiala(2, 30, 'altele'), data.Cheltuiala(3, 4, 'intretinere')]
    def test_filtru1(self): # testeaza functia filtru1 din modulul C5.py
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'mancare'),
                            data.Cheltuiala(30, 10, 'telefon'),
                            data.Cheltuiala(5, 30, 'altele'),
                            data.Cheltuiala(9, 30, 'intretinere'),
                            data.Cheltuiala(11, 30, 'telefon'))
        assert filtru1(l, 'telefon') == [data.Cheltuiala(2, 30, 'mancare'),
                                        data.Cheltuiala(5, 30, 'altele'),
                                        data.Cheltuiala(9, 30, 'intretinere')]
        assert filtru1(l, 'altele') == data.Cheltuieli(data.Cheltuiala(2, 30, 'mancare'),
                                                        data.Cheltuiala(30, 10, 'telefon'),
                                                        data.Cheltuiala(9, 30, 'intretinere'),
                                                        data.Cheltuiala(11, 30, 'telefon'))
        assert filtru1(l, 'mancare') == data.Cheltuieli(data.Cheltuiala(30, 10, 'telefon'),
                                                        data.Cheltuiala(5, 30, 'altele'),
                                                        data.Cheltuiala(9, 30, 'intretinere'),
                                                        data.Cheltuiala(11, 30, 'telefon'))
        assert filtru1(l, 'intretinere') == data.Cheltuieli(data.Cheltuiala(2, 30, 'mancare'),
                                                            data.Cheltuiala(30, 10, 'telefon'),
                                                            data.Cheltuiala(5, 30, 'altele'),
                                                            data.Cheltuiala(11, 30, 'telefon'))
    def test_filtru2(self): # testeaza functia filtru1 din modulul C5.py
        l = data.Cheltuieli(data.Cheltuiala(2, 2, 'mancare'),
                            data.Cheltuiala(30, 10, 'telefon'),
                            data.Cheltuiala(5, 30, 'altele'),
                            data.Cheltuiala(9, 50, 'intretinere'),
                            data.Cheltuiala(11, 100, 'telefon'))
        assert filtru2(l, 1000) == []
        assert filtru2(l, 100) == data.Cheltuieli(data.Cheltuiala(11, 100, 'telefon'))
        assert filtru2(l, 40) == data.Cheltuieli(data.Cheltuiala(9, 50, 'intretinere'),
                                                 data.Cheltuiala(11, 100, 'telefon'))
        assert filtru2(l, 9) == data.Cheltuieli(data.Cheltuiala(30, 10, 'telefon'),
                                                data.Cheltuiala(5, 30, 'altele'),
                                                data.Cheltuiala(9, 50, 'intretinere'),
                                                data.Cheltuiala(11, 100, 'telefon'))
    def test_suma_per_tip(self):
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'mancare'),
                            data.Cheltuiala(30, 10.99, 'telefon'),
                            data.Cheltuiala(5, 30, 'altele'),
                            data.Cheltuiala(9, 11, 'intretinere'),
                            data.Cheltuiala(11, 39.01, 'telefon'),
                            data.Cheltuiala(2, 40, 'mancare'))
        assert suma_per_tip(l, 'telefon') == 50
        assert suma_per_tip(l, 'mancare') == 70
        assert suma_per_tip(l, 'altele') == 30
        assert suma_per_tip(l, 'intretinere') == 11
        assert suma_per_tip(l, 'imbracaminte') == 0
    def test_zi_cu_suma_maxima(self):
        l = data.Cheltuieli(data.Cheltuiala(2, 30, 'mancare'),
                            data.Cheltuiala(30, 10.99, 'telefon'),
                            data.Cheltuiala(5, 30, 'altele'),
                            data.Cheltuiala(9, 11, 'intretinere'),
                            data.Cheltuiala(11, 39.01, 'telefon'),
                            data.Cheltuiala(2, 40, 'mancare'))
        assert ziua_cu_suma_maxima(l) == 2
        l.append(data.Cheltuiala(30, 1000, 'mancare'))
        assert ziua_cu_suma_maxima(l) == 30
    def __init__(self): # apeleaza toate testele
        self.test_sterge_zi()
        self.test_sterge_interval()
        self.test_sterge_tip()
        self.test_filtru1()
        self.test_filtru2()
        self.test_suma_per_tip()
        self.test_zi_cu_suma_maxima()

class TestIstoric:
    def test_undo_str(self):
        ist = data.Istoric()
        assert isinstance(ist, data.Istoric)
        ist += "+ 1 1 altele"
        assert ist.tasklist[-1] == "+ 1 1 altele"
        assert ist.undo() == "- 1 1 altele"
        assert len(ist) == 0
        ist += "+ 1 1 altele"
        ist += "+ 2 1 altele"
        ist += "+ 3 1 altele"
        ist += "+ 4 1 altele"
        ist += "+ 5 1 altele*+6 2 mancare*+5 3 altele"
        ist += "- 5 1 altele"
        assert ist.undo() == "+ 5 1 altele"
        assert ist.undo() == "- 5 1 altele*-6 2 mancare*-5 3 altele"
        ist += "~ 13 20.4 altele^12 40 mancare"
        assert ist.undo() == "~ 12 40 mancare^13 20.4 altele"

    def test_add_remove(self):
        l = data.Cheltuieli(
            data.Cheltuiala(1, 1, "altele"),
            data.Cheltuiala(2, 2, "mancare"),
        )
        l.remove(data.Cheltuiala(1, 1, "altele"))
        l.istoric -= data.Cheltuiala(1, 1, "altele")

        l.append(data.Cheltuiala(10, 10, "altele"))
        l.istoric += data.Cheltuiala(10, 10, "altele")
        assert len(l.istoric) == 2
        assert l.istoric.tasklist[-1] == f"+ 10 10 altele"
        l.undo()
        assert l.istoric.tasklist[-1] == f"- 1 1 altele"
        l.undo()
        assert len(l.istoric) == 0
        try:
            l.undo()
            assert False
        except IndexError: pass
        l.append(data.Cheltuiala(10, 10, "altele"))
        l.istoric += data.Cheltuiala(10, 10, "altele")

        l[0].actualizare(1, 1, "mancare")
        l.istoric.append("~", "10 10 altele^1 1 mancare")
        assert l[0] == data.Cheltuiala(1, 1, "mancare")
        l.undo()
        assert l[0] == data.Cheltuiala(10, 10, "altele")
        assert len(l.istoric) == 1
        l.undo()
        assert len(l.lista) == 2

    def __init__(self):
        self.test_undo_str()
        self.test_add_remove()


TestCheltuiala()
TestCheltuieli()
TestFunctii()
TestIstoric()