#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Sigma.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-03-23 10:10:22
# Last Modified Date: 2022-03-25 10:47:23
# Last Modified By  : sandwich <122079260@qq.com>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def gen_date(series):
    return pd.to_datetime(' '.join([series[1], series[0]]))


def to_float(item):
    if item == ' ':
        return pd.NA
    else:
        return float(item)


def lidar_pic(data, vmin=0, vmax=1, figpath='./res.png'):
    fig, axes = plt.subplots(figsize=(12, 4))
    # cas-pe配色
    colors = ['#024CEB', '#02BBA9', '#65FF00', '#FEFF00', '#FF8800', '#D40608']
    newcmap = LinearSegmentedColormap.from_list('mymap', colors)

    p = axes.imshow(data,
                    vmax=vmax,
                    vmin=vmin,
                    origin="lower",
                    aspect='auto',
                    cmap=newcmap)

    xmax, ymax = len(data.columns) - 1, len(data.index) - 1
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

    y_idx = [int(i) for i in plt.yticks()[0] if int(i) <= ymax]
    x_idx = [int(i) for i in plt.xticks()[0] if int(i) <= xmax]

    plt.yticks(y_idx, ["{:.2f}".format(float(i)) for i in data.index[y_idx]])
    plt.xticks(
        x_idx,
        ["{}\n{}".format(*str(i).split(' ')) for i in data.columns[x_idx]])

    plt.colorbar(p)
    plt.savefig(figpath)


def data_handle(filepath):
    data = pd.read_csv(filepath, encoding='GB18030', header=None)
    idx = [
        '距离/公里',
    ] + data.iloc[:2, 1:].apply(gen_date).to_list()
    data = data.iloc[2:, :]
    data.columns = idx
    data.set_index('距离/公里', inplace=True)
    data = data.apply(lambda ser: ser.apply(to_float))
    data = data[~data.isna().all(axis=1)].astype(float)
    return data


if __name__ == "__main__":
    ext = input(">>请输入消光文件地址:")
    # dep = input(">>请输入退偏文件地址:")

    ext_data = data_handle(ext)
    # dep_data = data_handle(dep)

    lidar_pic(ext_data, figpath='./消光.png')
    # lidar_pic(dep_data, vmax=0.4, figpath='./退偏.png')

    input(">>按任意键退出！")
