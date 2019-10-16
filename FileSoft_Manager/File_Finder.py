import os
from pathlib import Path
from pprint import pprint
import re

Output_path = r"OUTPUT_PATH"
Search_path = r"SEARCH_PATH"

folder = []


# TO DO .c,.hファイルを探してリスト型データにする
def file_finder(_path):
    os.chdir(_path)
    temp = Path(_path)
    file_list = [p for p in temp.glob("**/*") if re.search(".(c|h)", str(p))]

    for path in file_list:
        if not os.path.isdir(path):
            folder.append(os.path.relpath(path, Search_path))
    return folder


# TO DO  リストから全ファイルを開き、1行目だけを抜き出して閉じる。辞書型にして{相対path:"1行目"}となるようにする
def file_read(*folder_list):
    read_data = {}
    for j in folder_list:

        if os.path.isdir(j):
            with open(j, "r") as f:
                read_data[j] = f.readline()
            f.close()
        else:
            with open(j, "r") as f:
                read_data[j] = f.readline()
            f.close()
    return read_data


a = file_finder(Search_path)
pprint(a)
b = file_read(*a)
pprint(b)

# TO DO  一つのテキストファイルとして出力する

