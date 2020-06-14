import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def Credits():
    Quite = ""
    while Quite != "q":
        Clear()
        print("   --( ° Inspiration ° )--\n")

        print("      IcosaSwitch :           https://github.com/IcosaSwitch/IcosaSwitch")
        print("      SwitchTools :           https://github.com/THZoria/switchtools\n")

        print("   --( ° Utilisation ° )--\n")

        print("      7ZIP :                  https://www.7-zip.org/")
        print("      Wget :                  https://eternallybored.org/misc/wget/")
        print("      CommandLineDiskImager : https://github.com/davidferguson/CommandLineDiskImager")
        print("      LanPlay :               https://github.com/spacemeowx2/switch-lan-play")
        print("      SysDVR :                https://github.com/exelix11/SysDVR")
        print("      NSC Builder :           https://github.com/julesontheroad/NSC_BUILDER")
        print("      NSZ :                   https://github.com/nicoboss/nsz")
        print("      TegraRCM :              https://github.com/eliboa/TegraRcmGUI")
        print("      Zadig :                 https://zadig.akeo.ie/")
        print("      HomeBrew AppsStore :    https://apps.fortheusers.org/switch")
        print("      PoyoTools :             https://github.com/Murasaki64/PoyoTools")

        Quite = input("(Q) Quitter quand vous voulez quitter: ")
        Quite = Quite.lower()
