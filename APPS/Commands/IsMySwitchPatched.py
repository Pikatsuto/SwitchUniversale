import os
import re
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

#désolé pour les variable qui ne sont pas en accord un des dev n'a pas réspécté la charte et ne l'a pas encore corigé

def IsMySwitchPatched():
    IMSPFin = False
    while IMSPFin != True:
        if IMSPFin == True:
            return()
        Clear()
        print(" Votre Nintendo Switch est patchée?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quiter\n")
        userSerial = input("Entrez votre numéro de série : ")
        serialNumber = ""

        userSerial.lower()
        if userSerial == "q":
            return()

        def DefFin():
            input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nApuité sur entré pour retourné en ariere: ")
            os.system('COLOR 60')

        def safeResult(prefix, number):
            if _platform == 'win32':
                os.system('COLOR 2')
            Clear()
            print(f" Numéro de série : {prefix} - {number}\n Status : Votre Nintendo Switch n'est pas patchée.")
            DefFin()

        def possiblyPatchedResult(prefix, number):
            if _platform == 'win32':
                os.system('COLOR 6')
            Clear()
            print(f" Numéro de série : {prefix} - {number}\n Status : Votre Nintendo Switch est peut-être patchée, testez, vous ne risquez rien.")
            DefFin()

        def patchedResult(prefix, number):
            if _platform == 'win32':
                os.system('COLOR 4')
            Clear()
            print(f" Numéro de série : {prefix} - {number}\n Status : Votre Nintendo Switch est patchée.")
            DefFin()

        def unknownResult(prefix, number):
            if _platform == 'win32':
                os.system('COLOR 8')
            Clear()
            print(f" Numéro de série : {prefix} - {number}\n Status : Votre numéro de série est inconnu. Une faute de frappe ?")
            DefFin()

        try:
            userSerial = userSerial.replace(" ", "")
            serialNumber = re.findall(r'[X][A-Z]{2}[0-9]{7,14}', userSerial, re.IGNORECASE)[0]
            serialNumber = serialNumber.upper()

            prefix = serialNumber[0:4]
            numberStr = (serialNumber[4:14])

            while len(numberStr) != 10:
                numberStr = f"{numberStr}0"

            number = int(numberStr)

            if prefix.startswith("XKW") or prefix.startswith("XKJ") or prefix.startswith("XJE"):
                patchedResult(serialNumber[0:3], serialNumber[3:11])
            elif prefix.startswith("XAK"):
                possiblyPatchedResult(serialNumber[0:3], serialNumber[3:11])

            if prefix == "XAW1":
                if(number <= 74990000):
                    safeResult(prefix, numberStr)
                elif(75000000 <= number <= 120000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAW4":
                if(number <= 11000000):
                    safeResult(prefix, numberStr)
                elif(11000000 < number <= 12000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAW7":
                if(number <= 17800000):
                    safeResult(prefix, numberStr)
                elif(17800000 < number <= 30000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAJ1":
                if(number <= 20000000):
                    safeResult(prefix, numberStr)
                elif(20000000 < number <= 30000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAJ4":
                if(number <= 46000000):
                    safeResult(prefix, numberStr)
                elif(46000000 < number <= 83000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAJ7":
                if(number <= 40000000):
                    safeResult(prefix, numberStr)
                elif(40000000 < number <= 50000000):
                    possiblyPatchedResult(prefix, numberStr)
                else:
                    patchedResult(prefix, numberStr)

            if prefix == "XAW9":
                patchedResult(prefix, numberStr)

            if(not prefix.startswith("XJE") and not prefix.startswith("XKJ") and not prefix.startswith("XKW") and prefix != "XAW1" and prefix != "XAW4" and prefix != "XAW7" and prefix != "XAJ1" and prefix != "XAJ4" and prefix != "XAJ7" and prefix != "XAW9"):
                unknownResult(prefix, numberStr)

        except IndexError:
            if(len(userSerial) < 10):
                Valide = False
                Quite = ""
                while Valide != True:
                    print(" Vous devez spécifier au moins les 10 premiers caractères de votre numéro de série...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    Recommence = input(" (Q) Pour quitter (R) Pour recommencer: ")
                    Recommence = Recommence.lower()
                    if Quite == "q":
                        Valide = True
                        IMSPFin = True
                        return()
                    if Quite == "r":
                        Valide = True
            else:
                Valide = False
                while Valide != True:
                    print(" Votre numéro de série est incorrect...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    Recommence = input(" (Q) Pour quitter (R) Pour recommencer: ")
                    Recommence = Recommence.lower()
                    if Quite == "q":
                        Valide = True
                        IMSPFin = True
                        return()
                    if Quite == "r":
                        Valide = True