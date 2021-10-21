from userio import *

def validate(cheltuiala_tuple, left=""):
    '''
    valideaza o cheltuiala introdusa de utilizator
    :param cheltuiala_tuple: un tuple care retine proprietatile unei cheltuieli
    :param left: spatiile din stanga, folosite la afisarea erorilor
    :return: o cheltuiala valida sau False in caz contrar
    '''
    c = None
    try:
        c = Cheltuiala(cheltuiala_tuple[0], cheltuiala_tuple[1], cheltuiala_tuple[2])
    except ValueError as exc:
        print(cl.Fore.LIGHTRED_EX + left + str(exc) + cl.Fore.RESET)
        return
    except TypeError as exc:
        print(cl.Fore.LIGHTRED_EX + left + str(exc) + cl.Fore.RESET)
        return
    return c

def adauga_ui(cheltuieli, left=""): # adauga o cheltuiala valida in lista, left = padding-left
    c = validate(input_cheltuiala(left+"   "), left)
    if c is None: return
    cheltuieli.append(c)
    print(left + cl.Fore.LIGHTGREEN_EX + str(c) + " s-a adaugat cu succes!")

def actualizare_ui(cheltuieli, left=""): # actualizeaza o cheltuiala din lista, left = padding-left
    print(cl.Fore.GREEN +"\n"+ left + "  Introduceti o cheltuiala existenta: ")
    c = validate(input_cheltuiala(left+" "), left)
    index = cheltuieli.index(c)
    if index>=0:
        print(cl.Fore.GREEN + "\n"+ left + "  Introduceti noua cheltuiala:")
        noua = validate(input_cheltuiala(left), left)
        if noua is not None:
            cheltuieli[index].actualizare(noua.zi, noua.suma, noua.tip)
            print(left + cl.Fore.LIGHTGREEN_EX + "Cheltuiala introdusa s-a adaugat cu succes!")
    else: print(left + cl.Fore.LIGHTRED_EX + "Cheltuiala introdusa nu a fost gasita!" + cl.Fore.RESET)

def meniu_add(cheltuieli): # submeniul cerintei 1
    meniu = Meniu("\n\t  Selectați o opțiune:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Adaugă o cheltuială nouă", adauga_ui, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.GREEN
    meniu += Optiune("2", "Actualizează o cheltuială", actualizare_ui, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.GREEN
    meniu.run()