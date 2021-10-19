from data import Cheltuiala
from menu import *

def input_cheltuiala(left=""): # citeste o cheltuiala
    print(cl.Fore.RESET + left + "Ziua din luna: " + cl.Fore.LIGHTGREEN_EX, end='')
    zi = input()
    print(cl.Fore.RESET + left + "Suma: " + cl.Fore.LIGHTGREEN_EX, end='')
    suma = input()
    print(cl.Fore.RESET + left + "Tipul: " + cl.Fore.LIGHTGREEN_EX, end='')
    tip = input()
    return (zi, suma, tip)

def input_zi(left, msg="Introduceti ziua: "):  # obtine ziua de la utilizator sau None daca nu este introdusa corect
                                               # msg - mesajul afisat la introducere
                                               # functie ui
    print(left + "  " + cl.Fore.LIGHTGREEN_EX + msg + cl.Fore.RESET, end="")
    zi = input()
    try:
        zi = int(zi)
        assert zi > 0 and zi <= 31
    except ValueError:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Ziua trebuie sa fie un numar intreg!" + cl.Fore.RESET)
    except AssertionError:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Ziua trebuie sa fie un numar cuprins intre 1 si 31!" + cl.Fore.RESET)
    else:
        return zi

def input_tip(left, msg="Introduceti tipul: "):
    print(left + "  " + cl.Fore.LIGHTGREEN_EX + msg + cl.Fore.RESET, end="")
    tip = input()
    if tip in Cheltuiala.tipcheltuilei:
        return tip
    else:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Acest tip de cheltuieli nu exista!" + cl.Fore.RESET)

def input_suma(left, msg="Introduceti suma: "):
    print(left + "  " + cl.Fore.LIGHTGREEN_EX + "Introduceti suma: " + cl.Fore.RESET, end="")
    suma = input()
    try:
        suma = float(suma)
        assert suma>0
    except ValueError:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Suma trebuie sa fie un numar intreg sau real!" + cl.Fore.RESET)
    except AssertionError:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Suma trebuie sa fie un numar strict pozitiv!" + cl.Fore.RESET)
    else:
        return suma

def output_cheltuieli(cheltuieli, left): # afiseaza lista cheltuielilor
    if len(cheltuieli)>0:
        print(left + cl.Fore.LIGHTMAGENTA_EX+"    Cheltuieli:"+cl.Fore.RESET)
        for chelt in cheltuieli:
            s = chelt.suma
            epsilon = 0.000001
            if s-int(s)<epsilon:
                s = int(s)
            print(left + f"- In {cl.Fore.LIGHTYELLOW_EX}ziua{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX_EX}{str(chelt.zi)}{cl.Fore.RESET}, {cl.Fore.LIGHTYELLOW_EX}suma{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX}{str(s)}{cl.Fore.RESET}, {cl.Fore.LIGHTYELLOW_EX}tipul{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX_EX}{str(chelt.tip)}{cl.Fore.RESET};")
    else: print(left + "  " + cl.Fore.LIGHTRED_EX + "Nu exista cheltuieli adaugate!" + cl.Fore.RESET)