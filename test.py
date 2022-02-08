import requests
import json
import os

release_url = "https://api.github.com/repos/Noice75/Temp/releases/latest"
version = ""

def Update():
    try:
        os.remove("Lol.py")
    except:
        pass
    r = requests.get("https://raw.githubusercontent.com/Noice75/Temp/main/Lol.py")
    f = open("Lol.py", "w")
    f.write(r.text)
    f.close()
    os.system("attrib +h " + "Lol.py")
    print("Lol")

def Refresh():
    try:
        os.remove("Lol.py")
    except:
        pass
    r = requests.get("https://raw.githubusercontent.com/Noice75/Temp/main/Lol.py")
    f = open("Lol.py", "w")
    f.write(r.text)
    f.close()
    os.system("attrib +h " + "Lol.py")

def Write_Version(a):
    global version
    try:
        os.remove("version.json")
    except:
        pass

    with open('version.json', 'w') as f:
        json.dump(a.json(), f)
        version = a.json()["tag_name"]
        os.system("attrib +h " + "version.json")

def Read_Version():
    global version
    with open('version.json', 'r') as f:
        j = json.load(f)
        version = j["tag_name"]
        os.system("attrib +h " + "version.json")

try:
    a = requests.get(release_url)
except:
    print("Connect to the network!")
    quit()

try:
    Read_Version()
except:
    Write_Version(a)
    Update()

if (a.json()["tag_name"] != version):
    Write_Version(a)
    Update()
else:
    print(version)
    Refresh()
