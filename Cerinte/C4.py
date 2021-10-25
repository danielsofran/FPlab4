# cerinta 4

from userio import *

def suma_per_tip(cheltuieli, tip): # calculeaza si returneaza suma cheltuielilor de tipul tip
    s = 0
    for chelt in cheltuieli:
        if chelt.tip == tip:
            s += chelt.suma
    return s

def ziua_cu_suma_maxima(cheltuieli): # returneaza PRIMA zi in care suma este maxima sau 0 daca nu exista cheltuieli in lista
    zi_maxima = 0
    suma_maxima = 0
    for chelt in cheltuieli:
        if chelt.suma > suma_maxima:
            zi_maxima = chelt.zi
            suma_maxima = chelt.suma
    return zi_maxima

def o1(cheltuieli, left): # optiunea 1, fct ui pentru functia
    tip = input_tip(left)
    if tip is not None:
        s = suma_per_tip(cheltuieli, tip)
        if s > 0:
            print(left + cl.Fore.LIGHTGREEN_EX + "Suma " + cl.Fore.RESET + "tuturor cheltuielilor cu tipul " +
                  cl.Fore.YELLOW + tip + cl.Fore.RESET + " este " + cl.Fore.LIGHTGREEN_EX + str(s) + cl.Fore.RESET + ".")
        else: output_error(left, "Nu exista cheltuieli de tipul " + cl.Fore.YELLOW + tip + cl.Fore.RED + "!")

def o2(cheltuieli, left): # optiunea 2 din submeniu
    zi = ziua_cu_suma_maxima(cheltuieli)
    if zi > 0: print(f"{left}{cl.Fore.YELLOW}Ziua{cl.Fore.RESET} in care suma cheltuita este maxima este {cl.Fore.LIGHTGREEN_EX}{zi}{cl.Fore.RESET}.")
    else: output_error(left, "Nu exista cheltuieli adaugate!")

def o3(cheltuieli, left): # optiunea 3 din submeniu
    suma = input_suma(left)
    if suma is not None:
        l = cheltuieli.where(suma=suma)
        output_cheltuieli(l, left, f"Nu exista cheltuilei care sa aiba suma {cl.Fore.YELLOW}{suma}{cl.Fore.LIGHTRED_EX}!")

def o4(cheltuieli, left): # optiunea 4
    cheltuieli.lista.sort(key=lambda elem: elem.tip)
    output_cheltuieli(cheltuieli, left)

def meniu_rapoarte(cheltuieli): #submeniul cerintei 4
    meniu = Meniu("\n\t  Selectați o opțiune de raportare:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Suma totală pentru un anumit tip de cheltuială", o1, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("2", "Ziua în care suma cheltuită e maximă", o2, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("3", "Toate cheltuielile ce au o anumită sumă", o3, cheltuieli, meniu.left)
    meniu[2].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("4", "Cheltuielile sortate după tip", o4, cheltuieli, meniu.left)
    meniu[3].colornume = cl.Fore.LIGHTCYAN_EX
    meniu.run()