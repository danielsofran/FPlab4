# cerinta 3

from userio import *

def o1(cheltuieli, left): # optiunea 1 a submeniului
    suma = input_suma(left + "  ")
    if suma is not None:
        l = cheltuieli.where(function=lambda chelt: chelt.suma>suma)
        output_cheltuieli(l, left)

def o2(cheltuiei, left): # optiunea 2 a submeniului
    zi = input_zi(left + "  ")
    if zi is None: return
    suma = input_suma(left + "  ")
    if suma is not None:
        l = cheltuiei.where(function=lambda chelt: chelt.zi<zi and chelt.suma<suma)
        output_cheltuieli(l, left)

def o3(cheltuieli, left): # optiunea 3 a submeniului
    tip = input_tip(left + "  ")
    if tip is not None:
        l = cheltuieli.where(tip=tip)
        output_cheltuieli(l, left)

def meniu_caut(cheltuieli): # submeniul cerintei 3
    meniu = Meniu("\n\t  Selectați o opțiune de cautare:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Cheltuielile mai mari decât o sumă dată", o1, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("2", "Cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă", o2, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("3", "Cheltuielile de un anumit tip", o3, cheltuieli, meniu.left)
    meniu[2].colornume = cl.Fore.LIGHTCYAN_EX
    meniu.run()