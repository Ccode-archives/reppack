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

packfile = open("pack-list/list.txt")
packs = packfile.readlines()
packfile.close()


def help():
    print("python reppack.py <package name>")
    quit()



if len(sys.argv) < 1:
    help()
installed = False
for pack in packs:
    if sys.argv[1] == "remove":
        break
    pack = pack.strip().split("^")
    if pack[0].strip() == sys.argv[1]:
        os.chdir(os.path.expanduser("~") + "/Ccode/lib")
        os.system("git clone -q " + pack[1].strip())
        print("Package installed!")
        installed = True
        break
if not installed:
    if not sys.argv[1] == "remove":
        print("package not found!")
if sys.argv[1] == "remove":
    if os.path.exists(sys.argv[2]):
        os.system("rm -rf " + sys.argv[2])
