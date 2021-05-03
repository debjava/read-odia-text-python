import os
import re

DATA_FILE_NAME = "Vocabulary.txt"

def extractWords():
    parent = os.path.dirname(os.getcwd())
    txt_file_path = os.path.join(parent, "data", DATA_FILE_NAME)
    f = open(txt_file_path, "r", encoding="utf-8")
    file_data = f.read()
    regex_pattern = r"(\w+(?: \w+)*):"
    matches = re.findall(regex_pattern, file_data, re.MULTILINE)
    list1 = list(filter(lambda a: (a != "Similar") , matches))
    list2 = list(filter(lambda a: (a != "Synonyms") , list1))
    onelinestr = ",".join(list2)
    print(onelinestr)


if __name__ == "__main__":
    extractWords()