import mysql.connector

def connectDatabase(password, database=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=password,
            database=database,
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )

        return connection
        
    except mysql.connector.Error as error:
        if error.errno == 1045:
            print("Wrong username or password!")
        elif error.errno == 2059:
            print("Authentication error!")
        else:
            print("Database error:", error)
        return