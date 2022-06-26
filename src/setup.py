import sys
from cx_Freeze import setup, Executable
from pathlib import Path

# src_path = Path("./src/")
#
# src_files = [str(path) for path in src_path.iterdir() if path.is_file()]

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["pygame", "pathlib", "os"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PIXELJUMP",
    version="0.1",
    description="PIXELJUMP",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", target_name="pixeljump.exe", base=base)],
)
