from userio import *

def undo(cheltuieli): # anuleaza ultima operatie efectuata pe lista cheltuieli
    try:
        print("Operatii efectuate:")
        print(cheltuieli.istoric.showlast())
        cheltuieli.undo()
        #if len(cheltuieli)>0:
        #    userio.output_cheltuieli(cheltuieli, " ")
    except Exception as ex: output_error("", "Nu exista operatii ce pot fi anulate!")
    else: print(cl.Fore.LIGHTGREEN_EX + "Ultima operatie de adaugare/stergere/actualizare a fost anulata!"+cl.Fore.RESET)

def redo(cheltuieli): # reface ultima cheltuiala
    try:
        cheltuieli.redo()
        #if len(cheltuieli)>0:
        #    userio.output_cheltuieli(cheltuieli, " ")
    except Exception as ex: output_error("", "Nu exista operatii ce pot fi refacute!")
    else: print(cl.Fore.LIGHTGREEN_EX + "Ultima operatie de adaugare/stergere/actualizare a fost refacuta!"+cl.Fore.RESET)