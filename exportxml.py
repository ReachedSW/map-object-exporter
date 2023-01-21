from bs4 import BeautifulSoup as bs
constData = "" # enter your xml file path here

def MakeUnique(s):
    return s[len(constData):]

buildingFiles = set()
fileNames = set()
treeFiles = set()
effectFiles = set()


def getpropertylist(propertys : list):
    with open('property.xml', 'r') as f:
        data = f.read()

    bData = bs(data, 'xml')
    b_unique = bData.find_all('Property')

    for key in b_unique:
        if key.has_attr('crc'):
            if key['crc'] in propertys:
                if key.has_attr('buildingfile'):
                    buildingFiles.add(key['buildingfile'])
                
                if key.has_attr('filename'):
                    fileNames.add(key['filename'])
                
                if key.has_attr('treefile'):
                    treeFiles.add(key['treefile'])
                
                if key.has_attr('effectfile'):
                    effectFiles.add(key['effectfile'])

    with open('buildingFiles.txt', 'w') as f:
        for data in buildingFiles:
            f.write(data + "\n")
    
    with open('fileNames.txt', 'w') as f:
        for data in fileNames:
            f.write(MakeUnique(data) + "\n")
    
    with open('treeFiles.txt', 'w') as f:
        for data in treeFiles:
            f.write(data + "\n")
    
    with open('effectFiles.txt', 'w') as f:
        for data in effectFiles:
            f.write(data + "\n")
    
