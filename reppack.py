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
    os.system("git clone --depth 1 -q https://github.com/Ccode-lang/pack-list")

packfile = open("pack-list/list.txt")
packs = packfile.readlines()
packfile.close()


def help():
    print("python reppack.py <package name>")
    print("python reppack.py remove <package to remove>")
    print("\n\nFor more info go to https://github.com/Ccode-lang/Ccode/wiki/package-manager")
    quit()



if len(sys.argv) < 2:
    help()
installed = False
for pack in packs:
    if sys.argv[1] == "remove":
        break
    pack = pack.strip().split("^")
    if pack[0].strip() == sys.argv[1]:
        os.chdir(os.path.expanduser("~") + "/Ccode/lib")
        if os.path.exists(sys.argv[1]):
            installed = True
            print("Already installed!")
        os.system("git clone --depth 1 -q " + pack[1].strip())
        print("Package installed!")
        installed = True
        break

if not installed:
    if not sys.argv[1] == "remove":
        print("Package not found!")

if sys.argv[1] == "remove":
    os.chdir(os.path.expanduser("~") + "/Ccode/lib")
    if os.path.exists(sys.argv[2]):
        os.system("rm -rf " + sys.argv[2])
        print("Removed")
    else:
        print("Package not found!")
