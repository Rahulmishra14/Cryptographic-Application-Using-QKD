import sqlite3
from logs.logging_service import generateLogs

conn = sqlite3.connect('BOB.db',check_same_thread=False)
cursor = conn.cursor()
def setup_db():
    try:
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS KEY_STORE (
            key TEXT
        );
        '''
        cursor.execute(create_table_query)
        generateLogs(f"DB Setup Scussefully!","INFO")
    except Exception as e:
        pass

def insert_data(query):
    try:
        cursor.execute(query)
        generateLogs(f"DATA INserted to db","INFO")
        conn.commit()
    except Exception as e:
        generateLogs(f"Error occurred {e}","INFO")


def get_data_from_db(table_name):
    try:
        select_query = f'SELECT * FROM {table_name};'
        cursor.execute(select_query)
        rows = cursor.fetchall()
        generateLogs(f"DATA INserted to db","INFO")
        return rows
    except Exception as e:
        generateLogs(f"Error occurred {e}","INFO")

def execute_query(query):
    try:
        cursor.execute(query)
    except Exception as e:
        generateLogs(f"Error occurred {e}","INFO")