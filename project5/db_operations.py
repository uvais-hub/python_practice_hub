import mysql.connector
from mysql.connector import Error

class DatabaseOperations:
    def __init__(self, host, user, password, database, port=3306):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("Successfully connected to the database")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            if query.strip().upper().startswith(("SELECT", "SHOW")):
                result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()

    def table_exists(self, table_name):
        query = "SHOW TABLES LIKE %s"
        result = self.execute_query(query, (table_name,))
        return len(result) > 0

    def create_table(self, table_name, columns):
        column_defs = ", ".join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
        self.execute_query(query)

    def insert_row(self, table_name, data):
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    def select_all(self, table_name):
        query = f"SELECT * FROM {table_name}"
        cursor = self.execute_query(query)
        return cursor.fetchall() if cursor else []

    def update_row(self, table_name, data, condition):
        set_clause = ", ".join([f"{k} = %s" for k in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.execute_query(query, tuple(data.values()))

    def delete_row(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)
    
    def insert_subject(self, subject_name):
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        affected_rows = self.execute_query(query, (subject_name,))
        if affected_rows:
            last_id = self.execute_query("SELECT LAST_INSERT_ID()")[0][0]
            return last_id
        return None

    def insert_chapter(self, subject_id, chapter_name):
        query = "INSERT INTO chapters (subject_id, chapter_name) VALUES (%s, %s)"
        affected_rows = self.execute_query(query, (subject_id, chapter_name))
        if affected_rows:
            last_id = self.execute_query("SELECT LAST_INSERT_ID()")[0][0]
            return last_id
        return None

    def insert_question(self, chapter_id, question_text, correct_answer):
        query = "INSERT INTO questions (chapter_id, question_text, correct_answer) VALUES (%s, %s, %s)"
        affected_rows = self.execute_query(query, (chapter_id, question_text, correct_answer))
        if affected_rows:
            last_id = self.execute_query("SELECT LAST_INSERT_ID()")[0][0]
            return last_id
        return None

    def insert_option(self, question_id, option_letter, option_text):
        query = "INSERT INTO options (question_id, option_letter, option_text) VALUES (%s, %s, %s)"
        self.execute_query(query, (question_id, option_letter, option_text))

    def insert_extracted_data(self, extracted_data):
        subject_id = self.insert_subject(extracted_data['subject'])
        if subject_id:
            for chapter in extracted_data['chapters']:
                chapter_id = self.insert_chapter(subject_id, chapter['name'])
                if chapter_id:
                    for qa in chapter['questions']:
                        question_id = self.insert_question(chapter_id, qa['question'], qa['answer'])
                        if question_id:
                            for option in qa['options']:
                                self.insert_option(question_id, option[0], option[2:])
        print("Extracted data inserted successfully")
