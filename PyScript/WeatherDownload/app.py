# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2021-08-15 18:18:28
@LastEditTime: 2021-08-15 18:18:30
@LastEditors: sandwich
@Description: 气象数据下载脚本
@FilePath: \WeatherDownload\app.py
'''

from pandas import read_html, date_range

if __name__ == "__main__":
    code = input("请输入气象区站号编码(例如无锡:58354):")
    start = input("请输入下载开始日期(例如:2021-07-01):")
    end = input("请输入下载截至日期(例如:2021-07-05):")
    # 网站示例https://q-weather.info/weather/58354/history/?date=2020-07-01
    url_fmt = r'https://q-weather.info/weather/{}/history/?date={}'
    dts = date_range(start, end, freq='D')
    for dt in dts:
        url = url_fmt.format(code, "{:4d}-{:0>2d}-{:0>2d}".format(
                                     dt.year, dt.month, dt.day))
        df = read_html(url)[0]
        df.to_excel('./file/{}_{}.xlsx'.format(code, dt.date()))
        print('{}下载完成!'.format(dt.date()))
    input("按任意键退出程序！")