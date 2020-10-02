import os
import requests
import json
from Commands.Clear import Clear

def SwitchGet():

    RepoApps = "https://switchbru.com/appstore/repo.json"
    RepoPoyoTheme = "https://raw.githubusercontent.com/Bakassable/PoyoTools/master/PoyoTools%20DB/themes.json"

    Lettre = [
        "a",
        "b",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

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


    r = requests.get(RepoApps)
    with open("repo.json", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
            
    r = requests.get(RepoPoyoTheme)
    with open("themes.json", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


    with open("repo.json", "r") as file:
        DBUse = json.load(file)#ouverture de la DB
        file.close

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
    FilDirUse = []
    URL = []
    NameUse = []
    AuthorUse = []
    def GitAdd():
        FileSplit = ["", Recherche]
        print(FileSplit)
        FileSplit[0] = "https://api.github.com/repos/"
        FileSplit.append("/releases/latest")
        FileSplit = (f"{FileSplit[0]}{FileSplit[1]}{FileSplit[2]}")
        
        r = requests.get(FileSplit)
        with open("latest.json", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)

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

       
    DBNameSave = []
    AuthorSave = []
    NameIsDB = []
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
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        FileDownload.append(f"https://switchbru.com/appstore/zips/{DBName}.zip")
                        DBNameSave.append(DBName)
                        AuthorSave.append(Author)
                        FilDirUse.append("\\")
                        NameIsDB.append("AppsStore")
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
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        FileDownload.append(f"https://switchbru.com/appstore/zips/{DBName}.zip")
                        DBNameSave.append(DBName)
                        AuthorSave.append(Author)
                        FilDirUse.append("\\")
                        NameIsDB.append("AppsStore")
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
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        FileDownload.append(f"https://switchbru.com/appstore/zips/{DBName}.zip")
                        DBNameSave.append(DBName)
                        AuthorSave.append(Author)
                        FilDirUse.append("\\")
                        NameIsDB.append("AppsStore")
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
                        DBName = DBUse["packages"][val]["name"]
                        Author = DBUse["packages"][val]["author"]
                        FileDownload.append(f"https://switchbru.com/appstore/zips/{DBName}.zip")
                        DBNameSave.append(DBName)
                        AuthorSave.append(Author)
                        FilDirUse.append("\\")
                        NameIsDB.append("AppsStore")
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
                            DBNameSave.append(DBName)
                            AuthorSave.append(Author)
                            NameIsDB.append("ThemePoyo")
                            if val2 < 10:
                                print(f" [{val2}]  ThemePoyo {DBName} By {Author}")
                            else:
                                print(f" [{val2}] ThemePoyo {DBName} By {Author}")
                            val2 += 1
                            skyp = False
                            FilDir.append("Theme")
                            FilDirUse.append("\\ulaunch\\themes\\")
                except KeyError:
                    skyp = True
                try:
                    if Author.lower().startswith(Recherche) or Author.lower().endswith(Recherche):
                        if skyp == True:
                            FileDownload.append(DBPoyoTheme[val]["download"])
                            DBName = DBPoyoTheme[val]["name"]
                            DBNameSave.append(DBName)
                            AuthorSave.append(Author)
                            NameIsDB.append("ThemePoyo")
                            if val2 < 10:
                                print(f" [{val2}]  ThemePoyo {DBName} By {Author}")
                            else:
                                print(f" [{val2}] ThmemPoyo {DBName} By {Author}")
                            val2 += 1
                            skyp = False
                            skyp2 = False
                            FilDir.append("Theme")
                            FilDirUse.append("\\ulaunch\\themes\\")
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

    while Recherche != 300:
        try:
            try:
                val3 = 0
                val2 = 0
                val = 15
                Clear()
                for i in DBNameSave:
                    if val2 < 10:
                        print(f" [{val2}]  {NameIsDB[val2]} {DBNameSave[val2]} By {AuthorSave[val2]}")
                    else:
                        print(f" [{val2}] {NameIsDB[val2]} {DBNameSave[val2]} By {AuthorSave[val2]}")
                    val2 += 1
                    val3 +=1

                for DL in FileDownload:
                    val -= 1

                if val == 15:
                    print(" Aucun résultat trouvé.")
                    val -= 1
                while val != 0:
                    print("")
                    val -=1

                print("\n (Q) Quiter\n")
                RepDL = input("Entrer votre demande: ")
                try:
                    IntRepDL = int(RepDL)
                except ValueError:
                    pass

                try:
                    if RepDL == "q" or RepDL == "Q":
                        break
                    elif IntRepDL < val3:
                        os.system(f'Data\\Wget\\wget.exe "{FileDownload[IntRepDL]}"')
    
                        path = '.'
                        
                        files = os.listdir(path)
                        for name in files:
                            if name.endswith(".zip"):
                                Rename = name

                            elif name.endswith(".zip@raw=true"):
                                Rename = name.replace('@raw=true','',1)
                                os.system(f'ren "{name}" "{Rename}"')

                        for L in Lettre:
                            if os.path.exists(f"{L}:\\switch"):
                                CopyPath = (f"{L}:")
                                
                        os.system(f'move "{Rename}" "{CopyPath}{FilDirUse[IntRepDL]}{Rename}"')
                        os.system(f'Data\\7Zip\\7Zip.exe x "{CopyPath}{FilDirUse[IntRepDL]}{Rename}" -o"{CopyPath}{FilDirUse[IntRepDL]}" -y')
                        os.system(f'del "{CopyPath}{FilDirUse[IntRepDL]}{Rename}"')
    
                        path = (f"{CopyPath}{FilDirUse[IntRepDL]}")
                        files = os.listdir(path)
                        for name in files:
                            if name.endswith(".install"):
                                os.system(f"del {path}{name}")
                            if name.endswith(".exe"):
                                os.system(f"del {path}{name}")
                            if name.endswith(".nsp"):
                                if not os.path.exists(f"{CopyPath}\\NSP"):
                                    os.system(f'mkdir "{CopyPath}\\NSP"')
                                os.system(f'move {path}{name} {CopyPath}\\NSP')
                            if name.endswith(".nro") and name != "hbmenu.nro":
                                os.system(f'move {path}{name} {CopyPath}\\switch')
                            if name.startswith("info"):
                                os.system(f"del {path}{name}")
                            if name.startswith("readme"):
                                os.system(f"del {path}{name}")
                            if name.startswith("screen"):
                                os.system(f"del {path}{name}")
                    
                except UnboundLocalError:
                    pass
                
                skyp = False
            except KeyError:
                skyp = True
        
        except IndexError:
            skyp = True