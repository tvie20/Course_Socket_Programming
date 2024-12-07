# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from register import Ui_Dangky

class Ui_Dangnhap(object):
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dangky()
        self.ui.setupUi(self.window)
        self.window.show()
        self.centralwidget.parentWidget().hide() #Ẩn cửa sổ chính

    def setupUi(self, Dangnhap):
        Dangnhap.setObjectName("Dangnhap")
        Dangnhap.resize(909, 698)
        Dangnhap.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        Dangnhap.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        Dangnhap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        Dangnhap.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=Dangnhap)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 60, 551, 511))
        self.widget.setObjectName("widget")
        self.loginbutton = QtWidgets.QPushButton(parent=self.widget)
        self.loginbutton.setEnabled(True)
        self.loginbutton.setGeometry(QtCore.QRect(200, 310, 150, 31))
        self.loginbutton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.loginbutton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.loginbutton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.loginbutton.setToolTipDuration(-1)
        self.loginbutton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.loginbutton.setStyleSheet("QPushButton\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Nunito Medium\";\n"
"border-radius: 15px;\n"
"background-color: rgb(1, 24, 156);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color: rgb(1, 24, 156);\n"
"font: 10pt \"Nunito Black\";\n"
"background-color: rgb(222, 233, 255);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"color: rgb(0,0,0);\n"
"font: 10pt \"Nunito Medium\";\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.loginbutton.setShortcut("")
        self.loginbutton.setCheckable(False)
        self.loginbutton.setChecked(False)
        self.loginbutton.setAutoDefault(True)
        self.loginbutton.setDefault(False)
        self.loginbutton.setFlat(False)
        self.loginbutton.setObjectName("loginbutton")
        self.Ask_2 = QtWidgets.QLabel(parent=self.widget)
        self.Ask_2.setGeometry(QtCore.QRect(165, 370, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Ask_2.setFont(font)
        self.Ask_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Ask_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Ask_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Ask_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Ask_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Ask_2.setIndent(0)
        self.Ask_2.setObjectName("Ask_2")
        self.dangnhap = QtWidgets.QLabel(parent=self.widget)
        self.dangnhap.setGeometry(QtCore.QRect(20, 34, 510, 131))
        font = QtGui.QFont()
        font.setFamily("Public Sans Black")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.dangnhap.setFont(font)
        self.dangnhap.setStyleSheet("color : rgb(1, 24, 156)")
        self.dangnhap.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.dangnhap.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dangnhap.setObjectName("dangnhap")
        self.bg = QtWidgets.QLabel(parent=self.widget)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(20, 14, 510, 481))
        self.bg.setToolTipDuration(-1)
        self.bg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.username = QtWidgets.QLineEdit(parent=self.widget)
        self.username.setGeometry(QtCore.QRect(115, 168, 321, 31))
        self.username.setStyleSheet("background-color: rgab(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 2px solid rgb(1, 24, 156);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 1px;")
        self.username.setText("")
        self.username.setMaxLength(100)
        self.username.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(parent=self.widget)
        self.password.setGeometry(QtCore.QRect(115, 238, 321, 31))
        self.password.setStyleSheet("background-color: rgab(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 2px solid rgb(1, 24, 156);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 1px;")
        self.password.setText("")
        self.password.setMaxLength(100)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.Register = QtWidgets.QPushButton(parent=self.widget,  clicked = lambda:self.open_window())
        self.Register.setGeometry(QtCore.QRect(335, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(11)
        font.setUnderline(True)
        self.Register.setFont(font)
        self.Register.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Register.setStyleSheet("QPushButton {\n"
"border : none;\n"
"border-bottom : solid rgb(1, 24, 156);\n"
"color: rgb(1, 24, 156);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color: rgb(1, 24, 156);\n"
"font: 11pt \"Nunito Black\";\n"
"background-color: rgb(222, 233, 255);\n"
"border-radius: 15px;\n"
"}")
        self.Register.setIconSize(QtCore.QSize(15, 15))
        self.Register.setAutoDefault(True)
        self.Register.setObjectName("Register")
        self.Ask = QtWidgets.QLabel(parent=self.widget)
        self.Ask.setGeometry(QtCore.QRect(125, 420, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Ask.setFont(font)
        self.Ask.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Ask.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Ask.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Ask.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Ask.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Ask.setIndent(0)
        self.Ask.setObjectName("Ask")
        self.Ask_3 = QtWidgets.QLabel(parent=self.widget)
        self.Ask_3.setGeometry(QtCore.QRect(305, 420, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Ask_3.setFont(font)
        self.Ask_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Ask_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Ask_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Ask_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Ask_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Ask_3.setIndent(0)
        self.Ask_3.setObjectName("Ask_3")
        self.bg.raise_()
        self.loginbutton.raise_()
        self.Ask_2.raise_()
        self.dangnhap.raise_()
        self.username.raise_()
        self.password.raise_()
        self.Register.raise_()
        self.Ask.raise_()
        self.Ask_3.raise_()
        Dangnhap.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dangnhap)
        QtCore.QMetaObject.connectSlotsByName(Dangnhap)
        Dangnhap.setTabOrder(self.Register, self.username)
        Dangnhap.setTabOrder(self.username, self.password)
        Dangnhap.setTabOrder(self.password, self.loginbutton)


    def retranslateUi(self, Dangnhap):
        _translate = QtCore.QCoreApplication.translate
        Dangnhap.setWindowTitle(_translate("Dangnhap", "MainWindow"))
        self.loginbutton.setText(_translate("Dangnhap", "Log in"))
        self.Ask_2.setText(_translate("Dangnhap", "OR"))
        self.dangnhap.setText(_translate("Dangnhap", "LOG IN"))
        self.username.setPlaceholderText(_translate("Dangnhap", "Username"))
        self.password.setPlaceholderText(_translate("Dangnhap", "Password"))
        self.Register.setText(_translate("Dangnhap", "Click here"))
        self.Ask.setText(_translate("Dangnhap", "To Register New Account"))
        self.Ask_3.setText(_translate("Dangnhap", "\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dangnhap = QtWidgets.QMainWindow()
    ui = Ui_Dangnhap()
    ui.setupUi(Dangnhap)
    Dangnhap.show()
    sys.exit(app.exec())
