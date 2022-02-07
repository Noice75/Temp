import os

def Lol():
    f = open("Lol.txt", "w")
    f.write("Yoo")
    os.system("attrib +h " + "Lol.txt")
