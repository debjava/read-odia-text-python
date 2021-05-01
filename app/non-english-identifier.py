import os

ODIA_FILE_NAME = "Vocabulary.txt"


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def identifyNonEnglishWords():
    nonEnglishWords = []
    parent = os.path.dirname(os.getcwd())
    odiaTxtFilePath = os.path.join(parent, "data", ODIA_FILE_NAME)
    f = open(odiaTxtFilePath, "r", encoding="utf-8")
    for line in f:
        s = ""
        for word in s.split():
            if not (isEnglish(word)):
                s += word
        print(s)
        print("-------------------")
        #         if not (isEnglish(word)):
        # for word in line.split():
        #     # print(word)
        #     if (isEnglish(word)):
        #         pass
        #     else:
        #         # print(word)
        #         # append to list
        #         s += word
        #         # nonEnglishWords.append(s)
        #         # nonEnglishWords.append(word)
        #     nonEnglishWords.append(s)
    print("Total No of words: ", len(nonEnglishWords))
    for w in nonEnglishWords:
        print(w)
        print("-----------")


if __name__ == '__main__':
    identifyNonEnglishWords()
