#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : app.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-08-06 16:05:23
# Last Modified Date: 2021-08-06 16:49:05
# Last Modified By  : sanwich <122079260@qq.com>

import sys
from search import download_cities, city_handler, weather_handler
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QThread, pyqtSignal
from pandas import date_range, concat

class RunThread(QThread):
    _signal = pyqtSignal(str)
    _signal_status = pyqtSignal(str)

    def __init__(self, city: str, code: str, dts:list) -> None:
        self.code = code
        self.city = city
        self.dts = dts
        self.url_fmt = r"https://quotsoft.net/air/data/china_cities_{:4d}{:0>2d}{:0>2d}.csv"
        self.weather_fmt = r"https://q-weather.info/weather/{}/history/?date={:4d}-{:0>2d}-{:0>2d}"
        super(RunThread, self).__init__()

    def run(self):
        datas = []
        for date in self.dts:
            url = self.url_fmt.format(date.year, date.month, date.day)
            weather = self.weather_fmt.format(self.code, date.year, date.month, date.day)
            file_path = r"./file/{:4d}{:0>2d}{:0>2d}.csv".format(
                date.year, date.month, date.day)
            self._signal_status.emit(r"站点数据{}正在下载……".format(file_path))
            if download_cities(url, file_path):
                msg = r"站点数据{}下载完成!".format(file_path)
                self._signal.emit(msg)
                city_df = city_handler(file_path, self.city)
                self._signal_status.emit(r"气象数据正在下载……")
                weather_df = weather_handler(weather)
                msg = r"{:4d}{:0>2d}{:0>2d}气象数据处理完成!".format(
                        date.year, date.month, date.day)
                self._signal.emit(msg)
                datas.append(concat([city_df, weather_df], axis=1, sort=False))
        df = concat(datas)
        df.to_excel('./{}{}_{}.xlsx'.format(self.city, self.dts[0].date(), 
                    self.dts[-1].date()))
        msg = "处理完成!"
        self._signal.emit(msg)
        self._signal_status.emit("ready")
    

class MainWindow():
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.mainwindow = QMainWindow()
        self.ui.setupUi(self.mainwindow)
        # 初始化日期
        self.ui.dateEdit_start.setDate(QDate.currentDate())
        self.ui.dateEdit_end.setDate(QDate.currentDate())
        # 固定窗体
        self.mainwindow.setFixedSize(self.mainwindow.width(),
                                     self.mainwindow.height())
        # 绑定推出程序事件
        self.ui.actionxs.triggered.connect(sys.exit)
        # 绑定开始按钮事件
        self.ui.pushButton_active.clicked.connect(self.__active_clicked)
        self.ui.statusbar.showMessage("ready")
        self.thread = None

    def __active_clicked(self):
        city = self.ui.lineEdit_city.text()
        code = self.ui.lineEdit_code.text()
        start = self.ui.dateEdit_start.date()
        end = self.ui.dateEdit_end.date()
        if (city == "" or code == ""):
            QMessageBox.warning(self.mainwindow, "注意", "城市或气象站点不能为空！",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            return
        if start > end:
            QMessageBox.warning(self.mainwindow, "注意", "截止时间必须大于开始时间!",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            return
        dts = date_range(start.toString("yyyy-MM-dd"), 
                         end.toString("yyyy-MM-dd"),
                         freq='D').to_list()
                                
        self.thread = RunThread(city, code, dts)
        self.thread._signal.connect(self.__callback)
        self.thread._signal_status.connect(self.__callback_status_bar)
        self.thread.start()
    

    def __callback(self, msg):
        self.ui.listWidget.addItem(msg)
    
    def __callback_status_bar(self, msg):
        self.ui.statusbar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.mainwindow.show()

    sys.exit(app.exec_())
