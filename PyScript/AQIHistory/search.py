# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2021-08-02 09:27:52
@LastEditTime: 2021-08-02 09:27:52
@LastEditors: sandwich
@Description: 查询城市每小时天数据
@FilePath: /AQIHistory/search.py
'''

import sys
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

def city_handler(file_path, city):
    cols = ["date", "hour", "type", city]
    df = pd.read_csv(file_path).loc[:, cols]
    df["时间"] = df.apply(lambda s: get_datetime(s), axis=1)
    ser = df.set_index(["时间", "type"]).drop(["date", "hour"], axis=1)[city]
    return ser.unstack()

def tz_handler(tz_s):
    items = str(tz_s).split(' ')
    return datetime.strptime("{} {}".format(items[0], items[1]), r"%Y-%m-%d %H:%M")

def weather_handler(weather):
    df = pd.read_html(weather)[0]
    df["时间"] = df["时次"].apply(tz_handler)
    df.drop("时次", axis=1, inplace=True)
    df.set_index("时间", inplace=True)
    return df

def get_concat_df(url_fmt, weather_fmt, city, code, date_ser):
    for date in date_ser:
        url = url_fmt.format(date.year, date.month, date.day)
        weather = weather_fmt.format(code, date.year, date.month, date.day)
        file_path = r"./file/{:4d}{:0>2d}{:0>2d}.csv".format(date.year, date.month, date.day)
        if download_cities(url, file_path):
            print(r"站点数据{}下载完成!".format(file_path))
            city_df = city_handler(file_path, city)
            print("=====开始处理气象数据====")
            weather_df = weather_handler(weather)
            print("气象数据处理完成!")
            yield pd.concat([city_df, weather_df], axis=1)
            


if __name__ == "__main__":
    city = input("请输入需要查询的城市(例如:镇江): ")
    code = input("请输入需要查询气象点位编码(例如:58252): ")
    start = input("请输入需要查询的开始日期(例如:20210701): ")
    end = input("请输入需要查询截至日期(例如:20210705): ")

    # 时间格式化占位符为整数 例如 2012 01 02
    url_fmt = r"https://quotsoft.net/air/data/china_cities_{:4d}{:0>2d}{:0>2d}.csv"
    weather_fmt = r"https://q-weather.info/weather/{}/history/?date={:4d}-{:0>2d}-{:0>2d}"

    start_dt = datetime.strptime(start, r"%Y%m%d")
    end_dt = datetime.strptime(end, r"%Y%m%d")

    if start_dt > end_dt:
        print("截至日期必须大于开始日期！")
        sys.exit()
    
    date_ser = pd.date_range(start_dt, end_dt, freq='D')

    df = pd.concat(get_concat_df(url_fmt, weather_fmt, city, code, date_ser))
    df.to_excel(r"{}{:4d}{:0>2d}{:0>2d}-{:4d}{:0>2d}{:0>2d}.xlsx".format(city, 
                   start_dt.year, start_dt.month, start_dt.day,
                   end_dt.year, end_dt.month, end_dt.day))
    print("处理完成！")