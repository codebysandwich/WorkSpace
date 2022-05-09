#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : workstat.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2021-11-17 17:00:41
# Last Modified Date: 2021-11-17 17:27:50
# Last Modified By  : sandwich <122079260@qq.com>

import pandas as pd
from datetime import timedelta


def cal(df):
    count = df['时间'].count()
    time_delta = round((df['时间'].max() - df['时间'].min()).seconds / 3600, 2)
    count1 = ((df['时间'].dt.hour >= 19) & (df['时间'].dt.hour < 21)).sum()
    count2 = (df['时间'].dt.hour >= 21).sum()
    return pd.Series({
        '姓名': df['姓名'].iloc[0],
        '打卡次数': count,
        '打卡时间差': time_delta,
        '19-21点签到次数': count1,
        '21点后签到次数': count2
    })


if __name__ == "__main__":
    file = input('请输入文件地址:')
    time_cols = ['创建日期', '时间']
    df = pd.read_excel(file, parse_dates=time_cols)
    df['日期'] = df['时间'].dt.date

    groups = df.groupby(['工号', '日期'])
    res = groups.apply(cal)
    res[res['19-21点签到次数'] > 1] = 1
    res[res['21点后签到次数'] > 1] = 1
    res['19-21点签到次数'][res['21点后签到次数'] == 1] = 0
    res.to_excel('打卡情况明细.xlsx')

    p1 = res[res['打卡时间差'] >= 8].groupby(['工号', '姓名'])[['打卡次数']].count()
    p2 = res[res['打卡时间差'] >= 8].groupby(['工号',
                                         '姓名'])[['19-21点签到次数',
                                                 '21点后签到次数']].sum()
    
    pd.concat([p1, p2], axis=1).to_excel('./月打卡情况统计.xlsx')

    input('输入任意键退出>>')
