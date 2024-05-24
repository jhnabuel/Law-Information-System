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

from ui.addClient import Ui_addClient
from ui.editClient import Ui_editClient

from ui.addLawyerCase import Ui_addLawyerCase
from ui.editLawyerCase import Ui_editLawyerCase

from ui.addClientCase import Ui_addClientCase
from ui.editClientCase import Ui_editClientCase


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

        """
        Initialization for client page
        """
        self.addclientbtn = self.ui.addClient
        self.deleteclientbtn = self.ui.deleteClient
        self.editclientbtn = self.ui.editClient
        self.display_client_info = self.ui.clientDisplay
        self.search_client = self.ui.searchClient
        self.search_client.textChanged.connect(self.search_client_info)

        """
        Initialization for lawyer case page
        """

        self.addlawyercasebtn = self.ui.add_lawyercase_btn 
        self.deletelawyercasebtn = self.ui.delete_lawyer_case
        self.editlawyercasebtn = self.ui.edit_lawyer_case
        self.display_lawyer_case_info = self.ui.lawyer_case_display
        self.search_lawyer_case = self.ui.search_lawyer_case
        self.search_lawyer_case.textChanged.connect(self.search_lawyer_case_info)


        # Load lawyer table
        self.load_lawyer_info()

        # Load case table
        self.load_case_info()

        # Load client table
        self.load_client_info()

        # Load lawyer case table
        self.load_lawyer_case_info()

        # Initialize the buttons for each page
        self.init_signal_slot()


    def init_signal_slot(self):
        # Initizalizes all buttons inside each page
        self.addlawyerbtn.clicked.connect(self.open_addlawyer_dialog)
        self.deletelawyerbtn.clicked.connect(self.delete_lawyer_info)
        self.editlawyerbtn.clicked.connect(self.open_editLawyer_dialog)
        self.addcasebtn.clicked.connect(self.open_addcase_dialog)
        self.deletecasebtn.clicked.connect(self.delete_case_info)
        self.editcasebtn.clicked.connect(self.open_editCase_dialog)
        self.addclientbtn.clicked.connect(self.open_addclient_dialog)
        self.deleteclientbtn.clicked.connect(self.delete_client_info)
        self.editclientbtn.clicked.connect(self.open_editclient_dialog)
        self.addlawyercasebtn.clicked.connect(self.open_addlawyercase_dialog)
        self.deletelawyercasebtn.clicked.connect(self.delete_lawyer_case_info)
        self.editlawyercasebtn.clicked.connect(self.open_editlawyerCase_dialog)


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
        self.load_client_info()

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
                                         f"Are you sure you want to delete lawyer with ID: {lawyer_id}? This will affect"
                                         f"other tables in the system.",
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
            self.load_client_info()
            self.db.connect.close()  # Ensure database connection is closed

