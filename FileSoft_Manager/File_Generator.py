import os
import glob
from pathlib import Path
import random
import string

Output_path = r"C:\Users\MasaH\PycharmProjects\Hello_Python\practice\product\Tool\FileSoft_Manager\Ouput_folder"
Search_path = r"C:\Users\MasaH\PycharmProjects\Hello_Python\practice\product\Tool\FileSoft_Manager\Search_folder"
num_of_file = 25
num_of_folder = 5


def random_name(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def folder_generator(*num_folders):
    for num in range(num_folders):
        os.makedirs("{}_{}".format(num, random_name(8)))


def file_generator(num_files):
    for num in range(num_files):
        test_file = open("{}.c".format(random_name(10)), "w")
        test_file.write(r"/*   {}   */".format(random_name(10)))
        test_file.close()


def txt_to_c_convert(search_path):
    # ．txt=>.cファイルに変換
    # txt_to_c_convert(Output_path)
    txt_list = list(glob.glob("*.txt", recursive=True))
    for txt in txt_list:
        file_name, ext = os.path.splitext(txt)
        temp_txt = Path(txt)
        c_file = temp_txt.rename(file_name + ".c")
        print(c_file)

def random_file_generator(directory_path):
    folder = []

    def random_generator(*folder_list):
        for j in folder_list:
            os.chdir(j)
            for k in range(random.randint(1, 5)):
                test_file = open("{}.c".format(random_name(10)), "w")
                test_file.write(r"/*   {}   */".format(random_name(10)))
                test_file.close()
        os.chdir(Output_path)

    p = Path(Output_path)
    directory_list = list(p.glob("*"))
    for path in directory_list:
        if os.path.isdir(path):
            folder.append(path)
            print(path)

    random.shuffle(folder)
    random_generator(*folder)

###### main ####
os.chdir(Output_path)
# ディレクトリ移動
random_file_generator(Output_path)
