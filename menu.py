"""
    definitia claselor:
    - Meniu
    - Optiune(OptiuneMeniu in versiunile anterioare)
"""

import os
import time
import colorama as cl
cl.init()

class Optiune: # optiune a unui meniu
    def __init__(self, comanda="*", nume="Opțiune", functie_rulare=lambda: 0, *params):
        self.nume = nume  # denumirea
        self.colornume = cl.Fore.LIGHTWHITE_EX  # culoare
        self.comanda = comanda  # scurtatura
        self.colorcomanda = cl.Fore.LIGHTYELLOW_EX # culoare comanda
        self.functie_rulare = functie_rulare  # functia de rulare - se executa cand utilizatorul alege optiunea
        self.clear_method = 'clear after time'
        '''
            no clear - nu se sterge, 
            clear after time - sterge la un interval de timp dupa ce functia de rulare isi incheie executia
            clear after input - sterge dupa apasarea tastei enter
        '''
        self.params = []  # parametrii functiei de rulare
        for param in params:
            self.params.append(param)

    #def __instancecheck__(self, instance): # verifica daca obiectul self este o Optiune
    #    return isinstance(instance.nume, str) and isinstance(instance.comanda, str) and type(instance.functie_rulare)=="<class 'function'>"

    def __str__(self): # afiseaza optiunea
        return self.colorcomanda + self.comanda + cl.Style.RESET_ALL + " - " + self.colornume + self.nume + cl.Style.RESET_ALL

    def show(self): # print
        print(self.colorcomanda, self.comanda + cl.Style.RESET_ALL, " - ", self.colornume + self.nume + cl.Style.RESET_ALL)

    def ruleaza(self): # se apeleaza functia de rulare cu parametrii respectivi
        if len(self.params)>=1: self.functie_rulare(*self.params)
        else: self.functie_rulare()


class Meniu:
    # meniul unei aplicatii si datele corespunzatoare
    def __init__(self, titlu="Meniu", clear_after_input=False, show_one_time=False):
        self.variabile = dict()  # variabilele globale ale meniului, definite de utilizator
        self.listaoptiuni = []
        # parte design
        self.show_one_time = show_one_time
        self.clear_after_input = clear_after_input
        self.titlu = titlu
        self.culoaretitlu = cl.Fore.LIGHTMAGENTA_EX
        self.inputmessage = "Introduceți o opțiune din meniu: "
        self.inputmessagecolor = cl.Fore.LIGHTYELLOW_EX
        self.inputcolor = cl.Fore.LIGHTRED_EX
        self.errormessage = "Opțiunea nu a fost găsită!\n"
        self.errorcolor = cl.Fore.LIGHTRED_EX
        self.left = ""
        self.pause = 3

    def add(self, optiune: Optiune):
        # adaugarea unei optiuni in meniu
        self.listaoptiuni.append(optiune)

    def add(self, comanda="*", nume="Opțiune", functie_rulare=lambda: 0, *params):
        # adaugarea unei optiuni in meniu
        self.listaoptiuni.append(Optiune(comanda, nume, functie_rulare, *params))

    def __add__(self, optiune: Optiune):
        # adaugarea unei optiuni in meniu
        self.listaoptiuni.append(optiune)
        return self

    def addVariabila(self, nume, variabila):
        # adaugarea unei variabile in meniu
        # acestea pot fi folosite ca parametrii ai functiilor de rulare
        self.variabile[nume] = variabila

    def __len__(self):
        # numarul de optiuni
        return len(self.listaoptiuni)

    def __getitem__(self, item):
        # returneaza o optiune dupa:
        #   indexul ei din lista
        #   stringul de comanda
        #   numele optiunii
        if isinstance(item, int): return self.listaoptiuni[item]
        for optiune in self.listaoptiuni:
            if optiune.comanda == item or optiune.nume == item:
                return optiune
        return None

    def __setitem__(self, item, value):
        # functia de rely
        if isinstance(item, int):
            self.listaoptuini[item] = value
        elif isinstance(item, Optiune):
            for optiune in self.listaoptiuni:
                if optiune.comanda == item or optiune.nume == item:
                    optiune = value

    def config(self):
        # configureaza optiunile meniului
        # 1. Dacă comenzile introduse să se șteargă automat - clear_after_input
        # 2. Numărul de secunde după care să aibă loc ștergerea - pause

        s = input("Doriți ca meniul " + self.titlu + " să șteargă automat datele introduse de dvs?\n\t")
        s = s.lower()
        sindex = 0
        eindex = len(s) - 1
        while s[sindex] == ' ': sindex = sindex + 1
        while s[eindex] == ' ': eindex = eindex - 1
        s = s[sindex: eindex + 1]
        if s == "da" or s == "yes" or s == "d" or s == "y":
            self.clear_after_input = True
            for _ in range(3):
                s = input("Introduceți numărul de secunde pentru refresh-ul ecranului: ")
                try:
                    s = int(s)
                except ValueError:
                    try:
                        s = float(s)
                    except Exception:
                        print("Vă rugăm să introduceți o valoare numerică validă!")
                        continue
                self.pause = s
                break
            else:
                print("Număr de încercări prea mare.\n Durata va fi setată automat la " + str(self.pause) + " secunde.")
        else:
            self.clear_after_input = False
        print("\n Mulțumim! ☺")
        time.sleep(self.pause)
        os.system('cls')

    def show_menu(self):
        # afiseaza meniul
        # -titlul
        # -optiunile
        if (self.titlu != ""): print(self.left, self.culoaretitlu + self.titlu, cl.Style.RESET_ALL)
        for optiune in self.listaoptiuni:
            print(self.left, optiune, sep="")
        print()

    def interpret_input(self): # interpreteaza optiunile introduse de utilizator
        print(self.left + self.inputmessagecolor + self.inputmessage, self.inputcolor, end='')
        s = input()
        print(cl.Style.RESET_ALL, end='')
        for optiune in self.listaoptiuni:
            if s == optiune.nume or s == optiune.comanda:
                optiune.ruleaza()
                print()
                return optiune
        else:
            if s == "": self.interpret_input()
            else:
                print(self.left, self.errorcolor + self.errormessage + cl.Style.RESET_ALL, sep='')
                self.interpret_input()

    def run(self): # ruleaza meniul
        self.show_menu()
        if self.show_one_time:
            self.interpret_input()
            return
        while True:
            opt = self.interpret_input()
            if opt.clear_method == "clear after time":
                time.sleep(self.pause)
                os.system('cls')
                self.show_menu()
            elif opt.clear_method == "clear after input":
                print(self.left + cl.Fore.LIGHTBLUE_EX + "Apasati o tasta pentru a continua" + cl.Fore.RESET, end=" ")
                input()
                os.system('cls')
                self.show_menu()