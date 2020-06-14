import os
import json
from Commands.Clear import Clear

def SwitchGet():

    RepoApps = "https://switchbru.com/appstore/repo.json"
    RepoPoyoTheme = "https://raw.githubusercontent.com/Bakassable/PoyoTools/master/PoyoTools%20DB/themes.json"

    PatchSD = {
        "Atmosphere": {
            "Theme": "ulaunch/themes",
            "Apps": "switch",
            "OS": "",
            "NSP": "NSP",
            "XCI": "NSP",
            "Firmwares": "Firmwares",
            "KIPS": "atmosphere/kips",
            "Contents": "atmosphere/contents",
            "Roms": {
                "NES": "Roms/NES",
                "SNES": "Roms/SNES",
                "GBA": "Roms/GBA",
                "GBC": "Roms/GBC",
                "GB": "Roms/GB",
                "N64": "Roms/N64",
                "GC": "Roms/GC"
            }
        },
        "ReyNX": {
            "Theme": "ulaunch/themes",
            "Apps": "switch",
            "OS": "",
            "NSP": "NSP",
            "XCI": "NSP",
            "Firmwares": "Firmwares",
            "KIPS": "ReiNX/kips",
            "Contents": "ReiNX/contents",
            "Roms": {
                "NES": "Roms/NES",
                "SNES": "Roms/SNES",
                "GBA": "Roms/GBA",
                "GBC": "Roms/GBC",
                "GB": "Roms/GB",
                "N64": "Roms/N64",
                "GC": "Roms/GC"
            }
        },
        "SXOS": {
            "Apps": "switch",
            "OS": "",
            "NSP": "sxos/nsp",
            "XCI": "sxos/xci",
            "Firmwares": "Firmwares",
            "KIPS": "sxos/kips",
            "Contents": "sxos/contents",
            "Roms": {
                "NES": "Roms/NES",
                "SNES": "Roms/SNES",
                "GBA": "Roms/GBA",
                "GBC": "Roms/GBC",
                "GB": "Roms/GB",
                "N64": "Roms/N64",
                "GC": "Roms/GC"
            }
        }
    }


    os.system(f'Data\\Wget\\wget.exe "{RepoApps}"')
    with open("repo.json", "r") as file:
        DBUse = json.load(file)#ouverture de la DB
        file.close

    os.system(f'Data\\Wget\\wget.exe "{RepoPoyoTheme}"')
    with open("themes.json", "r") as file:
        DBPoyoTheme = json.load(file)#ouverture de la DB
        file.close

    FilDir = []
    val = 0
    while val != 50000:
        try:
            DBUpdate = ({
                "category": DBUse["packages"][val]["category"],
                "updated": DBUse["packages"][val]["updated"], 
                "name": DBUse["packages"][val]["name"],
                "author": DBUse["packages"][val]["author"],
                "license": DBUse["packages"][val]["license"], 
                "title": DBUse["packages"][val]["title"],
                "details": DBUse["packages"][val]["details"],
                "version": DBUse["packages"][val]["version"],
                "icon": "https://switchbru.com/appstore/packages/{}/icon.png".format(DBUse["packages"][val]["name"]),
                "screen": "https://switchbru.com/appstore/packages/{}/screen.png".format(DBUse["packages"][val]["name"]),
                "download": "https://switchbru.com/appstore/zips/{}.zip".format(DBUse["packages"][val]["name"]),
                "switchbru": "https://switchbru.com/appstore/#/app/{}".format(DBUse["packages"][val]["name"]),
                "source": DBUse["packages"][val]["url"]
            })
            DBTMP = (DBUse["packages"][val])
            DBTMP.update(DBUpdate)
            DBUse.update(DBTMP)
            FilDir.append(DBUse["packages"][val]["binary"])
            val += 1
        except IndexError:
            val += 1
            skyp = True
    
    with open("repo.json", "w+") as file:
        json.dump(DBUse, file, indent=4)
        file.close

    with open("repo.json", "r") as file:
        DBUse = json.load(file)#ouverture de la DB
        file.close

    Recherche = ""
    while Recherche == "":
        Clear()
        Recherche = input("Entré votre recherche\nLes paramètres pris en compte sont le nom, l'auteur, la catégorie et le titre.\nvous pouvez écrire le début ou la fin.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEntré votre recherche: ")
        Recherche = Recherche.lower()
    
    FileDownload = []
    URL = []
    NameUse = []
    AuthorUse = []
    def GitAdd():
        FileSplit = ["", Recherche]
        print(FileSplit)
        FileSplit[0] = "https://api.github.com/repos/"
        FileSplit.append("/releases/latest")
        FileSplit = (f"{FileSplit[0]}{FileSplit[1]}{FileSplit[2]}")
        os.system(f'Data\\Wget\\wget.exe "{FileSplit}"')
        os.system("rename latest latest.json")
        Clear()
        try:
            with open("latest.json", "r") as file:
                latest = json.load(file)#ouverture de la DB
                file.close
            try:
                for assets in latest["assets"]:
                    FileDownload.append(assets["browser_download_url"])
                    NameTMP = assets["browser_download_url"]
                    NameTMP = NameTMP.split("/")
                    NameTMP = NameTMP[-1]
                    NameUse.append(NameTMP)
                    AuthorTMP = Recherche
                    AuthorTMP = AuthorTMP.split("/")
                    AuthorTMP = AuthorTMP[0]
                    AuthorUse.append(AuthorTMP)
                    FilDir.append("Auto")
            except UnboundLocalError:
                skyp = True
            os.system("del latest.json")
            val = 0
            for N in NameUse:
                print(f"[{val}] GitHub {N} By {AuthorUse[val]}")
                val += 1
        except FileNotFoundError:
            skyp = True

        

    skyp = True    
    val = 0
    val2 = 0
    Clear()
    skyp2 = True
    while  Recherche != 300:
        try:
            try:
                if DBUse["packages"][val]["name"].lower().startswith(Recherche) or DBUse["packages"][val]["name"].lower().endswith(Recherche):
                    if skyp == True:
                        FileDownload.append(DBUse["packages"][val]["download"])
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        if val2 < 10:
                            print(f" [{val2}]  AppsStore {DBName} By {Author}")
                        else:
                            print(f" [{val2}] AppsStore {DBName} By {Author}")
                        val2 += 1
                        skyp = False
                        skyp2 = False
            except KeyError:
                skyp = True
            try:
                if DBUse["packages"][val]["title"].lower().startswith(Recherche) or DBUse["packages"][val]["title"].lower().endswith(Recherche):
                    if skyp == True:
                        FileDownload.append(DBUse["packages"][val]["download"])
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        if val2 < 10:
                            print(f" [{val2}]  AppsStore {DBName} By {Author}")
                        else:
                            print(f" [{val2}] AppsStore {DBName} By {Author}")
                        val2 += 1
                        skyp = False
                        skyp2 = False
            except KeyError:
                skyp = True
            try:
                if DBUse["packages"][val]["author"].lower().startswith(Recherche) or DBUse["packages"][val]["author"].lower().endswith(Recherche):
                    if skyp == True:
                        FileDownload.append(DBUse["packages"][val]["download"])
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        if val2 < 10:
                            print(f" [{val2}]  AppsStore {DBName} By {Author}")
                        else:
                            print(f" [{val2}] AppsStore {DBName} By {Author}")
                        val2 += 1
                        skyp = False
                        skyp2 = False
            except KeyError:
                skyp = True
            try:
                if DBUse["packages"][val]["category"].lower() == Recherche:
                    if skyp == True:
                        FileDownload.append(DBUse["packages"][val]["download"])
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        if val2 < 10:
                            print(f" [{val2}]  AppsStore {DBName} By {Author}")
                        else:
                            print(f" [{val2}] AppsStore {DBName} By {Author}")
                        val2 += 1
                        skyp = False
                        skyp2 = False
            except KeyError:
                skyp = True
            skyp = True
        except IndexError:
            break
        val += 1
        if val2 == 15:
            break
    
    if val2 != 15:
        val = 0
        while Recherche != 300:
            try:
                Author = DBPoyoTheme[val]["author"]
                Author = Author.split("By ")
                Author = Author[-1]
                try:
                    if DBPoyoTheme[val]["name"].lower().startswith(Recherche) or DBPoyoTheme[val]["name"].lower().endswith(Recherche):
                        if skyp == True:
                            FileDownload.append(DBPoyoTheme[val]["download"])
                            DBName = DBPoyoTheme[val]["name"]
                            if val2 < 10:
                                print(f" [{val2}]  ThemePoyo {DBName} By {Author}")
                            else:
                                print(f" [{val2}] ThemePoyo {DBName} By {Author}")
                            val2 += 1
                            skyp = False
                            FilDir.append("Theme")
                except KeyError:
                    skyp = True
                try:
                    if Author.lower().startswith(Recherche) or Author.lower().endswith(Recherche):
                        if skyp == True:
                            FileDownload.append(DBPoyoTheme[val]["download"])
                            DBName = DBPoyoTheme[val]["name"]
                            if val2 < 10:
                                print(f" [{val2}]  ThemePoyo {DBName} By {Author}")
                            else:
                                print(f" [{val2}] ThmemPoyo {DBName} By {Author}")
                            val2 += 1
                            skyp = False
                            skyp2 = False
                            FilDir.append("Theme")
                except KeyError:
                    skyp = True
                skyp = True
            except IndexError:
                skyp = True
            val += 1
            if val2 == 15:
                break
            if val == 1000:
                break

    if val2 != 15:
        if skyp2 == True:
            try:
                try:
                    GitAdd()
                    val += 1
                except KeyError:
                    skyp = True
            except IndexError:
                skyp = True
        
    os.system(f'del "repo.json"')
    os.system(f'del "themes.json"')

    val = 15
    for DL in FileDownload:
        val -= 1

    if val == 15:
        print(" Aucun résultat trouvé.")
        val -= 1
    while val != 0:
        print("")
        val -=1
    
    print("\n Quiter\n")
    input("Faite sur entrer quand vous êtes près: ")