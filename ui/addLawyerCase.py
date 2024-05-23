# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addLawyerCase.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addLawyerCase(object):
    def setupUi(self, addLawyerCase):
        addLawyerCase.setObjectName("addLawyerCase")
        addLawyerCase.resize(345, 420)
        addLawyerCase.setStyleSheet("QDialog{\n"
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
        self.titleWidget = QtWidgets.QWidget(addLawyerCase)
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
        self.add_info = QtWidgets.QPushButton(addLawyerCase)
        self.add_info.setGeometry(QtCore.QRect(30, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.add_info.setFont(font)
        self.add_info.setStyleSheet("QPushButton{\n"
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
        self.add_info.setObjectName("add_info")
        self.add_info_cancel = QtWidgets.QPushButton(addLawyerCase)
        self.add_info_cancel.setGeometry(QtCore.QRect(190, 350, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.add_info_cancel.setFont(font)
        self.add_info_cancel.setStyleSheet("QPushButton{\n"
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
        self.add_info_cancel.setObjectName("add_info_cancel")
        self.widget = QtWidgets.QWidget(addLawyerCase)
        self.widget.setGeometry(QtCore.QRect(20, 80, 301, 242))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.assigned_lawyer_combo = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.assigned_lawyer_combo.setFont(font)
        self.assigned_lawyer_combo.setObjectName("assigned_lawyer_combo")
        self.verticalLayout_3.addWidget(self.assigned_lawyer_combo)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.case_name_combo = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.case_name_combo.setFont(font)
        self.case_name_combo.setObjectName("case_name_combo")
        self.verticalLayout_4.addWidget(self.case_name_combo)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.lawyer_start_date = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.lawyer_start_date.setFont(font)
        self.lawyer_start_date.setObjectName("lawyer_start_date")
        self.verticalLayout_5.addWidget(self.lawyer_start_date)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(addLawyerCase)
        QtCore.QMetaObject.connectSlotsByName(addLawyerCase)

    def retranslateUi(self, addLawyerCase):
        _translate = QtCore.QCoreApplication.translate
        addLawyerCase.setWindowTitle(_translate("addLawyerCase", "Dialog"))
        self.title_2.setText(_translate("addLawyerCase", "Add New Lawyer Case"))
        self.add_info.setText(_translate("addLawyerCase", "Add Information"))
        self.add_info_cancel.setText(_translate("addLawyerCase", "Cancel"))
        self.label_4.setText(_translate("addLawyerCase", "Assigned Lawyer"))
        self.label_5.setText(_translate("addLawyerCase", "Case Name"))
        self.label_6.setText(_translate("addLawyerCase", "Start Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addLawyerCase = QtWidgets.QDialog()
    ui = Ui_addLawyerCase()
    ui.setupUi(addLawyerCase)
    addLawyerCase.show()
    sys.exit(app.exec_())
