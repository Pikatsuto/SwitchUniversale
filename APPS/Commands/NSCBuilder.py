import os
from sys import platform as _platform
from Commands.Clear import Clear
Path = os.getcwd()

def NSCBuilder():# Menu [(1) NSC Builder]
    NSCBuiler = (f"{Path}\\Data\\NSCBuilder\\NSCB.bat")
    os.system(NSCBuiler)