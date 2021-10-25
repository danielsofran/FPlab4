from menu import *
from data import Cheltuieli
from Cerinte.C1 import meniu_add
from Cerinte.C2 import meniu_remove
from Cerinte.C3 import meniu_caut
from Cerinte.C4 import meniu_rapoarte
from Cerinte.C5 import meniu_filtru
import test

def undo(cheltuieli): #todo
    pass

def main(): # meniul principal
    meniu = Meniu("\n\tCheltuieli de familie\n", clear_after_input=True)
    l = Cheltuieli()
    meniu += Optiune("1", "Adăugare", meniu_add, l)
    meniu[0].colornume = cl.Fore.LIGHTGREEN_EX
    meniu += Optiune("2", "Ștergere", meniu_remove, l)
    meniu[1].colornume = cl.Fore.RED
    meniu += Optiune("3", "Căutare", meniu_caut, l)
    meniu[2].colornume = cl.Fore.LIGHTCYAN_EX
    meniu[2].clear_method = "clear after input"
    meniu += Optiune("4", "Rapoarte", meniu_rapoarte, l)
    meniu[3].colornume = cl.Fore.LIGHTCYAN_EX
    meniu[3].clear_method = "clear after input"
    meniu += Optiune("5", "Filtrare", meniu_filtru, l)
    meniu[4].colornume = cl.Fore.LIGHTCYAN_EX
    meniu[4].clear_method = "clear after input"
    meniu += Optiune("6", "Undo", undo, l)
    meniu[5].colornume = cl.Fore.BLUE
    meniu.run()

main()
