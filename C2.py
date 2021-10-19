from userio import *

def sterge_zi(lista, zi:int): # sterge toate cheltuielile din ziua zi, functie de calcul ce returneaza numarul de elemente sterse
    l = lista.where(zi=zi)
    for elem in l:
        lista.remove(elem)
    return len(l)

def sterge_interval(lista, zi_inceput:int, zi_sfarsit:int): # sterge toate cheltuielile care zile cuprinse in intervalul dat, functie de calcul ce returneaza numarul de elemente sterse
    l = lista.where(function= lambda chelt: chelt.zi>=zi_inceput and chelt.zi<=zi_sfarsit)
    for elem in l:
        lista.remove(elem)
    return len(l)

def sterge_tip(lista, tip:str): # sterge toate cheltuielile de un anumit tip, functie de calcul ce returneaza numarul de elemente sterse
    l = lista.where(tip=tip)
    for elem in l:
        lista.remove(elem)
    return len(l)

def ui_sterge_zi(cheltuieli, left): # functie ui pentru functia sterge_zi
    if len(cheltuieli)==0:
        print(left + cl.Fore.LIGHTRED_EX + "Nu exista cheltuieli adaugate!" + cl.Fore.RESET)
        return
    zi = input_zi(left+ "  ")
    if zi is not None:
        nr = sterge_zi(cheltuieli, zi)
        if nr>0: print(left + cl.Fore.LIGHTGREEN_EX + f"{nr} + cheltuieli din ziua "+str(zi)+" au fost sterse!" + cl.Fore.RESET)
        else: print(left + cl.Fore.LIGHTRED_EX + "Nici o cheltuiala nu respecta proprietatea data!" + cl.Fore.RESET)

def ui_sterge_interval(cheltuieli, left): # functie ui pentru functia sterge_interval
    if len(cheltuieli)==0:
        print(left + cl.Fore.LIGHTRED_EX + "Nu exista cheltuieli adaugate!" + cl.Fore.RESET)
        return
    zi1 = input_zi(left+ "  ", "Introduceti ziua de inceput: ")
    if zi1 is None: return
    zi2 = input_zi(left+ "  ", "Introduceti ziua de sfarsit: ")
    if zi1 is None: return
    if zi1<zi2:
        nr = sterge_interval(cheltuieli, zi1, zi2)
        if nr>0: print(left + cl.Fore.LIGHTGREEN_EX + f"{nr} cheltuieli care incep in ziua {zi1} si se termina in ziua {zi2} inclusiv au fost sterse!" + cl.Fore.RESET)
        else: print(left + cl.Fore.LIGHTRED_EX + "Nici o cheltuiala nu respecta proprietatea data!" + cl.Fore.RESET)
    else: print(left + cl.Fore.LIGHTRED_EX + "Ziua de inceput trebuie sa fie inaintea zilei de sfarsit!" + cl.Fore.RESET)

def ui_sterge_tip(cheltuieli, left): # functie ui pentru functia sterge_tip
    if len(cheltuieli)==0:
        print(left + cl.Fore.LIGHTRED_EX + "Nu exista cheltuieli adaugate!" + cl.Fore.RESET)
        return
    tip = input_tip(left+ "  ")
    if tip is not None:
        nr = sterge_tip(cheltuieli, tip)
        if nr>0: print(left + cl.Fore.LIGHTGREEN_EX + f"{nr} cheltuieli cu tipul {tip} au fost sterse!" + cl.Fore.RESET)
        else: print(left + cl.Fore.LIGHTRED_EX + "Nici o cheltuiala nu respecta proprietatea data!" + cl.Fore.RESET)

def meniu_remove(cheltuieli): # submeniul cerintei 2
    meniu = Meniu("\n\t  Selectați o opțiune de stergere:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Toate cheltuielile dintr-o zi", ui_sterge_zi, cheltuieli, meniu.left )
    meniu[0].colornume = cl.Fore.RED
    meniu += Optiune("2", "Cheltuielile dintr-un interval de timp", ui_sterge_interval, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.RED
    meniu += Optiune("3", "Toate cheltuielile de un anumit tip", ui_sterge_tip,cheltuieli, meniu.left)
    meniu[2].colornume = cl.Fore.RED
    meniu.run()