# Client
    def open_addclient_dialog(self):
        # Opens the add client page.
        self.add_client_dialog = AddClientDialog(parent=self, connectDB=self.db)
        self.add_client_dialog.accepted.connect(self.load_client_info)
        self.add_client_dialog.exec_()

    def open_editclient_dialog(self):
        try:
            selected_row = self.display_client_info.currentRow()
            if selected_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to edit client information.")
                return
            # Fetch data from the selected row
            client_id = self.display_client_info.item(selected_row, 0).text().strip()
            client_name = self.display_client_info.item(selected_row, 1).text().strip()
            client_type = self.display_client_info.item(selected_row, 2).text().strip()
            client_email = self.display_client_info.item(selected_row, 3).text().strip()
            lawyer_name = self.display_client_info.item(selected_row, 4).text().strip()

            # Opens the edit client information page.
            self.edit_client_dialog = EditClientDialog(parent=self, connectDB=self.db)
            self.edit_client_dialog.set_client_data(client_id, client_name, client_type, client_email,
                                                        lawyer_name)
            self.edit_client_dialog.accepted.connect(self.load_client_info)
            self.edit_client_dialog.exec_()
        except Exception as E:
            print(str(E))

    def load_client_info(self):
        self.db.connect_database()
        try:
            # Fetch all client info from the database
            client_data = self.db.search_client_info()
            # Display client data in the table widget
            self.display_client_data(client_data)
        except Exception as E:
            print("Error:", E)
        finally:
            # Close the database connection
            self.db.connect.close()

    def search_client_info(self):
        # Search client information
        self.db.connect_database()
        try:
            search_value = self.search_client.text().strip()
            search_results = self.db.search_client_info(search_value)
            self.display_client_data(search_results)
        except Exception as E:
            print(str(E))

    def display_client_data(self, client_data):
        # Clear exisiting table contents
        self.display_client_info.clearContents()
        self.display_client_info.setRowCount(0)
        self.display_client_info.verticalHeader().setVisible(False)
        headers = ["Client ID", "Name", "Type", "E-Mail", "Assigned Lawyer"]
        # Set the horizontal header labels
        self.display_client_info.setHorizontalHeaderLabels(headers)
        if client_data:
            # Set the number of rows and columns based on the data
            self.display_client_info.setRowCount(len(client_data))
            self.display_client_info.setColumnCount(len(headers))

            # Populate the tablewidget with data
            for row_num, row_data in enumerate(client_data):
                for col_num, col_data in enumerate(row_data):
                    value = row_data[col_data]
                    self.display_client_info.setItem(row_num, col_num, QTableWidgetItem(str(value)))
            # Set the selection mode to single selection
            self.display_client_info.setSelectionMode(QAbstractItemView.SingleSelection)

    def delete_client_info(self):
        try:
            select_row = self.display_client_info.currentRow()
            if select_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to delete.")
                return

            # If a row is selected, get the Client ID for confirmation
            client_id = self.display_client_info.item(select_row, 0).text().strip()

            # Ask for confirmation using a QMessageBox
            reply = QMessageBox.question(self, 'Delete Confirmation',
                                             f"Are you sure you want to delete client with ID: {client_id}?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # User confirmed deletion, proceed with deletion
                self.db.connect_database()  # Ensure database connection is open
                self.db.delete_client_info(client_id)  # Call a method in your database handler to delete

                # Optionally, you may want to remove the row from the table widget
                self.display_client_info.removeRow(select_row)

                # Inform the user with a QMessageBox
                QMessageBox.information(self, "Deletion Successful", f"Deleted client with ID: {client_id}")

        except Exception as E:
            print("Error deleting client:", str(E))

        finally:
            # Reload the table after deleting.
            self.load_client_info()
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
            self.load_case_info()
            self.db.connect.close()  # Ensure database connection is closed


# lawyer case
    def open_addlawyercase_dialog(self):
        # Opens the add lawyer page.
        self.add_lawyer_case_dialog = AddLawyerCaseDialog(parent=self, connectDB=self.db)
        self.add_lawyer_case_dialog.accepted.connect(self.load_lawyer_case_info)
        self.add_lawyer_case_dialog.exec_()

    def open_editlawyerCase_dialog(self):
        try:
            selected_row = self.display_lawyer_case_info.currentRow()
            if selected_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to edit lawyer case information.")
                return
            # Fetch data from the selected row
            lawyer_name = self.display_lawyer_case_info.item(selected_row, 0).text().strip()
            case_name = self.display_lawyer_case_info.item(selected_row, 1).text().strip()
            start_date = self.display_lawyer_case_info.item(selected_row, 2).text().strip()
            
            # Opens the edit case information page.
            self.edit_lawyer_case_dialog = EditLawyerCaseDialog(parent=self, connectDB=self.db)
            self.edit_lawyer_case_dialog.set_lawyer_case_data(lawyer_name, case_name, start_date)
            self.edit_lawyer_case_dialog.accepted.connect(self.load_lawyer_case_info)
            self.edit_lawyer_case_dialog.exec_()
        except Exception as E:
            print(str(E))


    def load_lawyer_case_info(self):
        self.db.connect_database()
        try:
            # Fetch all case info from the database
            lawyer_case_data = self.db.search_lawyer_case_info()
            # Display case data in the table widget
            self.display_lawyer_case_data(lawyer_case_data)
        except Exception as E:
            print("Error:", E)
        finally:
            # Close the database connection
            self.db.connect.close()


    def search_lawyer_case_info(self):
        # Search lawyer information
        self.db.connect_database()
        try:
            search_value = self.search_lawyer_case.text().strip()
            search_results = self.db.search_lawyer_case_info(search_value)
            self.display_lawyer_case_data(search_results)
        except Exception as E:
            print(str(E))


    def display_lawyer_case_data(self, lawyer_case_data):
        # Clear exisiting table contents
        self.display_lawyer_case_info.clearContents()
        self.display_lawyer_case_info.setRowCount(0)
        self.display_lawyer_case_info.verticalHeader().setVisible(False)
        headers = ["Lawyer Name", "Case Name", "Start Date"]
        # Set the horizontal header labels
        self.display_lawyer_case_info.setHorizontalHeaderLabels(headers)
        if lawyer_case_data:
            # Set the number of rows and columns based on the data
            self.display_lawyer_case_info.setRowCount(len(lawyer_case_data))
            self.display_lawyer_case_info.setColumnCount(len(headers))

            # Populate the tablewidget with data
            for row_num, row_data in enumerate(lawyer_case_data):
                for col_num, col_data in enumerate(row_data):
                    value = row_data[col_data]
                    self.display_lawyer_case_info.setItem(row_num, col_num, QTableWidgetItem(str(value)))
            # Set the selection mode to single selection
            self.display_lawyer_case_info.setSelectionMode(QAbstractItemView.SingleSelection)


    def delete_lawyer_case_info(self):
        try:
            select_row = self.display_lawyer_case_info.currentRow()
            if select_row == -1:
                # If no row is selected, show a message box informing the user
                QMessageBox.information(self, "No Row Selected", "Please select a row to delete.")
                return

            # If a row is selected, get the lawyer_ ID for confirmation
            lawyer_id = self.display_lawyer_case_info.item(select_row, 0).text().strip()

            # Ask for confirmation using a QMessageBox
            reply = QMessageBox.question(self, 'Delete Confirmation',
                                         f"Are you sure you want to delete a case with an Assigned Lawyer: {lawyer_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # User confirmed deletion, proceed with deletion
                self.db.connect_database()  # Ensure database connection is open
                self.db.delete_lawyer_case_info(lawyer_id)  # Call a method in your database handler to delete

                # Optionally, you may want to remove the row from the table widget
                self.display_lawyer_case_info.removeRow(select_row)

                # Inform the user with a QMessageBox
                QMessageBox.information(self, "Deletion Successful", f"Deleted a case with an Assigned Lawyer: {lawyer_id}")

        except Exception as E:
            print("Error deleting lawyer case:", str(E))

        finally:
            # Reload the table after deleting.
            self.load_lawyer_case_info()
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


"""
   Class for Adding Client
   """


class AddClientDialog(QtWidgets.QDialog):
    try:
        def __init__(self, parent, connectDB):
            super(AddClientDialog, self).__init__(parent)
            self.setWindowTitle("Add Client")
            # Initialize the Add Client Dialog UI
            self.ui = Ui_addClient()
            self.ui.setupUi(self)
            self.connection = connectDB

            self.populate_lawyer_combo()

            # Initialize buttons in add client dialog
            self.ui.add_client_info.clicked.connect(self.add_client_action)
            self.ui.add_lawyer_cancel_2.clicked.connect(self.close)

        def populate_lawyer_combo(self):
            try:
                lawyer_names = self.connection.get_lawyer_names()
                self.ui.assignedLawyerCombo.clear()
                self.ui.assignedLawyerCombo.addItems(lawyer_names)
            except Exception as E:
                print(str(E) + "line A")

        def add_client_action(self):
            try:
                # Getting values of client information
                test_idnumber = self.ui.clientIDinput.text().strip()
                test_name = self.ui.clientNameinput.text().strip()
                client_type = self.ui.clientTypeCombo.currentText()
                client_lawyer = self.ui.assignedLawyerCombo.currentText()
                test_email = self.ui.clientEmail.text().strip()

                # Check if ID Number format is correct
                if len(test_idnumber) == 5 and sum(1 for c in test_idnumber if c.isdigit()) == 4 and any(
                        c.isupper() for c in test_idnumber):
                    idnumber = self.ui.clientIDinput.text().strip()
                else:
                    QMessageBox.warning(self, "Validation Result", "ID number format is invalid.")
                    return

                try:
                    # Check if ID number already exists in the database
                    if self.connection.client_id_exists(idnumber):
                        QMessageBox.warning(self, "Validation Result", "ID number already exists in the database.")
                        return
                except Exception as E:
                    print(str(E))

                # Check if name only consists of letters and is not blank
                if re.match(r"^[A-Za-z\s]+$", test_name) and test_name != "":
                    name = self.ui.clientNameinput.text().strip()
                else:
                    QMessageBox.warning(self, "Validation Result",
                                        "Name is blank or it contains numbers or special characters.")
                    return

                    # Check if email is valid
                if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", test_email) and test_email != "":
                    email = self.ui.clientEmail.text().strip()
                else:
                    QMessageBox.warning(self, "Validation Result", "E-Mail is not valid. Please try again.")
                    return

                # Finally add the information to the database
                reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with adding this information?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    # Add the information to the database
                    self.connection.add_client_info(idnumber, name, client_type, email, client_lawyer)
                    QMessageBox.information(self, "Add Client Information Success",
                                            "Client information has been added to the system.")
                    self.accept()
                else:
                    QMessageBox.information(self, "Operation Cancelled", "Adding client information cancelled.")
            except Exception as E:
                print(str(E) + "line B")
    except Exception as E:
        print(str(E) + "line C")


"""
    Class for Editing Client
    """


class EditClientDialog(QtWidgets.QDialog):
    try:
        def __init__(self, parent, connectDB):
            super(EditClientDialog, self).__init__(parent)
            self.setWindowTitle("Edit Client Information")
            # Initialize the Add Student Dialog UI
            self.ui = Ui_editClient()
            self.ui.setupUi(self)
            self.ui.clientIDinput_edit.setEnabled(False)
            # Initialize buttons in add lawyer dialog
            self.ui.edit_lawyer_cancel.clicked.connect(self.close)
            self.ui.edit_client_info.clicked.connect(self.edit_client_data)

            # Initialize connection to database
            self.connection = connectDB
            self.populate_lawyer_combo()

        def populate_lawyer_combo(self):
            lawyer_names = self.connection.get_lawyer_names()
            self.ui.assignedLawyerCombo_edit.clear()
            self.ui.assignedLawyerCombo_edit.addItems(lawyer_names)

        def set_client_data(self, client_id, client_name, client_type, client_email, lawyer_name):
            self.ui.clientIDinput_edit.setText(client_id)
            self.ui.clientNameinput_edit.setText(client_name)
            self.ui.clientTypeCombo_edit.setCurrentText(client_type)
            self.ui.assignedLawyerCombo_edit.setCurrentText(lawyer_name)
            self.ui.clientEmail_edit.setText(client_email)

        def edit_client_data(self):
            idnumber = self.ui.clientIDinput_edit.text().strip()
            name = self.ui.clientNameinput_edit.text().strip()
            client_type = self.ui.clientTypeCombo_edit.currentText()
            lawyer_name = self.ui.assignedLawyerCombo_edit.currentText()  # Get lawyer name from UI
            test_email = self.ui.clientEmail_edit.text().strip()


            # Check if name only consists of letters and is not blank
            if re.match(r"^[A-Za-z\s]+$", name) and name != "":
                name = self.ui.clientNameinput_edit.text().strip()
            else:
                QMessageBox.warning(self, "Validation Result",
                                    "Name is blank or it contains numbers or special characters.")
                return

            # Check if email is valid
            if re.match(r"[^@]+@[^@]+\.[^@]+", test_email) and test_email != "":
                client_email = self.ui.clientEmail_edit.text().strip()
            else:
                QMessageBox.warning(self, "Validation Result", "E-Mail is not valid. Please try again.")
                return

            # Confirmation prompt before editing
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with editing this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Edit information in the database
                if self.connection.edit_client_info(idnumber, name, client_type, client_email,
                                                    lawyer_name):  # Check for successful edit
                    QMessageBox.information(self, "Update Client Information Success.",
                                            "Client information has been edited to the system.")
                    print(idnumber, name, client_type, lawyer_name,
                                                    client_email)
                else:
                    QMessageBox.warning(self, "Update Failed", "An error occurred while updating client information.")
                self.accept()
            else:
                QMessageBox.information(self, "Operation Cancelled", "Update client information cancelled.")

    except Exception as E:
        print(str(E) + "ERROR")

         

"""
    Class for Adding Lawyer Case
    """

class AddLawyerCaseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(AddLawyerCaseDialog, self).__init__(parent)
        self.setWindowTitle("Add Lawyer Case")
        # Initialize the Add Lawyer Case Dialog UI
        self.ui = Ui_addLawyerCase()
        self.ui.setupUi(self)
        self.connection = connectDB
        self.populate_combo()

        # Initialize buttons in Add Lawyer Case dialog
        self.ui.add_info.clicked.connect(self.add_lawyer_case_action)
        self.ui.add_info_cancel.clicked.connect(self.close)

    def populate_combo(self):
        try:
            lawyer_names = self.connection.get_lawyer_names()
            case_names = self.connection.get_case_names()
            self.ui.assigned_lawyer_combo.clear()
            self.ui.assigned_lawyer_combo.addItems(lawyer_names)
            self.ui.case_name_combo.clear()
            self.ui.case_name_combo.addItems(case_names)

        except Exception as E:
            print(str(E) + "line A")

 
    def add_lawyer_case_action(self):
        try:
            # Getting values of case information
            test_idnumber = self.ui.assigned_lawyer_combo.currentText() # Get lawyer ID
            test_idnumber2 = self.ui.case_name_combo.currentText()      # Get case ID
            start_date = self.ui.lawyer_start_date.date()               # Get start date input
            lawyer_id = self.connection.get_lawyer_id(test_idnumber)
            case_id = self.connection.get_case_id(test_idnumber2)

            #Format start date to string 
            startDate_str = start_date.toString("MM-dd-yyyy")

            # Finally add the information to the database
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with adding this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                result = self.connection.add_lawyer_case_info(lawyer_id, case_id, startDate_str)
                if result is None:
                    QMessageBox.information(self, "Add Lawyer Case Information Success",
                                            "A Lawyer Case information has been added to the system.")
                    self.accept()

                else:
                    QMessageBox.warning(self, "Error", f"Failed to add data: {result}")
            else:
                QMessageBox.information(self, "Operation Cancelled", "Adding lawyer case information cancelled.")
        except Exception as E:
            print(str(E))


"""
    Class for Editing Lawyer Case
    """

class EditLawyerCaseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(EditLawyerCaseDialog, self).__init__(parent)
        self.setWindowTitle("Edit Lawyer Case Information")
        # Initialize the Edit Lawyer Case Dialog UI
        self.ui = Ui_editLawyerCase()
        self.ui.setupUi(self)
        self.connection = connectDB
        self.populate_combo()
        

        # Initialize buttons in Edit Lawyer Case dialog
        self.ui.edit_info_cancel.clicked.connect(self.close)
        self.ui.edit_info.clicked.connect(self.edit_lawyer_case_data)


    def populate_combo(self):
        try:
            lawyer_names = self.connection.get_lawyer_names()
            case_names = self.connection.get_case_names()
            self.ui.edit_assigned_lawyer_combo.clear()
            self.ui.edit_assigned_lawyer_combo.addItems(lawyer_names)
            self.ui.case_name_combo.clear()
            self.ui.case_name_combo.addItems(case_names)

        except Exception as E:
            print(str(E) + "line A")

    def set_lawyer_case_data(self, lawyer_name, case_name, start_date):
        self.ui.edit_assigned_lawyer_combo.setCurrentText(lawyer_name)
        self.ui.case_name_combo.setCurrentText(case_name)
        start_date_qdate = QDate.fromString(start_date, "MM-dd-yyyy")
        self.ui.edit_lawyer_start_date.setDate(start_date_qdate)
       
    def edit_lawyer_case_data(self):
        try:
            lawyerName = self.ui.edit_assigned_lawyer_combo.currentText()
            caseName = self.ui.case_name_combo.currentText()
            start_date = self.ui.edit_lawyer_start_date.date()
            lawyer_id = self.connection.get_lawyer_id(lawyerName)
            case_id = self.connection.get_case_id(caseName)
       
            startDate_str = start_date.toString("MM-dd-yyyy")

            # Finally add the information to the database
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with editing this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Add the information to the database
                result = self.connection.edit_lawyer_case_info(lawyer_id, case_id, startDate_str)
                if result is None:
                    QMessageBox.information(self, "Update edit information success.",
                                            "Edit information has been edited to the system.")
                    self.accept()

                else:
                    QMessageBox.warning(self, "Error", f"Failed to edit data: {result}")
            else:
                QMessageBox.information(self, "Operation Cancelled", "Update edit information cancelled.")
        except Exception as E:
            print(str(E))


"""
    Class for Adding Client Case
    """

class AddClientCaseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connectDB):
        super(AddClientCaseDialog, self).__init__(parent)
        self.setWindowTitle("Add Client Case")
        # Initialize the Add Client Case Dialog UI
        self.ui = Ui_addClientCase()
        self.ui.setupUi(self)
        self.connection = connectDB

        # Initialize buttons in Add Client Case dialog
        self.ui.add_client_case_info.clicked.connect(self.add_client_case_action)
        self.ui.add_client_case_cancel.clicked.connect(self.close)

    def add_client_case_action(self):
        try:
            # Getting values of case information
            test_idnumber = self.ui.client_name_combo.currentText()
            test_idnumber2 = self.ui.client_case_combo.currentText()      
       
            # Finally add the information to the database
            reply = QMessageBox.question(self, 'Confirmation', 'Do you want to proceed with adding this information?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
            
            # Add the information to the database
                self.connection.add_lawyer_case_info(test_idnumber, test_idnumber2)
                QMessageBox.information(self, "Add Client Case Information Success.",
                                        "A Client Case information has been added to the system.")
                self.accept()
            else:
                QMessageBox.information(self, "Operation Cancelled", "Adding client case information cancelled.")
        except Exception as E:
            print(str(E))

