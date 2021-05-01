'''
Created on Apr 21, 2021

@author: debad
'''
import os

from appdirs import unicode

# from click.types import Path
# import codecs

ODIA_FILE_NAME = "some-odia-text.txt"


def showCurrentDirectory():
    currentDirectory = os.getcwd()
    print("Current Directory: ", currentDirectory)

    ''' Show Parent and Grand Parent '''
    parent = os.path.dirname(currentDirectory)
    print("Parent Directory: ", parent)

    grandParent = os.path.dirname(parent)
    print("Grand Parent Directory: ", grandParent)
    dataDir = os.path.join(parent, "data")
    print("Data Directory: ", dataDir)
    odiatxtpath = os.path.join(dataDir, ODIA_FILE_NAME)
    print("Odia File Path: ", odiatxtpath)
    if (os.path.exists(odiatxtpath)):
        print("File exists ...")


def readFileFromDir():
    # showCurrentDirectory()
    parent = os.path.dirname(os.getcwd())
    odiaTxtFilePath = os.path.join(parent, "data", ODIA_FILE_NAME)
    print("Odia File Path: ", odiaTxtFilePath)
    # f = open(odiaTxtFilePath, "r", encoding="utf8")
    f = open(odiaTxtFilePath, "r", encoding="utf-8")
    # f = codecs.open(odiaTxtFilePath,"r",encoding='utf-8')
    print(f.read())

    # f = open(odiaTxtFilePath,'r')
    # for line in f:
    #     l = unicode(line, encoding='utf-8')# decode the input
    #     print(l.encode('utf-8')) # encode the output
    # f.close()

def readWordByWord():
    parent = os.path.dirname(os.getcwd())
    odiaTxtFilePath = os.path.join(parent, "data", ODIA_FILE_NAME)
    f = open(odiaTxtFilePath, "r", encoding="utf-8")
    for line in f:
        for word in line.split():
            print(word)


if __name__ == '__main__':
    # readFileFromDir()
    readWordByWord()
