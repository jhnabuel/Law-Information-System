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
        query = "SELECT * FROM lawyer_table WHERE lawyerID = %s"
        self.cursor.execute(query, (lawyer_id,))
        result = self.cursor.fetchone()
        self.cursor.close()
        return result is not None

    def add_lawyer_info(self, lawyer_id, lawyer_name, lawyer_gender, lawyer_position, lawyer_specialization, lawyer_email):
        try:
            # Connect to database
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = """INSERT INTO lawyer_table (lawyerID, lawyerName, lawyerGender, lawyerPosition, lawyerSpecialization, lawyerEmail) 
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
        sql = "DELETE FROM lawyer_table WHERE lawyerID = %s;"
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
            query = f"""UPDATE lawyer_table
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
                               SELECT * FROM lawyer_table WHERE {condition};    
                           """
                self.cursor.execute(sql, (f"%{search_value}%", f"%{search_value}%", f"%{search_value}%",
                                          f"%{search_value}%", f"%{search_value}%"))      # Correct parameter passing

            else:
                # If no search value is provided, select all rows from the "lawyer" table and order by lawyerID
                sql = "SELECT * FROM lawyer_table ORDER BY lawyerID ASC;"
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


# Client
    def client_id_exists(self, client_id):
        # Checks whether ID exists in the database
        self.connect_database()
        query = "SELECT * FROM client_table WHERE clientID = %s"
        self.cursor.execute(query, (client_id,))
        result = self.cursor.fetchone()
        self.cursor.close()
        return result is not None

    def add_client_info(self, client_id, client_name, client_type, client_email, lawyer_name):
        try:
            self.connect_database()
            query = """INSERT INTO client_table (clientID, clientName, clientType, clientEmail, clientLawyer) 
                           VALUES (%s, %s, %s, %s, %s);"""
            self.cursor.execute(query, (client_id, client_name, client_type, client_email, lawyer_name))
            self.connect.commit()
            return None
        except Exception as e:
            self.connect.rollback()
            return str(e)
        finally:
            self.connect.close()

    def edit_client_info(self, client_id, client_name, client_type, client_email, lawyer_name):
        try:
            self.connect_database()
            query = """UPDATE client_table
                       SET clientName = %s, clientType = %s, clientEmail = %s, clientLawyer = %s
                       WHERE clientID = %s;"""
            self.cursor.execute(query, (client_name, client_type, client_email, lawyer_name, client_id))
            self.connect.commit()
            return None
        except Exception as e:
            self.connect.rollback()
            print(f"Error updating client info: {e}")
            return str(e)
        finally:
            self.connect.close()

    def delete_client_info(self, client_id):
        self.connect_database()
        sql = "DELETE FROM client_table WHERE clientID = %s;"
        try:
            self.cursor.execute(sql, (client_id,))
            self.connect.commit()
        except Exception as E:
            self.connect.rollback()
            return E
        finally:
            self.connect.close()

    def get_lawyer_names(self):
        try:
            self.connect_database()
            query = "SELECT lawyerName FROM lawyer_table;"
            self.cursor.execute(query)
            lawyer_names = [row['lawyerName'] for row in self.cursor.fetchall()]
            return lawyer_names
        except Exception as e:
            print(str(e))
            return []
        finally:
            self.connect.close()

    def get_case_names(self):
        try:
            self.connect_database()
            query = "SELECT case_name FROM case_table;"
            self.cursor.execute(query)
            case_names = [row['case_name'] for row in self.cursor.fetchall()]
            return case_names
        except Exception as e:
            print(str(e))
            return []
        finally:
            self.connect.close()
            
    def get_client_names(self):
        try:
            self.connect_database()
            query = "SELECT clientName FROM client_table;"
            self.cursor.execute(query)
            client_names = [row['clientName'] for row in self.cursor.fetchall()]
            return client_names
        except Exception as e:
            print(str(e))
            return []
        finally:
            self.connect.close()
        

    def search_client_info(self, search_value=None):
        try:
            columns = ["clientID", "clientName", "clientType", "clientEmail",
                           "clientLawyer"]

            if search_value:
                condition = "clientID LIKE %s OR clientName LIKE %s OR clientType LIKE %s OR clientEmail LIKE %s OR clientLawyer LIKE %s"
            else:
                condition = None
            if condition:
                sql = f"""        
                SELECT * FROM client_table WHERE {condition};
                """
                self.cursor.execute(sql, (
                f"%{search_value}%", f"%{search_value}%", f"%{search_value}%", f"%{search_value}%",
                f"%{search_value}%"))
            else:
                sql = "SELECT * FROM client_table ORDER BY clientID ASC;"
                self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except Exception as E:
            print(str(E))
        finally:
            self.connect.close()


# case
    def case_id_exists(self, case_id):
        # Checks whether ID exists in the database
        self.connect_database()
        query = "SELECT * FROM case_table WHERE case_id = %s"
        self.cursor.execute(query, (case_id,))
        result = self.cursor.fetchone()
        self.cursor.close()
        return result is not None
    

    def add_case_info(self, case_id, case_name, case_type, start_date, end_date, case_status):
        try:
            # Connect to database
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = """INSERT INTO case_table (case_id, case_name, case_type, start_date, end_date, case_status) 
                       VALUES (%s, %s, %s, %s, %s, %s);"""
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (case_id, case_name, case_type, start_date, end_date, case_status))
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


    def delete_case_info(self, case_id):
        self.connect_database()
        # Construct SQL query for deleting case info
        sql = "DELETE FROM case_table WHERE case_id = %s;"
        try:
            # Execute the SQL query for deleting case info
            self.cursor.execute(sql, (case_id,))
            self.connect.commit()
        except Exception as E:
            # Rollback the operation in a case of an error
            self.connect.rollback()
            return E
        finally:
            # Close the database connection
            self.connect.close()


    def edit_case_info(self, case_id, case_name, case_type, start_date, end_date, case_status):
        try:
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = f"""UPDATE case_table
                SET case_name = %s, case_type = %s, start_date = %s, end_date = %s, case_status = %s 
                       WHERE case_id = %s;"""
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (case_name, case_type, start_date, end_date, case_status, case_id))
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


    def search_case_info(self, search_value=None):
        try:
            # Define the columns to search in the "case" table
            columns = ["case_id", "case_name", "case_type", "case_status"]

            if search_value:
                # Create the search condition by joining each column with an
                # OR condition and using placeholders for the parameters
                condition = "case_id LIKE %s OR case_name LIKE %s OR case_type LIKE %s OR case_status LIKE %s"
                # Form the SQL query to select all rows from the "case" table
            else:
                condition = None

            if condition:
                sql = f"""
                               SELECT * FROM case_table WHERE {condition};    
                           """
                self.cursor.execute(sql, (f"%{search_value}%", f"%{search_value}%", f"%{search_value}%",
                                          f"%{search_value}%"))      # Correct parameter passing

            else:
                # If no search value is provided, select all rows from the "lawyer" table and order by lawyerID
                sql = "SELECT * FROM case_table ORDER BY case_id ASC;"
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

# lawyer case
    def get_lawyer_id(self, lawyer_name):
        try:
            self.connect_database()
            sql = """
                    SELECT lawyerID FROM lawyer_table WHERE lawyerName = %s;
                """
            self.cursor.execute(sql, (lawyer_name,))          
            lawyer_ID = self.cursor.fetchone()
            if lawyer_ID:
                return lawyer_ID['lawyerID']  # Return the ID if it exists
            else:
                return None  # Return None if no ID found
        
        except Exception as e:
            print(str(e))
            return None  # Return None in case of any exception
        finally:
            self.connect.close()


    def get_case_id(self, case_name):
        try:
            self.connect_database()
            sql = """
                    SELECT case_id FROM case_table WHERE case_name = %s;
                """
            self.cursor.execute(sql, (case_name,))            
            case_ID = self.cursor.fetchone()
            if case_ID:
                return case_ID['case_id']  # Return the ID if it exists
            else:
                return None  # Return None if no ID found

        except Exception as e:
            print(str(e))
            return None  # Return None in case of any exception
        finally:
            self.connect.close()

    def get_client_id(self, client_name):
        try:
            self.connect_database()
            sql = """
                    SELECT clientID FROM client_table WHERE clientName = %s;
                """
            self.cursor.execute(sql, (client_name,))            
            client_ID = self.cursor.fetchone()
            if client_ID:
                return client_ID['clientID']  # Return the ID if it exists
            else:
                return None  # Return None if no ID found

        except Exception as e:
            print(str(e))
            return None  # Return None in case of any exception
        finally:
            self.connect.close()


    def add_lawyer_case_info(self, lawyer_id, case_id, start_date):
        try:
            # Connect to database
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = """INSERT INTO lawyer_case_table (lawyer_id, case_id, start_date) 
                       VALUES (%s, %s, %s);"""
            
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (lawyer_id, case_id, start_date))
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


    def delete_lawyer_case_info(self, lawyer_id, case_id):
        self.connect_database()
        # Construct SQL query for deleting a specific row by unique identifier
        sql = "DELETE FROM lawyer_case_table WHERE lawyer_id = %s AND case_id = %s;"
        try:
            # Execute the SQL query for deleting lawyer case info
            self.cursor.execute(sql, (lawyer_id, case_id))
            self.connect.commit()
            return None
        except Exception as E:
            # Rollback the operation in a lawyer case of an error
            self.connect.rollback()
            return str(E)
        finally:
            # Close the database connection
            self.connect.close()


    def edit_lawyer_case_info(self, old_lawyer_id, new_lawyer_id, case_id, old_case_id, start_date):
        try:
            self.connect_database()
            # Update the lawyer_case_table with the new information
            query = """
                UPDATE lawyer_case_table
                SET lawyer_id = %s, case_id = %s, start_date = %s
                WHERE lawyer_id = %s AND case_id = %s;
            """
            self.cursor.execute(query, (new_lawyer_id, case_id, start_date, old_lawyer_id, old_case_id))
            self.connect.commit()
            return None  # Return None to indicate success
        except Exception as e:
            self.connect.rollback()
            return str(e)
        finally:
            self.connect.close()



    def search_lawyer_case_info(self, search_value=None):
        try:
            # Define the columns to search in the "case" table
            columns = ["lawyer_id", "case_id"]

            if search_value:
                # Create the search condition by joining each column with an
                # OR condition and using placeholders for the parameters
                condition = "lawyer_id LIKE %s OR case_id LIKE %s" 
                # Form the SQL query to select all rows from the "case" table
            else:
                condition = None

            if condition:
                sql = f"""
                    SELECT lawyer_table.lawyerName, case_table.case_name, lawyer_case_table.start_date
                    FROM lawyer_case_table
                    JOIN lawyer_table ON lawyer_case_table.lawyer_id = lawyer_table.lawyerID
                    JOIN case_table ON lawyer_case_table.case_id = case_table.case_id
                    WHERE lawyer_table.lawyerName LIKE %s OR case_table.case_name LIKE %s;
                """
                self.cursor.execute(sql, (f"%{search_value}%", f"%{search_value}%",))  # Correct parameter passing

            else:
                # If no search value is provided, select all rows from the "lawyer case" table and order by lawyer ID
                sql = """SELECT lawyer_table.lawyerName, case_table.case_name, lawyer_case_table.start_date 
                        FROM lawyer_case_table 
                        JOIN lawyer_table ON lawyer_case_table.lawyer_id = lawyer_table.lawyerID 
                        JOIN case_table ON lawyer_case_table.case_id = case_table.case_id; "
                    """
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
    
    def add_client_case_info(self, client_id, case_id):
        try:
            # Connect to database
            self.connect_database()
            # Prepare the SQL query with placeholders
            query = """INSERT INTO client_case_table (client_id, case_id) 
                       VALUES (%s, %s);"""
            
            # Execute the SQL query with the provided parameters
            self.cursor.execute(query, (client_id, case_id))
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


    def delete_client_case_info(self, client_id, case_id):
        self.connect_database()
        # Construct SQL query for deleting a specific row by unique identifier
        sql = "DELETE FROM client_case_table WHERE client_id = %s AND case_id = %s;"
        try:
            # Execute the SQL query for deleting lawyer case info
            self.cursor.execute(sql, (client_id, case_id))
            self.connect.commit()
            return None
        except Exception as E:
            # Rollback the operation in a lawyer case of an error
            self.connect.rollback()
            return str(E)
        finally:
            # Close the database connection
            self.connect.close()


    def edit_client_case_info(self, old_client_id, new_client_id, case_id, old_case_id):
        try:
            self.connect_database()
            # Update the lawyer_case_table with the new information
            query = """
                UPDATE client_case_table
                SET client_id = %s, case_id = %s
                WHERE client_id = %s AND case_id = %s;
            """
            self.cursor.execute(query, (new_client_id, case_id, old_client_id, old_case_id))
            self.connect.commit()
            return None  # Return None to indicate success
        except Exception as e:
            self.connect.rollback()
            return str(e)
        finally:
            self.connect.close()



    def search_client_case_info(self, search_value=None):
        try:
            # Define the columns to search in the "case" table
            columns = ["client_id", "case_id"]

            if search_value:
                # Create the search condition by joining each column with an
                # OR condition and using placeholders for the parameters
                condition = "client_id LIKE %s OR case_id LIKE %s" 
                # Form the SQL query to select all rows from the "case" table
            else:
                condition = None

            if condition:
                sql = f"""
                    SELECT client_table.clientName, case_table.case_name
                    FROM client_case_table
                    JOIN client_table ON client_case_table.client_id = client_table.clientID
                    JOIN case_table ON client_case_table.case_id = case_table.case_id
                    WHERE client_table.clientName LIKE %s OR case_table.case_name LIKE %s;
                """
                self.cursor.execute(sql, (f"%{search_value}%", f"%{search_value}%",))  # Correct parameter passing

            else:
                # If no search value is provided, select all rows from the "lawyer case" table and order by lawyer ID
                sql = """SELECT client_table.clientName, case_table.case_name
                    FROM client_case_table
                    JOIN client_table ON client_case_table.client_id = client_table.clientID
                    JOIN case_table ON client_case_table.case_id = case_table.case_id
                    """
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
