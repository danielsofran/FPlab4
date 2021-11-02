# cerinta 5

from userio import *
from data import Cheltuieli

def filtru1(cheltuieli, tip):
    '''
    determina lista de cheltuieli care nu au tipul dat
    :param cheltuieli: lista de cheltuieli
    :param tip: tipul dat
    :return: lista cheltuielilor filtrate
    :rtype: Cheltuieli
    '''
    rez = Cheltuieli()
    for chelt in cheltuieli:
        if chelt.tip != tip:
            rez += chelt
    return rez

def filtru2(cheltuieli, suma):
    '''
    determina lista de cheltuieli care au suma mai mare sau egala decat lista initiala
    :param cheltuieli: lista de cheltuieli
    :param suma: suma data
    :return: lista cheltuielilor filtrate
    :rtype: Cheltuieli
    '''
    rez = Cheltuieli()
    for chelt in cheltuieli:
        if chelt.suma >= suma:
            rez += chelt
    return rez

def filtru1_ui(cheltuieli, left):
    '''
    functie ui pentru filtrul1
    :param cheltuieli: o lista de cheltuieli
    :param left: numarul de spatii din stanga afisarilor
    :return: None
    '''
    tip = input_tip(left, "Introduceti tipul care urmeaza sa fie eliminat: ")
    if tip is not None:
        l = filtru1(cheltuieli, tip)
        output_cheltuieli(l, left)

def filtru2_ui(cheltuieli, left): # functie ui pentru filtru2
    suma = input_suma(left, "Suma: ")
    if suma is not None:
        l = filtru2(cheltuieli, suma)
        output_cheltuieli(l, left)

def meniu_filtru(cheltuieli): #submeniul cerintei 5
    meniu = Meniu("\n\t  Selectați o opțiune de filtrare:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Elimină toate cheltuielile de un anumit tip", filtru1_ui, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.LIGHTCYAN_EX
    meniu += Optiune("2", "Elimină toate cheltuielile mai mici decât o sumă dată", filtru2_ui, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.LIGHTCYAN_EX
    meniu.run()