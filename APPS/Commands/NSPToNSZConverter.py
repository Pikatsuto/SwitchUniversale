import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def NSPToNSZConverter():# Menu [(2) NSZ Converter]
    os.system("py -m pip install --upgrade nsz")
    CompresseAndDe = ""
    while CompresseAndDe == "":

        Clear()
        print(" Copier tous vos jeux dans le dossier input\n Il ressortirons dans le même dossier\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
        CompresseAndDe = (input(" Voulez-vous Compresser[C] ou Décompresser[D]: "))
        CompresseAndDe = CompresseAndDe.lower()

    if CompresseAndDe == "q":
        return()
    os.system('COLOR 0f')
    if CompresseAndDe == "c":
        os.system(f'Data\\NSZ\\nsz.exe -o "Input" -C "Input"')

    elif CompresseAndDe == "d":
        os.system(f'Data\\NSZ\\nsz.exe -o "Input" -D "Input"')
    os.system('COLOR 60')