"""Connecting to SQL server via python"""

"""connection enviroment variables"""
connection = connect(
        host = os.getenv("MYSQL_HOST"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        db = os.getenv("MYSQL_DATABASE"),
        charset = "utf8mb4" 
        )

"""Write and Read from sql"""
def write():
    try:
        with connection.cursor() as cursor:
            query = 'insert into..."
            cursor.execute(query)
        connection.commit()
    finally:
        connection.close() 


def read():
    try:
        with connection.cursor() as cursor:
            query = "Select * from..."
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()


