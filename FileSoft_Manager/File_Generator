import os
import sys, glob, shutil, pathlib

import random
import string

num_of_file = 25
num_of_folder = 5


def random_name(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


for file_num in range(num_of_file):
    test_file = open("{}_{}.txt".format(random_name(10), file_num), "w")
    test_file.write(r"/*   {}   */".format(random_name(7)))
    test_file.close()
