# cerinta 1

from userio import *

def adauga_ui(cheltuieli, left=""): # adauga o cheltuiala valida in lista, left = padding-left
    c = input_cheltuiala(left)
    if c is None: return
    #cheltuieli.istoric += c
    cheltuieli.append(c)
    cheltuieli.istoric.append("+", c)
    print(left + cl.Fore.LIGHTGREEN_EX + c.show() + " s-a adaugat cu succes!" + cl.Fore.RESET)

def actualizare_ui(cheltuieli, left=""): # actualizeaza o cheltuiala din lista, left = padding-left
    print(cl.Fore.GREEN +"\n"+ left + "  Introduceti o cheltuiala existenta: ")
    c = input_cheltuiala(left)
    if c is None: return
    index = cheltuieli.index(c)
    if index>=0:
        print(cl.Fore.GREEN + "\n"+ left + "  Introduceti noua cheltuiala:")
        noua = input_cheltuiala(left)
        if noua is not None:
            cheltuieli.istoric.append("~", f"{cheltuieli[index]}^{noua}")
            cheltuieli[index].actualizare(noua.zi, noua.suma, noua.tip)
            print(left + cl.Fore.LIGHTGREEN_EX + "Cheltuiala introdusa s-a adaugat cu succes!")
    else: output_error(left, "Cheltuiala introdusa nu a fost gasita!")

def meniu_add(cheltuieli): # submeniul cerintei 1
    meniu = Meniu("\n\t  Selectați o opțiune:\n", clear_after_input=False, show_one_time=True)
    meniu.left = "\t"
    meniu.inputmessage = "Introduceți opțiunea: "
    meniu += Optiune("1", "Adaugă o cheltuială nouă", adauga_ui, cheltuieli, meniu.left)
    meniu[0].colornume = cl.Fore.GREEN
    meniu += Optiune("2", "Actualizează o cheltuială", actualizare_ui, cheltuieli, meniu.left)
    meniu[1].colornume = cl.Fore.GREEN
    meniu.run()