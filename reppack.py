import os
import urllib.request as internet
import distutils.spawn
import sys
import platform


def is_tool(name):
    return distutils.spawn.find_executable(name) is not None
def connected(url = "https://google.com", timeout = 3):
    try:
        internet.urlopen(url, timeout=timeout)
        return True
    except:
        return False


# basic setup and checking
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")
if not os.path.exists(os.path.expanduser("~") + "/Ccode"):
    raise OSError("Ccode language is not installed!")
if not is_tool("git"):
    raise OSError("Git is not installed")
if not os.path.exists("pack-list"):
    os.system("git clone --depth 1 -q https://github.com/Ccode-lang/pack-list")
if not connected():
    raise OSError("No internet connection")

packfile = open("pack-list/list.txt")
packs = packfile.readlines()
packfile.close()


def help():
    print("python reppack.py <package name>")
    print("python reppack.py remove <package to remove>")
    print("python reppack.py refresh")
    print("\n\nFor more info go to https://github.com/Ccode-lang/Ccode/wiki/package-manager")
    quit()



if len(sys.argv) < 2:
    help()
installed = False
for pack in packs:
    if sys.argv[1] == "remove" or sys.argv[1] == "refresh":
        installed = True
        break
    #data reader
    pack_ = pack.strip()
    pack = pack.strip().split("^")
    if pack_ == "" or pack_.startswith("$"):
        # comments
        continue
    elif pack[0].strip() == sys.argv[1]:
        os.chdir(os.path.expanduser("~") + "/Ccode/lib")
        if os.path.exists(sys.argv[1]):
            installed = True
            print("Already installed!")
            break
        os.system("git clone --depth 1 -q " + pack[1].strip())
        print("Package installed!")
        installed = True
        break

if not installed:
    print("Package not found!")

if sys.argv[1] == "refresh":
    os.chdir("pack-list")
    os.system("git pull -q")
    os.chdir("..")

if sys.argv[1] == "remove":
    os.chdir(os.path.expanduser("~") + "/Ccode/lib")
    if os.path.exists(sys.argv[2]):
        os.system("rm -rf " + sys.argv[2])
        print("Removed")
    else:
        print("Package not found!")
