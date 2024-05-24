# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addLawyer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addLawyer(object):
    def setupUi(self, addLawyer):
        addLawyer.setObjectName("addLawyer")
        addLawyer.resize(460, 470)
        addLawyer.setStyleSheet("QDialog{\n"
"background-color: white;\n"
"}\n"
"\n"
"#titleWidget{\n"
"background-color: #1d3453;\n"
"}\n"
"#title {\n"
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
"")
        self.add_lawyer_info = QtWidgets.QPushButton(addLawyer)
        self.add_lawyer_info.setGeometry(QtCore.QRect(70, 410, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_lawyer_info.setFont(font)
        self.add_lawyer_info.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 139, 0);\n"
"    color:white;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.add_lawyer_info.setObjectName("add_lawyer_info")
        self.add_lawyer_cancel = QtWidgets.QPushButton(addLawyer)
        self.add_lawyer_cancel.setGeometry(QtCore.QRect(270, 410, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_lawyer_cancel.setFont(font)
        self.add_lawyer_cancel.setStyleSheet("QPushButton{\n"
"    background-color: #1d3453;\n"
"    color:white;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(53, 96, 153)\n"
"}")
        self.add_lawyer_cancel.setObjectName("add_lawyer_cancel")
        self.titleWidget = QtWidgets.QWidget(addLawyer)
        self.titleWidget.setGeometry(QtCore.QRect(0, 0, 461, 61))
        self.titleWidget.setObjectName("titleWidget")
        self.title = QtWidgets.QLabel(self.titleWidget)
        self.title.setGeometry(QtCore.QRect(60, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.layoutWidget = QtWidgets.QWidget(addLawyer)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 440, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lawyerIDinput = QtWidgets.QLineEdit(self.layoutWidget)
        self.lawyerIDinput.setMinimumSize(QtCore.QSize(0, 35))
        self.lawyerIDinput.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lawyerIDinput.setObjectName("lawyerIDinput")
        self.verticalLayout.addWidget(self.lawyerIDinput)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lawyerNameinput = QtWidgets.QLineEdit(self.layoutWidget)
        self.lawyerNameinput.setMinimumSize(QtCore.QSize(0, 35))
        self.lawyerNameinput.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lawyerNameinput.setObjectName("lawyerNameinput")
        self.verticalLayout_2.addWidget(self.lawyerNameinput)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.lawyerGenderCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.lawyerGenderCombo.setMinimumSize(QtCore.QSize(0, 35))
        self.lawyerGenderCombo.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.lawyerGenderCombo.setFont(font)
        self.lawyerGenderCombo.setObjectName("lawyerGenderCombo")
        self.lawyerGenderCombo.addItem("")
        self.lawyerGenderCombo.addItem("")
        self.lawyerGenderCombo.addItem("")
        self.lawyerGenderCombo.addItem("")
        self.verticalLayout_4.addWidget(self.lawyerGenderCombo)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.positionCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.positionCombo.setMinimumSize(QtCore.QSize(0, 35))
        self.positionCombo.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.positionCombo.setFont(font)
        self.positionCombo.setObjectName("positionCombo")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.positionCombo.addItem("")
        self.verticalLayout_5.addWidget(self.positionCombo)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.specCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.specCombo.setMinimumSize(QtCore.QSize(0, 35))
        self.specCombo.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.specCombo.setFont(font)
        self.specCombo.setObjectName("specCombo")
        self.specCombo.addItem("")
        self.specCombo.addItem("")
        self.specCombo.addItem("")
        self.specCombo.addItem("")
        self.specCombo.addItem("")
        self.specCombo.addItem("")
        self.verticalLayout_6.addWidget(self.specCombo)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lawyerEmail_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.lawyerEmail_input.setMinimumSize(QtCore.QSize(0, 35))
        self.lawyerEmail_input.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lawyerEmail_input.setObjectName("lawyerEmail_input")
        self.verticalLayout_3.addWidget(self.lawyerEmail_input)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.retranslateUi(addLawyer)
        QtCore.QMetaObject.connectSlotsByName(addLawyer)

    def retranslateUi(self, addLawyer):
        _translate = QtCore.QCoreApplication.translate
        addLawyer.setWindowTitle(_translate("addLawyer", "Dialog"))
        self.add_lawyer_info.setText(_translate("addLawyer", " Add Lawyer"))
        self.add_lawyer_cancel.setText(_translate("addLawyer", "Cancel"))
        self.title.setText(_translate("addLawyer", "Add New Lawyer"))
        self.label_2.setText(_translate("addLawyer", "Lawyer ID"))
        self.label_3.setText(_translate("addLawyer", "Name"))
        self.label_5.setText(_translate("addLawyer", "Select Gender"))
        self.lawyerGenderCombo.setItemText(0, _translate("addLawyer", "Male"))
        self.lawyerGenderCombo.setItemText(1, _translate("addLawyer", "Female"))
        self.lawyerGenderCombo.setItemText(2, _translate("addLawyer", "Nonbinary"))
        self.lawyerGenderCombo.setItemText(3, _translate("addLawyer", "Prefer not to say"))
        self.label_6.setText(_translate("addLawyer", "Select Position"))
        self.positionCombo.setItemText(0, _translate("addLawyer", "Junior Associate"))
        self.positionCombo.setItemText(1, _translate("addLawyer", "Senior Associate"))
        self.positionCombo.setItemText(2, _translate("addLawyer", "Junior Partner"))
        self.positionCombo.setItemText(3, _translate("addLawyer", "Senior Partner"))
        self.positionCombo.setItemText(4, _translate("addLawyer", "Managing Partner"))
        self.label_7.setText(_translate("addLawyer", "Lawyer Specialization"))
        self.specCombo.setItemText(0, _translate("addLawyer", "Corporate Law"))
        self.specCombo.setItemText(1, _translate("addLawyer", "Criminal Law"))
        self.specCombo.setItemText(2, _translate("addLawyer", "Finance Law"))
        self.specCombo.setItemText(3, _translate("addLawyer", "Bankruptcy Law"))
        self.specCombo.setItemText(4, _translate("addLawyer", "Intellectual Property Law"))
        self.specCombo.setItemText(5, _translate("addLawyer", "Labor Law"))
        self.label_4.setText(_translate("addLawyer", "E-Mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addLawyer = QtWidgets.QDialog()
    ui = Ui_addLawyer()
    ui.setupUi(addLawyer)
    addLawyer.show()
    sys.exit(app.exec_())
