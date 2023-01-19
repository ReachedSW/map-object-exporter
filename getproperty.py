import os, re
import exportxml

mapname = input("Enter map name: ")

try:
    os.listdir(mapname)
except FileNotFoundError:
    print("Map name is not exist")
    exit()

map_places = []
for folder in os.listdir(mapname):
    if folder.startswith("0"):
        map_places.append(folder)

def convert_indentations_to_tabs(file_path, tab_size=4):
    with open(file_path, 'r') as f:
        content = f.read()
    
    spaces_regex = r' {'+str(tab_size)+ r'}' 
    content = re.sub(spaces_regex, '\t', content)

    with open(file_path, 'w') as f:
        f.write(content)

def readfile():
    ret = set()
    for part in map_places:
        with open(mapname + "/" + part + "/" + "areadata.txt") as f:
            bFounded = False
            iCounter = 0
            for line in f:
                if bFounded:
                    if line.startswith("End"):
                        bFounded = False
                        iCounter = 0
                        continue
                    iCounter += 1
                    if iCounter == 2:
                        ret.add(line)
                    else:
                        continue

                if line.startswith("Start"):
                    bFounded = True
    return ret

def writeFile():
    with open("output.txt", "w") as f:
        for crc in readfile():
            f.write(crc)

def makePretty():
    retArr = []
    with open("output.txt", "r") as f:
        for line in f:
            retArr.append(line.split("\t")[1].replace("\n", ""))
    
    return retArr

writeFile()
convert_indentations_to_tabs("output.txt")
makePretty()
exportxml.getpropertylist(makePretty())

