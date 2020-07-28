from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
from datetime import datetime
# TODO Watchdogの学習


class ChangeHandler(FileSystemEventHandler):

    # すべてのイベント
    def on_any_event(self, event):
        pass
        # print('[全て]', event)

    # 作成された時のイベント
    def on_created(self, event):
        time.sleep(5)
        # 2回ログを出力されるのを防ぐ

        event_time_stamp = datetime.now()
        print("{} {}".format("[作成]", event_time_stamp.strftime('%Y/%m/%d %H:%M:%S')), event)

    # 変更されたときのイベント
    def on_modified(self, event):

        event_time_stamp = datetime.now()
        print("{} {}".format('[変更]', event_time_stamp.strftime('%Y/%m/%d %H:%M:%S')), event)

    # 削除された時のイベント
    def on_deleted(self, event):

        event_time_stamp = datetime.now()
        print("{} {}".format("[削除]", event_time_stamp.strftime('%Y/%m/%d %H:%M:%S')), event)

    # 移動した時のイベント
    def on_moved(self, event):

        event_time_stamp = datetime.now()
        print("{} {}".format("[移動]", event_time_stamp.strftime('%Y/%m/%d %H:%M:%S')), event)


if __name__ == "__main__":

    observer = Observer()

    # 監視するフォルダを第２引数に指定
    observer.schedule(ChangeHandler(), '../Target', recursive=True)

    # 監視を開始する
    observer.start()
    print("Start")

    while True:
        time.sleep(5)
