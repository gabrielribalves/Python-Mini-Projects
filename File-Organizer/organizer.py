import os

def getListFile(folderPath:str):
    for file in os.listdir(folderPath):
        if os.path.isfile(os.path.join(folderPath, file)):
            yield file

def changeDir(folderName:str)-> None:
    path = os.curdir
    folderPath = os.path.join(path, folderName)
    listFiles = getListFile(folderPath)
    for file in listFiles:
        extention = file.split(".")[-1]
        print(os.path.join(folderPath, extention, file))
        if os.path.exists(os.path.join(folderPath, extention)):
            os.rename(os.path.join(folderPath, file), os.path.join(folderPath, extention , file))
        else:
            os.mkdir(os.path.join(folderPath, extention))
            os.rename(os.path.join(folderPath, file), os.path.join(folderPath, extention , file))



changeDir("Test Folder-copy")

# print(os.path.isfile("./Test Folder/app.js"))
