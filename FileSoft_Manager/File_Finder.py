import os
from pathlib import Path
import re

Output_path = r"OUTPUT_PATH"
Search_path = r"SEARCH_PATH"

folder = []


# .c/.hファイルを探してリスト型データにする
def file_finder(_path):
    temp = Path(_path)
    file_list = [p for p in temp.glob("**/*") if re.search(".(c|h)", str(p))]
    # .c /.h以外のファイルも取り込んでいる。要改善
    for path in file_list:
        if not os.path.isdir(path):
            folder.append(path)

    return folder


# リストから全ファイルを開き、1行目だけを抜き出して閉じる。辞書型にして{相対path:"1行目"}となるようにする
def file_read(*folder_list):
    read_data = {}
    for j in folder_list:
        if os.path.isdir(j):
            os.chdir(j)
        else:
            with open(j, "r", encoding="utf8") as f:
                read_data[str(j)] = f.readline()
            f.close()
    return read_data


# 一つのテキストファイルとして出力する
def file_list_generator(**dictionary):
    os.chdir(Output_path)
    with open("soft_list.txt", "w") as f:
        for k, i in dictionary.items():
            temp = str(i).replace("/* ", "")
            temp = temp.replace(" */", "")
            f.write("{}  : {}\n".format(k, temp))

    f.close()


def main():
    file_list = file_finder(Search_path)
    file_dict = file_read(*file_list)
    file_list_generator(**file_dict)


main()
