#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : app.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-08-06 16:05:23
# Last Modified Date: 2021-08-06 16:49:05
# Last Modified By  : sanwich <122079260@qq.com>

import sys
from search import get_concat_df
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pandas import date_range, concat


class MainWindow():
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.mainwindow = QMainWindow()
        self.ui.setupUi(self.mainwindow)
        # 固定窗体
        self.mainwindow.setFixedSize(self.mainwindow.width(),
                                     self.mainwindow.height())
        # 绑定开始按钮事件
        self.ui.pushButton_active.clicked.connect(self.__active_clicked)

    def __active_clicked(self):
        city = self.ui.lineEdit_city.text()
        code = self.ui.lineEdit_code.text()
        if (city == "" or code == ""):
            QMessageBox.warning(self.mainwindow, "注意", "城市或气象站点不能为空！",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
        self.__search(city, code)

    def __search(self, city, code):
        url_fmt = r"https://quotsoft.net/air/data/china_cities_{:4d}{:0>2d}{:0>2d}.csv"
        weather_fmt = r"https://q-weather.info/weather/{}/history/?date={:4d}-{:0>2d}-{:0>2d}"
        start = self.ui.dateEdit_start.date()
        end = self.ui.dateEdit_end.date()
        dts = date_range(start.toString(), end.toString(), freq='D')
        df = concat(get_concat_df(url_fmt, weather_fmt, city, code, dts))
        df.to_excel('./{}{}_{}.xlsx'.format(city, start.toString(),
                                            end.toString()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.mainwindow.show()

    sys.exit(app.exec_())
