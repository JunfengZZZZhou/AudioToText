# -*- coding: utf-8 -*-
 
'''
Author: Junfeng Zhou
Since: 2020.3.23
Discription: This file is used to generate a window that can select a audio
file and tranlate it into text
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QFileDialog, QRadioButton, QButtonGroup

from fileToText_en import wav2txt_en, wav2txt_zh
 
 
class SpeechWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.save_path = ''
        self.open_path = ''
        self.language_mode = 1
        self.setupUi()
        self.show()
 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(484, 412)
        self.open_path_text = QtWidgets.QLineEdit(self)
        self.open_path_text.setGeometry(QtCore.QRect(40, 20, 331, 20))
        self.open_path_text.setObjectName("open_path_text")
        self.open_path_but = QtWidgets.QPushButton(self)
        self.open_path_but.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.open_path_but.setObjectName("open_path_but")
        self.save_path_but = QtWidgets.QPushButton(self)
        self.save_path_but.setGeometry(QtCore.QRect(380, 50, 75, 23))
        self.save_path_but.setObjectName("save_path_but")
        self.save_path_text = QtWidgets.QLineEdit(self)
        self.save_path_text.setGeometry(QtCore.QRect(40, 50, 331, 20))
        self.save_path_text.setObjectName("save_path_text")
        self.text_value = QtWidgets.QTextEdit(self)
        self.text_value.setGeometry(QtCore.QRect(10, 90, 461, 281))
        self.text_value.setObjectName("text_value")
        self.save_but = QtWidgets.QPushButton(self)
        self.save_but.setGeometry(QtCore.QRect(100, 380, 75, 23))
        self.save_but.setObjectName("save_but")
        self.process_but = QtWidgets.QPushButton(self)
        self.process_but.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.process_but.setObjectName("process_but")

        #radio button for process english or chinese
        self.rb1 = QRadioButton('English', self)
        self.rb2 = QRadioButton('中文', self)
        self.rb1.move(0, 0)
        self.rb2.move(70, 0)
        self.rb1.setChecked(True)
        
        self.bg = QButtonGroup(self)
        self.bg.addButton(self.rb1, 1)
        self.bg.addButton(self.rb2, 2)
        self.bg.buttonClicked.connect(self.rbclicked)
 
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def rbclicked(self):
        if self.bg.checkedId() == 1:
            self.language_mode = 1
        elif self.bg.checkedId() == 2:
            self.language_mode = 2
        else:
            print('set to default')
            self.language_mode = 1

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.open_path_text.setPlaceholderText(_translate("Form", "打开地址"))
        self.open_path_but.setText(_translate("Form", "浏览"))
        self.save_path_but.setText(_translate("Form", "浏览"))
        self.save_path_text.setPlaceholderText(_translate("Form", "保存地址"))
        self.save_but.setText(_translate("Form", "保存"))
        self.process_but.setText(_translate("Form", "处理"))
        self.open_path_but.clicked.connect(self.open_event)
        self.save_path_but.clicked.connect(self.save_event)
        self.save_but.clicked.connect(self.save_text)
        self.process_but.clicked.connect(self.process_event)

    def open_event(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件")
        print(directory1)  # 打印文件夹路径
        path = directory1[0]
        self.open_path_text.setText(_translate("Form", path))
        self.open_path = path
        
    def save_event(self):
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        self.save_path = fileName2
        self.save_path_text.setText(_translate("Form", save_path))

    def process_event(self):
        if self.open_path:
            print("请等待")
            filepath = self.open_path
            endfix = filepath.split(".")[-1]
            if endfix != "wav":
                t = filepath.split(".")
                t[-1]="wav"
                wavfilepath=".".join(t)
                ff = ffmpy.FFmpeg(inputs={filepath: None},outputs={wavfilepath: None})
                ff.run()
            else:
                wavfilepath = filepath

            if self.language_mode == 2:
                text = wav2txt_zh(wavfilepath)
            else:
                text = wav2txt_en(wavfilepath)
            self.text_value.setPlainText(text)
        else:
            self.text_value.setPlainText("请选择文件")
 
    def save_text(self):
        save_path = self.save_path
        if save_path:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.text_value.toPlainText())
            print('已保存！')
            self.text_value.clear()
        else:
            pass
 
            '''
            directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
            print(directory1)  # 打印文件夹路径
            text.setText(_translate("Form", directory1))
            fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
            print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
            print(fileName)  # 打印文件全部路径（包括文件名和后缀名）
            text.setText(_translate("Form", fileName))
            fileinfo = QFileInfo(fileName)
            print(fileinfo)  # 打印与系统相关的文件信息，包括文件的名字和在文件系统中位置，文件的访问权限，是否是目录或符合链接，等等。
            file_name = fileinfo.fileName()
            print(file_name)  # 打印文件名和后缀名
            file_suffix = fileinfo.suffix()
            print(file_suffix)  # 打印文件后缀名
            file_path = fileinfo.absolutePath()
            print(file_path)  # 打印文件绝对路径（不包括文件名和后缀名）
            files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
            print(files, ok1)  # 打印所选文件全部路径（包括文件名和后缀名）和文件类型
            fileName2, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "/", "图片文件 (*.png);;(*.jpeg)")
            print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
            '''


def createWindow():
    app = QtWidgets.QApplication(sys.argv)
    ui = SpeechWindow()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    createWindow()
 
    
