from userio import *

def validate(cheltuiala_tuple, left=""): # valideaza tripletul introdus si afiseaza erorile daca exista, sau returneaza cheltuiala
    c = None
    try:
        c = Cheltuiala(cheltuiala_tuple[0], cheltuiala_tuple[1], cheltuiala_tuple[2])
    except ValueError as ex:
        print(cl.Fore.LIGHTRED_EX + left + str(ex) + cl.Fore.RESET)
        return False
    except TypeError as ex:
        print(cl.Fore.LIGHTRED_EX + left + str(ex) + cl.Fore.RESET)
        return False
    return c

def adauga_ui(cheltuieli, left=""): # adauga o cheltuiala valida in lista
    c = validate(input_cheltuiala(left+"  "), left)
    if c == False: return
    cheltuieli.append(c)
    print(cl.Fore.LIGHTGREEN_EX + left + str(c) + " s-a adaugat cu succes!")

def actualizare_ui(cheltuieli, left=""): # actualizeaza o cheltuiala din lista
    print(cl.Fore.GREEN +"\n"+ left + "  Introduceti o cheltuiala existenta: ")
    c = validate(input_cheltuiala(left+" "), left)
    index = cheltuieli.index(c)
    if index>=0:
        print(cl.Fore.GREEN + "\n"+ left + "  Introduceti noua cheltuiala:")
        noua = validate(input_cheltuiala(left), left)
        if noua != False:
            cheltuieli[index].actualizare(noua.zi, noua.suma, noua.tip)
            print(cl.Fore.LIGHTGREEN_EX + left + "Cheltuiala introdusa s-a adaugat cu succes!")
    else: print(cl.Fore.LIGHTRED_EX + left + "Cheltuiala introdusa nu a fost gasita!" + cl.Fore.RESET)

def meniu_add(cheltuieli): # submeniul cerintei 1
    meniu = Meniu("\n\t  Selectați o opțiune:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Adaugă o cheltuială nouă", adauga_ui, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.GREEN
    meniu += Optiune("2", "Actualizează o cheltuială", actualizare_ui, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.GREEN
    meniu.run()