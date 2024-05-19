import mysql.connector
class ConnectDatabase:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.password = ""
        self.database = "law_firm_system"
        self.cursor = None

    def connect_database(self):
        self.connect = mysql.connector.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connect.cursor(dictionary=True)

    def lawyer_id_exists(self, lawyer_id):
        # Checks whether ID exists in the database
        self.connect_database()
        query = "SELECT * FROM lawyer WHERE lawyerID = %s"
        self.cursor.execute(query, (lawyer_id,))
        result = self.cursor.fetchone()
        self.cursor.close()
        return result is not None

    def add_lawyer_info(self, lawyer_id, lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization, lawyer_email):
        try:
            # Connect to database
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = """INSERT INTO lawyer (lawyerID, lawyerName, lawyerGender, lawyerPosition, lawyerSpecialization, lawyerEmail) 
                       VALUES (%s, %s, %s, %s, %s, %s);"""
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (lawyer_id, lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization, lawyer_email))
            # Commit the transaction to save the changes
            self.connect.commit()
            return None  # Return None to indicate success
        except Exception as e:
            # Rollback the transaction and return the error message
            self.connect.rollback()
            return str(e)
        finally:
            # Close the database connection
            self.connect.close()

    def delete_lawyer_info(self, lawyer_id):
        self.connect_database()
        # Construct SQL query for deleting student info
        sql = "DELETE FROM lawyer WHERE lawyerID = %s;"
        try:
            # Execute the SQL query for deleting student info
            self.cursor.execute(sql, (lawyer_id,))
            self.connect.commit()
        except Exception as E:
            # Rollback the operation in a case of an error
            self.connect.rollback()
            return E
        finally:
            # Close the database connection
            self.connect.close()

    def edit_lawyer_info(self, lawyer_id, lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization, lawyer_email):
        try:
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = f"""UPDATE lawyer
                SET lawyerName = %s, lawyerGender = %s, lawyerPosition = %s, lawyerSpecialization = %s, lawyerEmail = %s 
                       WHERE lawyerID = %s;"""
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization, lawyer_email, lawyer_id))
            # Commit the transaction to save the changes
            self.connect.commit()
            return None  # Return None to indicate success
        except Exception as e:
            # Rollback the transaction and return the error message
            self.connect.rollback()
            return str(e)
        finally:
            # Close the database connection
            self.connect.close()

    def search_lawyer_info(self, search_value=None):
        try:
            # Define the columns to search in the "lawyer" table
            columns = ["lawyerID", "lawyerName", "lawyerPosition", "lawyerSpecialization",
                       "lawyerEmail"]

            if search_value:
                # Create the search condition by joining each column with an
                # OR condition and using placeholders for the parameters
                condition = "lawyerID LIKE %s OR lawyerName LIKE %s OR lawyerPosition LIKE %s OR lawyerSpecialization LIKE %s OR lawyerEmail LIKE %s"
                # Form the SQL query to select all rows from the "lawyer" table
            else:
                condition = None

            if condition:
                sql = f"""
                               SELECT * FROM lawyer WHERE {condition};    
                           """
                self.cursor.execute(sql, (f"%{search_value}%", f"%{search_value}%", f"%{search_value}%",
                                          f"%{search_value}%", f"%{search_value}%"))      # Correct parameter passing

            else:
                # If no search value is provided, select all rows from the "lawyer" table and order by lawyerID
                sql = "SELECT * FROM lawyer ORDER BY lawyerID ASC;"
                # Execute the query without parameters
                self.cursor.execute(sql)

            # Fetch all the rows resulting from the query
            rows = self.cursor.fetchall()
            # Return the fetched rows
            return rows

        except Exception as E:
            # Print any exception that occurs
            print(str(E))

        finally:
            # Ensure the database connection is closed
            self.connect.close()

