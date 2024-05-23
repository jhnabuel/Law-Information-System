# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editClientCase.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editClientCase(object):
    def setupUi(self, editClientCase):
        editClientCase.setObjectName("editClientCase")
        editClientCase.resize(340, 330)
        editClientCase.setStyleSheet("QDialog{\n"
"background-color: white;\n"
"}\n"
"\n"
"#titleWidget{\n"
"background-color: #1d3453;\n"
"}\n"
"#title_2{\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QComboBox{\n"
"border: 1px solid black;\n"
"border-radius: 8px;\n"
"background-color: #1d3453;\n"
"color: white;\n"
"height: 35px;\n"
"\n"
"\n"
"}\n"
"\n"
"QDateEdit{\n"
"    border:1px solid gray;\n"
"    border-radius: 8px;\n"
"    padding-left: 15px;\n"
"    height: 35px;\n"
"    background-color: #1d3453;\n"
"color: white;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(editClientCase)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 160, 281, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.edit_case_combo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.edit_case_combo.setFont(font)
        self.edit_case_combo.setObjectName("edit_case_combo")
        self.verticalLayout_2.addWidget(self.edit_case_combo)
        self.edit_client_case = QtWidgets.QPushButton(editClientCase)
        self.edit_client_case.setGeometry(QtCore.QRect(30, 260, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.edit_client_case.setFont(font)
        self.edit_client_case.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 139, 0);\n"
"    color:white;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.edit_client_case.setObjectName("edit_client_case")
        self.titleWidget = QtWidgets.QWidget(editClientCase)
        self.titleWidget.setGeometry(QtCore.QRect(0, 0, 461, 61))
        self.titleWidget.setObjectName("titleWidget")
        self.title_2 = QtWidgets.QLabel(self.titleWidget)
        self.title_2.setGeometry(QtCore.QRect(0, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.layoutWidget_2 = QtWidgets.QWidget(editClientCase)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 70, 281, 73))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.edit_client_combo = QtWidgets.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.edit_client_combo.setFont(font)
        self.edit_client_combo.setObjectName("edit_client_combo")
        self.verticalLayout.addWidget(self.edit_client_combo)
        self.edit_info_cancel = QtWidgets.QPushButton(editClientCase)
        self.edit_info_cancel.setGeometry(QtCore.QRect(190, 260, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.edit_info_cancel.setFont(font)
        self.edit_info_cancel.setStyleSheet("QPushButton{\n"
"    background-color: #1d3453;\n"
"    color:white;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(53, 96, 153)\n"
"}")
        self.edit_info_cancel.setObjectName("edit_info_cancel")

        self.retranslateUi(editClientCase)
        QtCore.QMetaObject.connectSlotsByName(editClientCase)

    def retranslateUi(self, editClientCase):
        _translate = QtCore.QCoreApplication.translate
        editClientCase.setWindowTitle(_translate("editClientCase", "Dialog"))
        self.label_5.setText(_translate("editClientCase", "Case Name"))
        self.edit_client_case.setText(_translate("editClientCase", "Edit Information"))
        self.title_2.setText(_translate("editClientCase", "Edit Client Case"))
        self.label_6.setText(_translate("editClientCase", "Client Name"))
        self.edit_info_cancel.setText(_translate("editClientCase", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editClientCase = QtWidgets.QDialog()
    ui = Ui_editClientCase()
    ui.setupUi(editClientCase)
    editClientCase.show()
    sys.exit(app.exec_())