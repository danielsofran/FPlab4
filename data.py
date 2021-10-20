"""
    modul in care se declara clasele care stocheaza datele si functiile lor
"""

class Cheltuiala:
    '''
        Cheltuiala - tipul de date care retine datele unei cheltuieli
        zi : intreg - reprezinta numarul zilei din luna
        suma : numar real - reprezinta suma cheltuita
        tip : tipul cheltuielii
        tipcheltuieli : lista cu categoriile posibile de cheltuieli
    '''

    tipcheltuilei = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele'] # categoriile posibile de cheltuieli

    def __init__(self, zi, suma, tip): # constructor
        t = self.convert(zi, suma, tip)
        zi, suma, tip = t
        self.verify_data(zi, suma, tip)
        self.zi = zi
        self.suma = suma
        self.tip = tip

    def __eq__(self, other): # verifica egalitatea dinre doua cheltuieli
        epsilon = 0.001
        try: return self.zi == other.zi and self.suma - other.suma < epsilon and self.tip == other.tip
        except Exception as ex:
            print("ex")
            return False

    def actualizare(self, zi, suma, tip): # functie care actualizeaza datele despre cheltuiala
        t = self.convert(zi, suma, tip)
        zi, suma, tip = t
        self.verify_data(zi, suma, tip)
        self.zi = zi
        self.suma = suma
        self.tip = tip

    def verify_data(self, zi, suma, tip):  # verifica daca datele sunt valide
        '''
            :raise: ValueError
        '''
        ex = ""  # string de exceptie
        if zi < 1 or zi > 31:
            ex += "Ziua trebuie sa fie cuprinsa intre 1 si 31!\n"
        if suma <= 0:
            ex += "Suma nu poate fi negativa sau nula!\n"
        else:
            ok = True
            try:
                str(suma).index('.')
            except ValueError:
                ok = False
            if ok and len(str(suma).rsplit('.')[-1]) > 2:
                ex += "Suma are mai mult de 2 zecimale!\n"
        try:
            assert Cheltuiala.tipcheltuilei.index(tip) >= 0
        except Exception:
            ex += "Acest tip de cheltuieli nu exista!\n"
        if ex != "": raise ValueError(ex)

    def convert(self, zi, suma, tip):
        '''
            incearca sa converteasca valorile date la tipurile membrilor clasei
            :raise: TypeError daca conversia este imposibila
            :return: un tuple de tip (zi, suma, an), in care valorile au fost convertite
        '''
        try:
            epsilon = 0.0000001
            if isinstance(zi, float) and zi-int(zi)>epsilon: raise Exception
            zi = int(zi)
        except Exception: raise TypeError("Ziua trebuie sa fie un numar intreg!\n")
        try:
            suma = float(suma)
        except Exception: raise TypeError("Suma trebuie sa fie un numar intreg sau real!\n")
        if not isinstance(tip, str):
            raise TypeError("Tipul trebuie sa fie un cuvant!\n")
        return (zi, suma, tip)

    def __str__(self): # conversie la sir de caractere
        s = self.suma
        epsilon = 0.0000001
        if s-int(s)<epsilon:
            s = int(s)
        return f"Cheltuiala in ziua: {str(self.zi)}, suma: {str(s)}, tipul: {str(self.tip)}"

class Cheltuieli:
    '''
        lista - lista de cheltuileli
    '''
    def __init__(self, *params): # adauga parametrii de tip Cheltuiala si liste de cheltuieli, ignorandu-i pe ceilalti
        self.lista = []
        for param in params:
            if isinstance(param, list) or isinstance(param, tuple):
                for elem in param:
                    if isinstance(elem, Cheltuiala):
                        self.lista.append(elem)
            elif isinstance(param, Cheltuiala):
                self.lista.append(param)

    def __len__(self): return len(self.lista) # determina numarul de cheltuieli

    def __iter__(self): # returneaza iteratorul catre primul element din lista, functia va fi folosita in parcurgerea for
        return iter(self.lista)

    def index(self, value: Cheltuiala): # gaseste primul index al valorii date in lista, sau -1 daca nu este gasita
        for i in range(len(self.lista)):
            if self.lista[i] == value:
                return i
        return -1

    def __add__(self, other): # adauga o cheltuiala in lista
        if isinstance(other, Cheltuiala):
            self.lista.append(other)
            return self
        elif isinstance(other, (Cheltuieli, list, tuple)): # sau mai multe
            for c in other:
                if isinstance(c, Cheltuiala):
                    self.lista.append(c)
            return self
        return self

    def append(self, other): # adauga o cheltuiala in lista
        if isinstance(other, Cheltuiala):
            self.lista.append(other)
        elif isinstance(other, (Cheltuieli, list, tuple)): # sau mai multe
            for c in other:
                if isinstance(c, Cheltuiala):
                    self.lista.append(c)

    def removeAt(self, index: int): # sterge din lista elementul cu indexul index
        self.lista.remove(self.lista[index])
    def remove(self, value: Cheltuiala): # sterge din lista prima aparitie a valorii date
        self.lista.remove(value)

    def __getitem__(self, item: int): # indexator
        if item <len(self):
            return self.lista[item]
        return None

    def __setitem__(self, item: int, value: Cheltuiala): # indexator
        if item <len(self):
            self.lista[item].actualizare(value.zi, value.suma, value.tip)

    def __eq__(self, other): # pentru a testa mai usor, verifica elementele si ordinea lor
        if isinstance(other, Cheltuieli):
            return self.lista == other.lista
        elif isinstance(other, list):
            for i in range(len(other)):
                if self.lista[i] != other[i]:
                    return False
            return True
        return False

    def where(self, **kvargs):
        '''
        returneaza cheltuielile care respecta o anumita UNICA proprietate
        :param kvargs: dictionar de forma (proprietate: valoare),
                       proprietatea - cea a unei cheltuieli, adica ziua, suma sau tipul
                                    - function
                       valoarea - un literal specific
                                - functia : poate fi o functie booleana de tip predicat
        :return: o lista de cheltuieli care respecta o anumita proprietate - prin functie sau daca au o valoare a unui membru
        :rtype: list
        '''
        rez = Cheltuieli()
        for key, value in kvargs.items():
            if (key=='zi' or key=='ziua') and isinstance(value, int):
                for c in self.lista:
                    if c.zi == value:
                        rez+=c
            elif key=='suma' and (isinstance(value, int) or isinstance(value, float)):
                for c in self.lista:
                    epsilon = 0.0000001
                    if abs(c.suma - value)<epsilon:
                        rez+=c
            elif key=='tip' and isinstance(value, str):
                for c in self.lista:
                    if c.tip == value:
                        rez+=c
            elif key=='function' and str(type(value)) == "<class 'function'>":
                for c in self.lista:
                    if (value(c)):
                        rez += c
                return rez
        return rez

    def __str__(self): # conversia la sir de caractere, scop in testare
        rez=""
        for c in self.lista:
            rez += str(c) + '\n'
        return rez