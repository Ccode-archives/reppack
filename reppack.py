import os
import sys
import platform
# basic setup and checking
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")
if not os.path.exists(os.path.expanduser("~") + "/Ccode"):
    raise OSError("Ccode language is not installed!")
if not os.path.exists("pack-list"):
    os.system("git clone -q https://github.com/Ccode-lang/pack-list")

packfile = open("list.txt")
packs = packfile.readlines()
packfile.close()


def help():
    print("python reppack.py <package name>")
    quit()



if len(sys.argv) < 1:
    help()
installed = False
for pack in packs:
    pack = pack.strip().split("^")
    if pack[0].strip() == sys.argv[1]:
        os.chdir(os.path.expanduser("~") + "/Ccode/lib")
        os.system("git clone -q " + pack[1].strip())
        print("Package installed!")
        installed = True
        break
if not installed:
    print("package not found!")
