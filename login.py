# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dangnhap(object):
    def setupUi(self, Dangnhap):
        Dangnhap.setObjectName("Dangnhap")
        Dangnhap.resize(909, 674)
        Dangnhap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        Dangnhap.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=Dangnhap)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 60, 551, 511))
        self.widget.setObjectName("widget")
        self.Register = QtWidgets.QPushButton(parent=self.widget)
        self.Register.setGeometry(QtCore.QRect(329, 414, 91, 31))
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
        self.loginbutton = QtWidgets.QPushButton(parent=self.widget)
        self.loginbutton.setEnabled(True)
        self.loginbutton.setGeometry(QtCore.QRect(210, 314, 141, 31))
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
        self.Ask = QtWidgets.QLabel(parent=self.widget)
        self.Ask.setGeometry(QtCore.QRect(122, 414, 181, 31))
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
        self.Ask_2 = QtWidgets.QLabel(parent=self.widget)
        self.Ask_2.setGeometry(QtCore.QRect(170, 368, 221, 31))
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
        self.dangnhap.setGeometry(QtCore.QRect(120, 44, 310, 131))
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
        self.Ask_3 = QtWidgets.QLabel(parent=self.widget)
        self.Ask_3.setGeometry(QtCore.QRect(300, 414, 41, 31))
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
        self.input_username = QtWidgets.QTextBrowser(parent=self.widget)
        self.input_username.setGeometry(QtCore.QRect(115, 184, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_username.sizePolicy().hasHeightForWidth())
        self.input_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito Light")
        font.setPointSize(10)
        self.input_username.setFont(font)
        self.input_username.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.input_username.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.input_username.setStyleSheet("background-color: rgab(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 2px solid rgb(1, 24, 156);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 1px;")
        self.input_username.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.input_username.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.input_username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.input_username.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.input_username.setReadOnly(False)
        self.input_username.setObjectName("input_username")
        self.bg = QtWidgets.QLabel(parent=self.widget)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(19, 14, 511, 481))
        self.bg.setToolTipDuration(-1)
        self.bg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.input_password = QtWidgets.QTextBrowser(parent=self.widget)
        self.input_password.setGeometry(QtCore.QRect(115, 244, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito Light")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.input_password.setFont(font)
        self.input_password.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.input_password.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.input_password.setStyleSheet("background-color: rgab(0,0,0,0);\n"
"border : none;\n"
"border-bottom : 2px solid rgb(1, 24, 156);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom: 1px;")
        self.input_password.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.input_password.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.input_password.setLineWidth(0)
        self.input_password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.input_password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.input_password.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.input_password.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.input_password.setReadOnly(False)
        self.input_password.setAcceptRichText(True)
        self.input_password.setCursorWidth(1)
        self.input_password.setObjectName("input_password")
        self.bg.raise_()
        self.loginbutton.raise_()
        self.Ask.raise_()
        self.Ask_2.raise_()
        self.dangnhap.raise_()
        self.Ask_3.raise_()
        self.Register.raise_()
        self.input_username.raise_()
        self.input_password.raise_()
        Dangnhap.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(parent=Dangnhap)
        self.statusBar.setObjectName("statusBar")
        Dangnhap.setStatusBar(self.statusBar)

        self.retranslateUi(Dangnhap)
        QtCore.QMetaObject.connectSlotsByName(Dangnhap)
        Dangnhap.setTabOrder(self.loginbutton, self.input_password)
        Dangnhap.setTabOrder(self.input_password, self.Register)

    def retranslateUi(self, Dangnhap):
        _translate = QtCore.QCoreApplication.translate
        Dangnhap.setWindowTitle(_translate("Dangnhap", "MainWindow"))
        self.Register.setText(_translate("Dangnhap", "Click here"))
        self.loginbutton.setText(_translate("Dangnhap", "Log in"))
        self.Ask.setText(_translate("Dangnhap", "To Register New Account"))
        self.Ask_2.setText(_translate("Dangnhap", "OR"))
        self.dangnhap.setText(_translate("Dangnhap", "LOG IN"))
        self.Ask_3.setText(_translate("Dangnhap", "\""))
        self.input_username.setHtml(_translate("Dangnhap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nunito Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>"))
        self.input_username.setPlaceholderText(_translate("Dangnhap", "Username"))
        self.input_password.setHtml(_translate("Dangnhap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nunito Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>"))
        self.input_password.setPlaceholderText(_translate("Dangnhap", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dangnhap = QtWidgets.QMainWindow()
    ui = Ui_Dangnhap()
    ui.setupUi(Dangnhap)
    Dangnhap.show()
    sys.exit(app.exec())