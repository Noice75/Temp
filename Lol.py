import os

try:
    os.remove("Lol.txt")
except:
    pass
f = open("Lol.txt", "w")
f.write("Yoo")
os.system("attrib +h " + "Lol.txt")
print("Done")
