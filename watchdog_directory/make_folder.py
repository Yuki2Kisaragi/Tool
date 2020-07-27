import os
from datetime import datetime
import shutil

target_dir = "source/target/stack"
destination_dir = "source/target/backup"
fmt = "%Y%m%d_shrimp"


def copy_folder(file):
    t = datetime.now()
    folder_name = t.strftime(fmt)
    os.chdir(destination_dir)

    if not os.path.exists(folder_name):
        os.makedir(folder_name)
        shutil.move(file, destination_dir)
        # print(folder_name)

    else:
        shutil.move(file, destination_dir)

        pass

    os.chdir(target_dir)


while True:
    # with os.listdir as f:
    #
    # copy_folder()
    pass
