#! python3
# counter_tool.py
import subprocess
import time


def work_func(work):
    while work > 0:
        time.sleep(0.5)
        work -= 1
    subprocess.Popen(['start', 'Alarm.wav'], shell=True)


def rest_func(rest):
    while rest > 0:
        print(rest, end="")
        time.sleep(0.5)
        rest -= 1


print("ポモドーロテクニック設定しましょう‼")
Work_Time = int(input("Work_Time:"))
Rest_Time = int(input("Rest_Time:"))
Cycle_Counter = int(input("Loop:"))
try:
    for i in range(Cycle_Counter):
        print("Loop{} Start!".format(i + 1))
        work_func(Work_Time)
        time.sleep(5)
        # 再生時間分待機
        rest_func(Rest_Time)
        print("Loop{} End!".format(i + 1))
except ValueError as err:
    print("数字を入れてください",err)
    exit()
except KeyboardInterrupt:
    exit()


