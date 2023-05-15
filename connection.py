import mysql.connector

# Establish a connection to the MySQL server as root


def connect(database = "QA", host = "localhost", user = "root", password=""):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="QA"

    )
    return cnx

# Perform database operations...

def add_user_a(EU, EP, MEE):
    cnx = connect()
    cursor = cnx.cursor()
    query = "INSERT INTO UA (EU, EP, MEE) VALUES (%s, %s, %s)"
    values = (EU, EP, MEE)

    cursor.execute(query, values)

    cnx.commit()
    close(cnx)

def add_user_k(key):
    cnx = connect()
    cursor = cnx.cursor()
    query = "INSERT INTO EK (EK) VALUES (%s)"
    values = (key,)

    cursor.execute(query, values)

    cnx.commit()
    close(cnx)





# Close the connection

def close(cnx):
    cnx.close()


