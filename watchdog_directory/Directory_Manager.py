import os
from hurry.filesize import size, alternative
import time
import tkinter
from datetime import datetime

target_dir = "../Target"


class DirectoryManager:
    def __init__(self):
        self.dir_limit = 5000000
        self.alert_size = int(self.dir_limit * 0.5)
        self.total = 0

    def get_dir_size(self, path):
        """
        :argument:
            Target Directory path
        :return:
           Target Directory Size

        :other:
            シンボリックリンクのサイズを見ない場合は
            is_file(), is_dir()の引数follow_symlinksをFalse

            "hurry.filesize"
                https://pypi.org/project/hurry.filesize/#description

        """
        self.total = 0

        with os.scandir(path) as folder:
            for entry in folder:
                if entry.is_file():
                    self.total += entry.stat().st_size
                elif entry.is_dir():
                    self.total += self.get_dir_size(entry.path)

        return self.total

    def capacity_monitor(self, path):
        time_stamp = datetime.now()
        dir_space = self.get_dir_size(path)

        if dir_space >= self.alert_size:
            print("Directory '{}' is reaching limit space. Please confirm its data space".format(path))
            # TODO  sizeが50%超えた時の警告表示 -> Done
            # TODO  tkinterによるGUI表示

        print("Time:{} Size:{}".format(time_stamp.strftime('%Y/%m/%d %H:%M:%S'),
                                       size(self.get_dir_size(target_dir), alternative)))

        return 0

    # def change_handler(self, path):
    #     pass


if __name__ == "__main__":

    print("Start")
    target = DirectoryManager()

    while True:
        time.sleep(5)
        target.capacity_monitor(target_dir)
