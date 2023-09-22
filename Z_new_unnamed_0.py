from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
# import rc_add_link

class Ui_prog():
    def setupUi(self, note):
        note.setObjectName("add_link")
        note.resize(410, 233)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/z_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        note.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(note)
        self.widget.setGeometry(QtCore.QRect(0, 0, 410, 233))
        self.widget.setStyleSheet(".QWidget#widget{\n"
"    background-color:#212227;\n"
"    border:2px solid silver;\n"
"}\n"
"\n"
".QLineEdit{\n"
"    border: 2px solid white;\n"
"    font-family: MS Shell Dlg 2, sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    outline: none;\n"
"    background: #212227;\n"
"    color: white;\n"
"}\n"
"\n"
".QLabel{\n"
"    font-family: MS Shell Dlg 2, sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 13px;\n"
"    color: white;\n"
"}\n"
"\n"
"QCheckBox{\n"
"font-family: MS Shell Dlg 2, sans-serif;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"color: white;}\n"
"QCheckBox::indicator {\n"
"     width: 14px;\n"
"     height: 14px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked\n"
"  {\n"
"    image: url(:/checkbox/unchecked.png);\n"
"  }\n"
"\n"
" QCheckBox::indicator:checked\n"
"  {\n"
"    image: url(:/checkbox/checked.png);\n"
"  }\n"
"\n"
" QCheckBox::indicator:unchecked:hover\n"
"  {\n"
"    image: url(:/checkbox/hover_unchecked.png);\n"
"  }\n"
"\n"
" QCheckBox::indicator:checked:hover\n"
"  {\n"
"    image: url(:/checkbox/hover_checked.png);\n"
"  }")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 410, 31))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    border:2px solid silver;\n"
"background: #BAFAFF}\n"
"\n"
".QPushButton#exit{\n"
"image:url(:/exit/exit.png);\n"
"border:none;\n"
"background: #21F227;\n"
"}\n"
".QPushButton#exit:hover{\n"
"image:url(:/exit/exit_hover.png);\n"
"border:none;\n"    
"background: #22F227;\n"
"}\n"
"\n"
"\n"
".QPushButton#hider{\n"
"image:url(:/hide/hider.png);\n"
"border:none;\n"
"}\n"
"\n"
"\n"
".QPushButton#hider:hover{\n"
"image:url(:/hide/hide_hover.png);\n"
"border:none;\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.exit = QtWidgets.QPushButton(self.widget_2)
        self.exit.setGeometry(QtCore.QRect(390, 10, 16, 16))
        self.exit.setMaximumSize(QtCore.QSize(33, 23))
        self.exit.setStyleSheet("")
        self.exit.setText("X")
        self.exit.setObjectName("exit")
        self.hider = QtWidgets.QPushButton(self.widget_2)
        self.hider.setGeometry(QtCore.QRect(370, 10, 16, 16))
        self.hider.setMaximumSize(QtCore.QSize(33, 23))
        self.hider.setStyleSheet("background: #BBB23AAA")
        self.hider.setText("▬▬")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/hide/hider.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.hider.setIcon(icon1)
        self.hider.setObjectName("hider")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(195, 90, 81, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.Cancel = QtWidgets.QPushButton(self.widget)
        self.Cancel.setGeometry(QtCore.QRect(270, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet(".QPushButton{\n"
"font-size:12px;\n"
"font-family: MS Shell Dlg 2, sans-serif;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"background: #232930;\n"
"color: white;}")
        self.Cancel.setObjectName("Cancel")
        self.link_item = QtWidgets.QLineEdit(self.widget)
        self.link_item.setGeometry(QtCore.QRect(25, 50, 360, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.link_item.setFont(font)
        self.link_item.setStyleSheet("")
        self.link_item.setAlignment(QtCore.Qt.AlignCenter)
        self.link_item.setObjectName("link_item")
        self.number_value = QtWidgets.QLineEdit(self.widget)
        self.number_value.setGeometry(QtCore.QRect(283, 90, 101, 18))
        self.number_value.setStyleSheet("")
        self.number_value.setObjectName("number_value")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(25, 90, 41, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.Ok = QtWidgets.QPushButton(self.widget)
        self.Ok.setGeometry(QtCore.QRect(65, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Ok.setFont(font)
        self.Ok.setStyleSheet(".QPushButton{\n"
"font-family: MS Shell Dlg 2, sans-serif;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"font-size:12px;\n"
"background: #232930;\n"
"color: white;}")
        self.Ok.setObjectName("Ok")
        self.cost_value = QtWidgets.QLineEdit(self.widget)
        self.cost_value.setGeometry(QtCore.QRect(70, 90, 101, 18))
        self.cost_value.setStyleSheet("")
        self.cost_value.setInputMethodHints(QtCore.Qt.ImhNone)
        self.cost_value.setObjectName("cost_value")
        self.max_cost_value = QtWidgets.QLineEdit(self.widget)
        self.max_cost_value.setGeometry(QtCore.QRect(190, 130, 101, 18))
        self.max_cost_value.setStyleSheet("")
        self.max_cost_value.setObjectName("max_cost_value")
        self.checkbox_per = QtWidgets.QCheckBox(self.widget)
        self.checkbox_per.setGeometry(QtCore.QRect(25, 130, 161, 17))
        self.checkbox_per.setStyleSheet("")
        self.checkbox_per.setObjectName("checkbox_per")

        self.retranslateUi(note)
        QtCore.QMetaObject.connectSlotsByName(note)

    def retranslateUi(self, add_link):
        _translate = QtCore.QCoreApplication.translate
        add_link.setWindowTitle(_translate("add_link", "Form"))
        self.label_2.setText(_translate("add_link", "Количество:"))
        self.Cancel.setText(_translate("add_link", "Отмена"))
        self.link_item.setPlaceholderText(_translate("add_link", "Ссылка на предмет"))
        self.label.setText(_translate("add_link", "Цена:"))
        self.Ok.setText(_translate("add_link", "Ок"))
        self.checkbox_per.setText(_translate("add_link", "Перебивать цену до:"))

class Widget(QtWidgets.QWidget, Ui_prog):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def close_app(self):
        add_link.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_link = Widget()

    add_link.exit.clicked.connect(add_link.close_app)
    

    add_link.show()
    sys.exit(app.exec_())