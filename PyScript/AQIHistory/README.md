<!--
 * @Author: sandwich
 * @Date: 2021-08-04 20:49:18
 * @LastEditTime: 2021-08-04 21:35:46
 * @LastEditors: sandwich
 * @Description: In User Settings Edit
 * @FilePath: /AQIHistory/README.md
-->

# AQIHistory使用说明

```
🔥本工具使用公开数据下载及发布信息，仅用于个人学习
```

<!-- TOC -->

- [使用截图](#使用截图)
- [使用说明](#使用说明)
- [tips](#tips)

<!-- /TOC -->
 
## 软件截图

![mac](https://gitee.com/codebysandwich/source/raw/master/picgo/20210809103044.png)
![win](https://gitee.com/codebysandwich/source/raw/master/picgo/1628475507(1).png)

## 使用说明

本工具使用城市小时AQI数据及发布的地面气象站点数据，下载需要时间段的数据并整合到Excel文件中。
```
城市小时AQI数据来源：https://quotsoft.net/air/
地面气象数据来源(无锡20200701为例)：https://q-weather.info/weather/58354/history/?date=2020-07-01
```

1. 运行软件
2. 填写城市名称(例如：无锡), 填写气象站点对照表中的无锡对应的区站号：58354(国家级地面气象观测站站点基本信息全表（2017）.xls打包在程序压缩包中)
3. 选择开始和截止日期
4. 点击开始按钮

下载的全国城市小时数据会存储在压缩包里`file`文件夹下, 下载合并的结果数据会在压缩包根目录下(和程序在一级目录下)
![](https://gitee.com/codebysandwich/source/raw/master/picgo/AQIHistory_tree.png)

## tips
如果你也是python使用者,本项目中的search.py文件提供了terminal程序可实现同样的效果！如果你也是Github用户欢迎star,fork。
