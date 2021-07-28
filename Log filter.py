import os
import datetime
import time

path = r"\\192.168.111.49\CinderellaLog\Cinderella\DailyWalkthrough"
files = os.listdir(path)


def getparameters():
    while True:
        start_time = input("请输入起始时间：")
        start_time_int = time.strptime(start_time, "%Y-%m-%d-%H:%M")
        end_time = input("请输入结束时间：")
        end_time_int = time.strptime(end_time, "%Y-%m-%d-%H:%M")
        key_work = input("请输入过滤关键字：")
        Timestamp = int(time.mktime(start_time_int))
        timestamp = int(time.mktime(end_time_int))
        if len(start_time) == 0 or len(key_work) == 0 or end_time == 0:
            flag = input("您输入的文件名或关键子为空，输出c重试，q退出程序：")
            if flag == "q":
                return
            elif flag == "c":
                continue
        else:
            break






for i in range(len(files) - 1):
    now = os.path.getatime(path + '/' + files[1])
    print(now)
# timestamp = os.path.getmtime(r"\\192.168.111.49\CinderellaLog\Cinderella\driver_test")
# print(datetime.datetime.fromtimestamp(timestamp))

if __name__ == '__main__':
    getparameters()

