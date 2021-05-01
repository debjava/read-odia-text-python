'''
This python file performs the following operations.
1. It reads the file line by line
2. From each line , it reads the words
3. Each word is verified whether it is a Non English word or not.
4. Extracts all the Non English words
5. Stores all the Non English words in a list
6. Process the list item and remove further English words
7. Finally prints all the Non English words separated by commas
'''
import os
import re

DATA_FILE_NAME = "Vocabulary.txt"

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def processList(wordslist):
    processedItems = []
    for item in wordslist:
        replacedValue = item.replace(",", " ").replace(",", "").replace("(", "").replace(")", "")
        processstr = re.sub("[!a-zA-Z]", "", replacedValue)
        processedItems.append(processstr)
    items_comma = ",".join(processedItems)
    print(items_comma)
    # for value in processedItems:
    #     print(value)


def extractNonEnglish():
    nonenglishwords = []
    parent = os.path.dirname(os.getcwd())
    txt_file_path = os.path.join(parent, "data", DATA_FILE_NAME)
    f = open(txt_file_path, "r", encoding="utf-8")
    for line in f:
        s = ""
        # print("Line: ", line)
        for word in line.split():
            if not (isEnglish(word)):
                s += " "+word
        if not len(s) == 0:
            # print(s)
            nonenglishwords.append(s)
    processList(nonenglishwords)

if __name__ == "__main__":
    extractNonEnglish()

