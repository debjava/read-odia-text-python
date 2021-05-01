import os
import random

DATA_FILE_NAME = "odia-hindi.txt"


def randomizewords():
    # read the file
    parent = os.path.dirname(os.getcwd())
    txt_file_path = os.path.join(parent, "data", DATA_FILE_NAME)
    f = open(txt_file_path, "r", encoding="utf-8")
    values = f.read().split(",")
    random.shuffle(values)
    joined_words = ",".join(values)
    print(joined_words)


if __name__ == "__main__":
    randomizewords()
