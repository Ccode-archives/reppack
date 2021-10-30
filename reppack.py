import os
import platform
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")
if not os.path.exists(os.path.expanduser("~") + "/Ccode"):
    raise OSError("Ccode language is not installed!")
if not os.path.exists("pack-list"):
    os.system("git clone -q https://github.com/Ccode-lang/pack-list")
