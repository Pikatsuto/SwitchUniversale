import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def SDFlacher():
    AndriodImg128 = "https://download.switchroot.org/android/android-128gb.img.gz"
    AndriodImg64 = "https://download.switchroot.org/android/android-64gb.img.gz"
    AndriodImg32 = "https://download.switchroot.org/android/android-32gb.img.gz"
    AndriodImg16 = "https://download.switchroot.org/android/android-16gb.img.gz"
    AndriodShieldifier = "https://download.switchroot.org/android/shieldifier.zip"
    AndriodJoyconFix = "https://download.switchroot.org/android/extras/fix-joycon.zip"
    AndriodRebootToPayload = "http://download1589.mediafire.com/nbjar3f2saug/nyzak7fjje60g9s/reboot2payload.zip"
    Hekate = "https://github.com/CTCaer/hekate/releases/download/v5.2.1/hekate_ctcaer_5.2.1_Nyx_0.9.1.zip"
    OpenGapps = "http://download1336.mediafire.com/sbzfritue1qg/gj0do49j5b9lw3h/open_gapps-arm64-8.1-nano-20200610.zip"
    Ubuntu = "https://download.switchroot.org/ubuntu/switchroot-l4t-ubuntu-3.0.0-lite-2020-03-02.img.gz"

    ChoisAndroidFull = ""

    while ChoisAndroidFull != "q":
        Clear()

        AndroidChoisImg = ""
        ChoisListe = ["1", "2", "3", "4", "5", "q"]

        while AndroidChoisImg not in ChoisListe:
            print(" Quelle image d'Android voulez-vous ?\n")
            print(f" (1) 128 GB\n (2) 64 GB\n (3) 32 GB\n (4) 16 GB\n (5) Ou souhaitez-vous Ubuntu Lite\n\n\n\n\n\n\n\n\n\n (Q) Quitter\n")
            AndroidChoisImg = input("Que choisissez-vous: ")
            AndroidChoisImg == AndroidChoisImg.lower()

        if AndroidChoisImg == "q":
            ChoisAndroidFull = "q"
            break

        Leter = ["A", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        AndroidDrive = ""
        while AndroidDrive not in Leter:
            Clear()
            print(" Êtes-vous sûr de vouloir le faire ? Votre périphérique sera formaté !\n Entrez la lettre de votre SD si vous avez plusieurs partitions il faudra la formater au préalable.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n (Q) Quiter\n")
            AndroidDrive = input("Que choisissez vous: ")
            AndroidDrive = AndroidDrive.upper()
        
        if AndroidDrive == "q":
            ChoisAndroidFull = "q"
            break

        if AndroidChoisImg == "1":
            AndroidChoisImgGZ = "android-128gb.img.gz"
            AndroidChoisImg = "android-128gb.img"
            AndriodDL = AndriodImg128
        elif AndroidChoisImg == "2":
            AndroidChoisImgGZ = "android-64gb.img.gz"
            AndroidChoisImg = "android-64gb.img"
            AndriodDL = AndriodImg64
        elif AndroidChoisImg == "3":
            AndroidChoisImgGZ = "android-32gb.img.gz"
            AndroidChoisImg = "android-32gb.img"
            AndriodDL = AndriodImg32
        elif AndroidChoisImg == "4":
            AndroidChoisImgGZ = "android-16gb.img.gz"
            AndroidChoisImg = "android-16gb.img"
            AndriodDL = AndriodImg16
        elif AndroidChoisImg == "5":
            AndroidChoisImgGZ = "switchroot-l4t-ubuntu-3.0.0-lite-2020-03-02.img.gz"
            AndroidChoisImg = "switchroot-l4t-ubuntu-3.0.0-lite-2020-03-02.img"
            AndriodDL = Ubuntu

        if AndroidDrive != "c" and AndroidDrive != "C":

            os.system(f'Data\\Wget\\wget.exe "{AndriodDL}"')

            os.system(f'Data\\7Zip\\7Zip.exe e "{AndroidChoisImgGZ}" -y')
            os.system(f'del {AndroidChoisImgGZ}')
            os.system(f'Data\\SDFlach\\CommandLineDiskImager.exe {AndroidChoisImg} {AndroidDrive}')
            os.system(f'del {AndroidChoisImg}')

            SdValide = False
            for l in Leter:
                if os.path.exists(f"{l}:/switchroot_android"):
                    AndroidDrive = l
                    SdValide = True
                    break
            
            if SdValide== True:
                os.system(f'Data\\Wget\\wget.exe "{Hekate}"')
                os.system(f'Data\\Wget\\wget.exe "{AndriodJoyconFix}"')
                os.system(f'Data\\Wget\\wget.exe "{AndriodRebootToPayload}"')
                os.system(f'Data\\Wget\\wget.exe "{AndriodShieldifier}"')
                os.system(f'Data\\Wget\\wget.exe "{OpenGapps}"')

                os.system(f'move "hekate_ctcaer_5.2.1_Nyx_0.9.1.zip" "{AndroidDrive}:/hekate_ctcaer_5.2.1_Nyx_0.9.1.zip"')
                os.system(f'Data\\7Zip\\7Zip.exe x "{AndroidDrive}:/hekate_ctcaer_5.2.1_Nyx_0.9.1.zip" -o{AndroidDrive}:/ -y')
                os.system(f'del "{AndroidDrive}:/hekate_ctcaer_5.2.1_Nyx_0.9.1.zip"')
                os.system(f'mkdir "{AndroidDrive}:/ZIP_TWRP_A_Flacher"')
                os.system(f'move "reboot2payload.zip" "{AndroidDrive}:/ZIP_TWRP_A_Flacher/reboot2payload.zip"')
                os.system(f'move "shieldifier.zip" "{AndroidDrive}:/ZIP_TWRP_A_Flacher/shieldifier.zip"')
                os.system(f'move "fix-joycon.zip" "{AndroidDrive}:/ZIP_TWRP_A_Flacher/fix-joycon.zip"')
                os.system(f'move "open_gapps-arm64-8.1-nano-20200610.zip" "{AndroidDrive}:/ZIP_TWRP_A_Flacher/open_gapps-arm64-8.1-nano-20200610.zip"')
                os.system('del "s!AtgMAK7Yw9dYgd9hd8LiSvu-Vz042Q@e=sNSvy1"')
        
        os.system('COLOR 60')
