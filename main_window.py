import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow, QDialog, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt, QPoint, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QFont
from PyQt5.QtCore import QDate

from connect_database import ConnectDatabase

from ui.mainsys import Ui_MainWindow
from ui.addLawyer import Ui_addLawyer
from ui.editLawyer import Ui_editLawyer

from ui.addCase import Ui_addCase
from ui.editCase import Ui_editCase



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a database object
        self.db = ConnectDatabase()

        """
        Initializations for starting and switching pages. Ignore these.
        """
        self.pages = self.ui.functionWidget
        self.pages.setCurrentIndex(0)
        self.lawyer_table = self.ui.lawyerDisplay
        self.lawyer_table.horizontalHeader().setVisible(True)
        self.client_table = self.ui.clientDisplay
        self.case_table = self.ui.caseDisplay

        self.show_lawyer_btn = self.ui.lawyerButton
        self.show_client_btn = self.ui.clientButton
        self.show_case_btn = self.ui.caseButton
        self.show_client_lawyer_btn = self.ui.caseButton_2

        self.show_lawyer_btn.toggled.connect(lambda: self.change_system_page(self.show_lawyer_btn))
        self.show_client_btn.toggled.connect(lambda: self.change_system_page(self.show_client_btn))
        self.show_case_btn.toggled.connect(lambda: self.change_system_page(self.show_case_btn))
        self.show_client_lawyer_btn.toggled.connect(lambda: self.change_system_page(self.show_client_lawyer_btn))

        """
        Initialization for lawyer page
        """
        self.addlawyerbtn = self.ui.addLawyer
        self.deletelawyerbtn = self.ui.deleteLawyer
        self.editlawyerbtn = self.ui.editLawyer
        self.display_lawyer_info = self.ui.lawyerDisplay
        self.search_lawyer = self.ui.searchLawyer
        self.search_lawyer.textChanged.connect(self.search_lawyer_info)

        """
        Initialization for case page
        """

        self.addcasebtn = self.ui.addCase
        self.deletecasebtn = self.ui.deleteCase
        self.editcasebtn = self.ui.editCase
        self.display_case_info = self.ui.caseDisplay
        self.search_case = self.ui.searchClient_2
        self.search_case.textChanged.connect(self.search_case_info)

        #Initialize the buttons for each page
        self.init_signal_slot()

        # Load lawyer table
        self.load_lawyer_info()

        # Load case table
        self.load_case_info()

   



    def init_signal_slot(self):
        #Initizalizes all buttons inside each page
        self.addlawyerbtn.clicked.connect(self.open_addlawyer_dialog)
        self.deletelawyerbtn.clicked.connect(self.delete_lawyer_info)
        self.editlawyerbtn.clicked.connect(self.open_editLawyer_dialog)
        self.addcasebtn.clicked.connect(self.open_addcase_dialog)
        self.deletecasebtn.clicked.connect(self.delete_case_info)
        self.editcasebtn.clicked.connect(self.open_editCase_dialog)

    def open_addlawyer_dialog(self):
        # Opens the add lawyer page.
        self.add_lawyer_dialog = AddLawyerDialog(parent=self, connectDB=self.db)
        self.add_lawyer_dialog.accepted.connect(self.load_lawyer_info)
        self.add_lawyer_dialog.exec_()

    def open_editLawyer_dialog(self):
        try:
            selected_row = self.display_lawyer_info.currentRow()
            if selected_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to edit lawyer information.")
                return
            # Fetch data from the selected row
            lawyer_id = self.display_lawyer_info.item(selected_row, 0).text().strip()
            lawyer_name = self.display_lawyer_info.item(selected_row, 1).text().strip()
            lawyer_gender = self.display_lawyer_info.item(selected_row, 2).text().strip()
            lawyer_position = self.display_lawyer_info.item(selected_row, 3).text().strip()
            lawyer_specialization = self.display_lawyer_info.item(selected_row, 4).text().strip()
            lawyer_email = self.display_lawyer_info.item(selected_row, 5).text().strip()

            # Opens the edit lawyer information page.
            self.edit_lawyer_dialog = EditLawyerDialog(parent=self, connectDB=self.db)
            self.edit_lawyer_dialog.set_lawyer_data(lawyer_id, lawyer_name, lawyer_gender, lawyer_position,
                                                    lawyer_specialization, lawyer_email)
            self.edit_lawyer_dialog.accepted.connect(self.load_lawyer_info)
            self.edit_lawyer_dialog.exec_()
        except Exception as E:
            print(str(E))


    def load_lawyer_info(self):
        self.db.connect_database()
        try:
            # Fetch all lawyer info from the database
            lawyer_data = self.db.search_lawyer_info()
            # Display lawyer data in the table widget
            self.display_lawyer_data(lawyer_data)
        except Exception as E:
            print("Error:", E)
        finally:
            # Close the database connection
            self.db.connect.close()

    def search_lawyer_info(self):
        # Search lawyer information
        self.db.connect_database()
        try:
            search_value = self.search_lawyer.text().strip()
            search_results = self.db.search_lawyer_info(search_value)
            self.display_lawyer_data(search_results)
        except Exception as E:
            print(str(E))

    def display_lawyer_data(self, lawyer_data):
        # Clear exisiting table contents
        self.display_lawyer_info.clearContents()
        self.display_lawyer_info.setRowCount(0)
        self.display_lawyer_info.verticalHeader().setVisible(False)
        lawyer_headers = ["Lawyer ID", "Name", "Gender", "Position", "Specialization", "E-Mail"]
        # Set the horizontal header labels
        self.display_lawyer_info.setHorizontalHeaderLabels(lawyer_headers)
        if lawyer_data:
            # Set the number of rows and columns based on the data
            self.display_lawyer_info.setRowCount(len(lawyer_data))
            self.display_lawyer_info.setColumnCount(len(lawyer_headers))

            # Populate the tablewidget with data
            for row_num, row_data in enumerate(lawyer_data):
                for col_num, col_data in enumerate(row_data):
                    value = row_data[col_data]
                    self.display_lawyer_info.setItem(row_num, col_num, QTableWidgetItem(str(value)))
            # Set the selection mode to single selection
            self.display_lawyer_info.setSelectionMode(QAbstractItemView.SingleSelection)

    def delete_lawyer_info(self):
        try:
            select_row = self.display_lawyer_info.currentRow()
            if select_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to delete.")
                return

            # If a row is selected, get the lawyer ID for confirmation
            lawyer_id = self.display_lawyer_info.item(select_row, 0).text().strip()

            # Ask for confirmation using a QMessageBox
            reply = QMessageBox.question(self, 'Delete Confirmation',
                                         f"Are you sure you want to delete lawyer with ID: {lawyer_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # User confirmed deletion, proceed with deletion
                self.db.connect_database()  # Ensure database connection is open
                self.db.delete_lawyer_info(lawyer_id)  # Call a method in your database handler to delete

                # Optionally, you may want to remove the row from the table widget
                self.display_lawyer_info.removeRow(select_row)

                # Inform the user with a QMessageBox
                QMessageBox.information(self, "Deletion Successful", f"Deleted lawyer with ID: {lawyer_id}")

        except Exception as E:
            print("Error deleting lawyer:", str(E))

        finally:
            # Reload the table after deleting.
            self.load_lawyer_info()
            self.db.connect.close()  # Ensure database connection is closed



    # Case
    def open_addcase_dialog(self):
        # Opens the add lawyer page.
        self.add_case_dialog = AddCaseDialog(parent=self, connectDB=self.db)
        self.add_case_dialog.accepted.connect(self.load_case_info)
        self.add_case_dialog.exec_()

    def open_editCase_dialog(self):
        try:
            selected_row = self.display_case_info.currentRow()
            if selected_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to edit case information.")
                return
            # Fetch data from the selected row
            case_id = self.display_case_info.item(selected_row, 0).text().strip()
            case_name = self.display_case_info.item(selected_row, 1).text().strip()
            case_type = self.display_case_info.item(selected_row, 2).text().strip()
            case_start_date = self.display_case_info.item(selected_row, 3).text().strip()
            case_end_date = self.display_case_info.item(selected_row, 4).text().strip()
            case_status = self.display_case_info.item(selected_row, 5).text().strip()

            # Opens the edit case information page.
            self.edit_case_dialog = EditCaseDialog(parent=self, connectDB=self.db)
            self.edit_case_dialog.set_case_data(case_id, case_name, case_type, case_start_date,
                                                    case_end_date, case_status)
            self.edit_case_dialog.accepted.connect(self.load_case_info)
            self.edit_case_dialog.exec_()
        except Exception as E:
            print(str(E))


    def load_case_info(self):
        self.db.connect_database()
        try:
            # Fetch all case info from the database
            case_data = self.db.search_case_info()
            # Display case data in the table widget
            self.display_case_data(case_data)
        except Exception as E:
            print("Error:", E)
        finally:
            # Close the database connection
            self.db.connect.close()


    def search_case_info(self):
        # Search lawyer information
        self.db.connect_database()
        try:
            search_value = self.search_case.text().strip()
            search_results = self.db.search_case_info(search_value)
            self.display_case_data(search_results)
        except Exception as E:
            print(str(E))


    def display_case_data(self, case_data):
        # Clear exisiting table contents
        self.display_case_info.clearContents()
        self.display_case_info.setRowCount(0)
        self.display_case_info.verticalHeader().setVisible(False)
        headers = ["Case ID", "Case Name", "Case Type", "Start Date", "End Date", "Status"]
        # Set the horizontal header labels
        self.display_case_info.setHorizontalHeaderLabels(headers)
        if case_data:
            # Set the number of rows and columns based on the data
            self.display_case_info.setRowCount(len(case_data))
            self.display_case_info.setColumnCount(len(headers))

            # Populate the tablewidget with data
            for row_num, row_data in enumerate(case_data):
                for col_num, col_data in enumerate(row_data):
                    value = row_data[col_data]
                    self.display_case_info.setItem(row_num, col_num, QTableWidgetItem(str(value)))
            # Set the selection mode to single selection
            self.display_case_info.setSelectionMode(QAbstractItemView.SingleSelection)


    def delete_case_info(self):
        try:
            select_row = self.display_case_info.currentRow()
            if select_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to delete.")
                return

            # If a row is selected, get the case ID for confirmation
            case_id = self.display_case_info.item(select_row, 0).text().strip()

            # Ask for confirmation using a QMessageBox
            reply = QMessageBox.question(self, 'Delete Confirmation',
                                         f"Are you sure you want to delete a case with ID: {case_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # User confirmed deletion, proceed with deletion
                self.db.connect_database()  # Ensure database connection is open
                self.db.delete_case_info(case_id)  # Call a method in your database handler to delete

                # Optionally, you may want to remove the row from the table widget
                self.display_case_info.removeRow(select_row)

                # Inform the user with a QMessageBox
                QMessageBox.information(self, "Deletion Successful", f"Deleted a case with ID: {case_id}")

        except Exception as E:
            print("Error deleting case:", str(E))

        finally:
            # Reload the table after deleting.
            self.load_lawyer_info()
            self.db.connect.close()  # Ensure database connection is closed



    """
        Additional functionalities, no need to be changed unless necessary
        """

    @pyqtSlot()
    def on_exitButton_clicked(self):
        try:
            messageBox = QMessageBox(self)
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setWindowTitle("Exit Program")
            messageBox.setText("Are you sure you want to exit?")
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            reply = messageBox.exec_()

            if reply == QMessageBox.Yes:
                self.close()
            else:
                return
        except Exception as E:
            print(str(E))

    def change_system_page(self, btn):
        header_font = QFont("Poppins", 9)
        btn_text = btn.text().strip()
        if btn_text == self.show_lawyer_btn.text().strip():
            self.pages.setCurrentIndex(0)
            self.lawyer_table.horizontalHeader().setVisible(True)
            self.lawyer_table.horizontalHeader().setFont(header_font)
        elif btn_text == self.show_client_btn.text().strip():
            self.pages.setCurrentIndex(1)
            self.client_table.horizontalHeader().setVisible(True)
            self.client_table.horizontalHeader().setFont(header_font)
        elif btn_text == self.show_case_btn.text().strip():
            self.pages.setCurrentIndex(2)
            self.case_table.horizontalHeader().setVisible(True)
            self.case_table.horizontalHeader().setFont(header_font)
        elif btn_text == self.show_client_lawyer_btn.text().strip():
            self.pages.setCurrentIndex(3)






    """
    Class for Adding Lawyer
    """

class AddLawyerDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(AddLawyerDialog, self).__init__(parent)
        self.setWindowTitle("Add Lawyer")
        # Initialize the Add Student Dialog UI
        self.ui = Ui_addLawyer()
        self.ui.setupUi(self)
        self.connection = connectDB

        # Initialize buttons in add lawyer dialog
        self.ui.add_lawyer_info.clicked.connect(self.add_lawyer_action)
        self.ui.add_lawyer_cancel.clicked.connect(self.close)

    def add_lawyer_action(self):
        # Getting values of lawyer information
        test_idnumber = self.ui.lawyerIDinput.text().strip()
        test_name = self.ui.lawyerNameinput.text().strip()
        gender = self.ui.lawyerGenderCombo.currentText()
        position = self.ui.positionCombo.currentText()
        specialization = self.ui.specCombo.currentText()
        test_email = self.ui.lawyerEmail_input.text().strip()

        # Check if ID Number format is correct
        if len(test_idnumber) == 5 and sum(1 for c in test_idnumber if c.isdigit()) == 4 and any(
                c.isupper() for c in test_idnumber):
            idnumber = self.ui.lawyerIDinput.text().strip()
        else:
            QMessageBox.warning(self, "Validation Result", "ID number format is invalid. Use this sample ID format: 'A0013'")
            return

        try:  # Check if ID number already exists in the database
            if self.connection.lawyer_id_exists(idnumber):
                QMessageBox.warning(self, "Validation Result", "ID number already exists in the database.")
                return
        except Exception as E:
            print(str(E))

        # Check if name only consists of letters and is not blank
        if re.match(r"^[A-Za-z\s]+$", test_name) and test_name != "":
            name = self.ui.lawyerNameinput.text().strip()
        else:
            QMessageBox.warning(self, "Validation Result",
                                    "Name is blank or it contains numbers or special characters.")
            return

        # Check if email is valid
        if re.match(r"[^@]+@[^@]+\.[^@]+", test_email) and test_email != "":
               email = self.ui.lawyerEmail_input.text().strip()
        else:
            QMessageBox.warning(self, "Validation Result", "E-Mail is not valid. Please try again.")
            return
        # Finally add the information to the database
        reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with adding this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Add the information to the database
            self.connection.add_lawyer_info(idnumber, name, gender, position, specialization, email)
            QMessageBox.information(self, "Add Lawyer Information Success.",
                                        "Lawyer information has been added to the system.")
            self.accept()
        else:
            QMessageBox.information(self, "Operation Cancelled", "Adding lawyer information cancelled.")

    """
    Class for Editing Lawyer
    """

class EditLawyerDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(EditLawyerDialog, self).__init__(parent)
        self.setWindowTitle("Edit Lawyer Information")
        # Initialize the Add Student Dialog UI
        self.ui = Ui_editLawyer()
        self.ui.setupUi(self)
        self.ui.edit_LawyerID.setEnabled(False)
        # Initialize buttons in add lawyer dialog
        self.ui.edit_cancel_btn.clicked.connect(self.close)
        self.ui.edit_lawyer_info.clicked.connect(self.edit_lawyer_data)

        # Initialize connection to database
        self.connection = connectDB

    def set_lawyer_data(self, lawyer_id, lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization,
                            lawyer_email):
        self.ui.edit_LawyerID.setText(lawyer_id)
        self.ui.edit_LawyerName.setText(lawyer_name)
        self.ui.edit_LawyerGender.setCurrentText(lawyer_gender)
        self.ui.edit_Position.setCurrentText(lawyer_position)
        self.ui.edit_Specialization.setCurrentText(lawyer_specialization)
        self.ui.edit_LawyerEmail.setText(lawyer_email)

    def edit_lawyer_data(self):
        idnumber = self.ui.edit_LawyerID.text().strip()
        test_name = self.ui.edit_LawyerName.text().strip()
        gender = self.ui.edit_LawyerGender.currentText()
        position = self.ui.edit_Position.currentText()
        specialization = self.ui.edit_Specialization.currentText()
        test_email = self.ui.edit_LawyerEmail.text().strip()

        # Check if name only consists of letters and is not blank
        if re.match(r"^[A-Za-z\s]+$", test_name) and test_name != "":
            name = self.ui.edit_LawyerName.text().strip()
        else:
            QMessageBox.warning(self, "Validation Result",
                                    "Name is blank or it contains numbers or special characters.")
            return

        # Check if email is valid
        if re.match(r"[^@]+@[^@]+\.[^@]+", test_email) and test_email != "":
            email = self.ui.edit_LawyerEmail.text().strip()
        else:
            QMessageBox.warning(self, "Validation Result", "E-Mail is not valid. Please try again.")
            return
        
        # Finally add the information to the database
        reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with editing this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Add the information to the database
            self.connection.edit_lawyer_info(idnumber, name, gender, position, specialization, email)
            QMessageBox.information(self, "Update lawyer information success.",
                                        "Lawyer information has been edited to the system.")
            self.accept()
        else:
            QMessageBox.information(self, "Operation Cancelled", "Update lawyer information cancelled.")


"""
    Class for Adding Case
    """

class AddCaseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(AddCaseDialog, self).__init__(parent)
        self.setWindowTitle("Add Case")
        # Initialize the Add Case Dialog UI
        self.ui = Ui_addCase()
        self.ui.setupUi(self)
        self.connection = connectDB

        # Initialize buttons in Add Case dialog
        self.ui.add_case_info.clicked.connect(self.add_case_action)
        self.ui.add_case_cancel.clicked.connect(self.close)

    def add_case_action(self):
        try:
            # Getting values of case information
            test_idnumber = self.ui.caseIDinput.text().strip()
            test_name = self.ui.caseNameinput.text().strip()
            case_type = self.ui.caseType.currentText()
            startDate = self.ui.startDate.date()
            endDate = self.ui.endDate.text().strip()
            case_status = self.ui.caseStatus.currentText().strip()

            # Check if ID Number format is correct
            if len(test_idnumber) == 3 and sum(1 for c in test_idnumber if c.isdigit()) == 2 and any(
                    c.isupper() for c in test_idnumber):
                idnumber = self.ui.caseIDinput.text().strip()
            else:
                QMessageBox.warning(self, "Validation Result", "ID number format is invalid. A 3-character password consisting of a 'Capital Letter' and any two digits from 0'-9'. Use this sample ID format: 'A03'.")
                return

            try:  # Check if ID number already exists in the database
                if self.connection.case_id_exists(idnumber):
                    QMessageBox.warning(self, "Validation Result", "ID number already exists in the database. Please enter a different one.")
                    return
            except Exception as E:
                print(str(E))

            # Check if name only consists of letters and is not blank
            if re.match(r"^[A-Za-z\s]+$", test_name) and test_name != "":
                name = self.ui.caseNameinput.text().strip()
            else:
                QMessageBox.warning(self, "Validation Result",
                                        "Name is blank or it contains numbers or special characters.")
                return
              #Format dates to string (e.g., 'dd-MM-yyyy')
            startDate_str = startDate.toString("MM-dd-yyyy")
            endDate_str = str(endDate)

    
            # Finally add the information to the database
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with adding this information?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
            
                # Add the information to the database
                self.connection.add_case_info(idnumber, name, case_type, startDate_str, endDate_str, case_status)
                QMessageBox.information(self, "Add Case Information Success.",
                                            "Case information has been added to the system.")
                self.accept()
            else:
                QMessageBox.information(self, "Operation Cancelled", "Adding case information cancelled.")
        except Exception as E:
            print(str(E))



"""
    Class for Editing Case
    """

class EditCaseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(EditCaseDialog, self).__init__(parent)
        self.setWindowTitle("Edit Case Information")
        # Initialize the Edit Case Dialog UI
        self.ui = Ui_editCase()
        self.ui.setupUi(self)
        self.ui.caseIDinput_edit.setEnabled(False)

        # Initialize buttons in Edit Case dialog
        self.ui.edit_case_cancel.clicked.connect(self.close)
        self.ui.edit_case_info.clicked.connect(self.edit_case_data)

        # Initialize connection to database
        self.connection = connectDB

    def set_case_data(self, case_id, case_name, case_type, start_date, end_date, case_status):
        self.ui.caseIDinput_edit.setText(case_id)
        self.ui.caseNameinput_edit.setText(case_name)
        self.ui.caseType_edit.setCurrentText(case_type)
        start_date_qdate = QDate.fromString(start_date, "MM-dd-yyyy")
        self.ui.startDate_edit.setDate(start_date_qdate)
        self.ui.endDate.setText(end_date)
        self.ui.caseStatus_edit.setCurrentText(case_status)

    def edit_case_data(self):
        try:
            idnumber = self.ui.caseIDinput_edit.text().strip()
            test_name = self.ui.caseNameinput_edit.text().strip()
            case_type = self.ui.caseType_edit.currentText()
            start_date = self.ui.startDate_edit.date()
            end_date = self.ui.endDate.text().strip()
            case_status = self.ui.caseStatus_edit.currentText()

            # Check if name only consists of letters and is not blank
            if re.match(r"^[A-Za-z\s]+$", test_name) and test_name != "":
                name = self.ui.caseNameinput_edit.text().strip()
            else:
                QMessageBox.warning(self, "Validation Result",
                                        "Name is blank or it contains numbers or special characters.")
                return
        
            startDate_str = start_date.toString("MM-dd-yyyy")
            if end_date == "To be Determined":
                pass  # No further validation needed
            elif not re.match(r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$", end_date):
                QMessageBox.warning(self, "Validation Result",
                                "Invalid end date format. Please use MM-dd-yyyy or 'To be determined'.")
                return

            # Finally add the information to the database
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with editing this information?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Add the information to the database
                self.connection.edit_case_info(idnumber, name, case_type, startDate_str, end_date, case_status)
                QMessageBox.information(self, "Update edit information success.",
                                            "Edit information has been edited to the system.")
                self.accept()
            else:
                QMessageBox.information(self, "Operation Cancelled", "Update edit information cancelled.")
        except Exception as E:
            print(str(E))

         