from cx_Freeze import setup, Executable
 
build_exe_options = {"includes": ["sys", "os", "requests", "json"]}

target = Executable(
    script="start.py",
    icon="SwitchUniversale.ico",
    targetName="SwitchUniversale"
    )

setup(
    name = "SwitchUniversale_1.0.0_Beta",
    version = "1.0.0",
    description = "Script universel pour la Switch", 
    options = {"build_exe": build_exe_options},
    executables = [target],
)