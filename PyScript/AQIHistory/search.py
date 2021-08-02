# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2021-08-02 09:27:52
@LastEditTime: 2021-08-02 09:27:52
@LastEditors: sandwich
@Description: 查询城市每小时天数据
@FilePath: /AQIHistory/search.py
'''

import requests
from datetime import datetime
import pandas as pd

def download_cities(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return True

def get_datetime(series):
    year = int(str(series["date"])[:4])
    month = int(str(series["date"])[4:6])
    day = int(str(series["date"])[6:])
    hour = int(series["hour"])
    return datetime(year, month, day, hour)

if __name__ == "__main__":
    # date = r"20210721"
    # city = "镇江"
    city = input("请输入需要查询的城市(例如:北京): ")
    date = input("请输入需要查询的日期: ")
    url_fmt = r"https://quotsoft.net/air/data/china_cities_{}.csv"
    file_path = r"./file/{}.csv".format(date)
    if download_cities(url_fmt.format(date), file_path):
        print("download completed!")
    cols = ["date", "hour", "type", city]
    df = pd.read_csv(file_path).loc[:, cols]
    df["时间"] = df.apply(lambda s: get_datetime(s), axis=1)
    ser = df.set_index(["时间", "type"]).drop(["date", "hour"], axis=1)[city]
    ser.unstack().to_excel(f"./{city}_{date}.xlsx")
    input("按任意键退出程序!")