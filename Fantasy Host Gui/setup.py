import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Fantasy Raider",
        version = "1.0",
        description = "Fantasy Football but for Classic WoW Raiding",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Host GUI.py", base=base, targetName="Fantasy Raider.exe", icon="imgs/fr_icon.ico")])