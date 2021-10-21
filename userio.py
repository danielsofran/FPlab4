from data import Cheltuiala
from menu import *

def input_cheltuiala(left=""):
    '''
    citeste o cheltuiala introdusa
    :param left: spatiile din stanga folosite la afisare
    :return: ziua, suma si tipul introduse
    :rtype: tuple
    '''
    print(cl.Fore.RESET + left + "Ziua din luna: " + cl.Fore.LIGHTGREEN_EX, end='')
    zi = input()
    print(cl.Fore.RESET + left + "Suma: " + cl.Fore.LIGHTGREEN_EX, end='')
    suma = input()
    print(cl.Fore.RESET + left + "Tipul: " + cl.Fore.LIGHTGREEN_EX, end='')
    tip = input()
    return (zi, suma, tip)

def input_zi(left, msg="Introduceti ziua: "):
    '''
       citeste ziua introdusa de utilizator
       :param left: spatiile din stanga folosite la afisare
       :param msg: mesajul afisat
       :return: ziua sau None
    '''
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

def input_tip(left, msg="Introduceti tipul: "): # citeste tipul, left = padding-left, msg = mesajul afisat
    '''
        citeste tipul introdus de utilizator
        :param left: spatiile din stanga folosite la afisare
        :param msg: mesajul afisat
        :return: tipul sau None
        '''
    print(left + "  " + cl.Fore.LIGHTGREEN_EX + msg + cl.Fore.RESET, end="")
    tip = input()
    if tip in Cheltuiala.tipcheltuilei:
        return tip
    else:
        print(left + "  " + cl.Fore.LIGHTRED_EX + "Acest tip de cheltuieli nu exista!" + cl.Fore.RESET)

def input_suma(left, msg="Introduceti suma: "):
    '''
    citeste suma introdusa de utilizator
    :param left: spatiile din stanga folosite la afisare
    :param msg: mesajul afisat
    :return: suma sau None
    '''
    print(left + "  " + cl.Fore.LIGHTGREEN_EX + msg + cl.Fore.RESET, end="")
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

def output_cheltuieli(cheltuieli, left, errormsg="Nu exista astfel de cheltuieli adaugate!"):
    '''
    afiseaza lista cheltuielilor
    :param cheltuieli: lista cheltuielilor
    :param left: spatiile din stanga folosite la afisare
    :param errormsg: mesaj de eroare in cazul in care lista este vida
    :return: None
    '''
    print()
    if len(cheltuieli)>0:
        print(left + cl.Fore.LIGHTMAGENTA_EX+"    Cheltuieli:"+cl.Fore.RESET)
        for chelt in cheltuieli:
            s = chelt.suma
            epsilon = 0.000001
            if s-int(s)<epsilon:
                s = int(s)
            print(left + f"- In {cl.Fore.LIGHTYELLOW_EX}ziua{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX}{str(chelt.zi)}{cl.Fore.RESET}, {cl.Fore.LIGHTYELLOW_EX}suma{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX}{str(s)}{cl.Fore.RESET}, {cl.Fore.LIGHTYELLOW_EX}tipul{cl.Fore.RESET}: {cl.Fore.LIGHTGREEN_EX}{str(chelt.tip)}{cl.Fore.RESET};")
    else: print(left + "  " + cl.Fore.LIGHTRED_EX + errormsg + cl.Fore.RESET)