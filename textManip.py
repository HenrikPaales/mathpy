fileA = 'est5word.txt'
fileB = 'com5word.txt'
fileC = 'resultA.txt'

def filterLength(listName, wordLen):
    resultList = []
    for i in listName:
        if len(i) == int(wordLen):
            resultList += i
    return resultList
def linesToList(fileName):
    linesF = []
    fileT = open(fileName, 'r')
    linesT = fileT.readlines()
    for line in linesT:
        linesF += [line.strip()]
    fileT.close()
    return linesF
def commonLines(listSmaller, listLarger):
    listCommon = []
    for i in listSmaller:
        if i in listLarger:
            listCommon += [i]
    return listCommon
def listToFile(fileName, listName):
    file1 = open(fileName, 'w')
    for i in listName:
        file1.writelines([i])
        file1.writelines("\n")
    file1.close()

def addCom(listName):
    summedList = []
    for i in listName:
        summedList += [i + ".com"]
    return summedList

# listToFile(fileC, commonLines(linesToList(fileA), linesToList(fileB)))
listToFile(fileC, addCom(linesToList(fileA)))