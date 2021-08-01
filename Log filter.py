import os
import datetime
import time
#
path = r"\\192.168.111.49\CinderellaLog\Cinderella\DailyWalkthrough"
# 获取文件下所有文件
files = os.listdir(path)
print(files)
input_screen = "00-04-4b-e9-be-09_18_2021-01-14-18-02-02.log.tar"

def get_time_Data():
    """
    :return:筛选后的 开始于结束时间戳
        """
    # start_time = input("请输入起始时间：")
    start_time = "2021-01-21 00:00:00"
    start_time_int = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    # end_time = input("请输入结束时间：")
    end_time = "2021-01-21 23:59:21"
    end_time_int = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    Timestamp = int(time.mktime(start_time_int))
    timestamp = int(time.mktime(end_time_int))
    return Timestamp,timestamp


start_time, end_time = get_time_Data()


def screen_path_liat():
    """

    :return: 返回筛选后的路径列表
    """
    path_list = []
    for i in range(len(files) - 1):
        # 获取文件创建时间
        now = os.path.getatime(path + '/' + files[i])
        sys_time = int(now)
        if start_time < sys_time < end_time:
            path_list.append(path + '/' + files[i])
    return path_list


list_dir = screen_path_liat()

def detect_nowalk(dir_path):
    files = os.listdir(dir_path)
    for filename in files:
        if filename.startswith(input_screen):
            print(os.path.join(dir_path, filename))
        next = os.path.join(dir_path, filename)
        if os.path.isdir(next):
            detect_nowalk(next)
for i in list_dir:
    detect_nowalk(i)




