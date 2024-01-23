import sqlite3
from sqlite3 import Error


def databaseConnect():
    path = "./opec_authomation.db"

    connect = None

    try:
        connect = sqlite3.connect(path)

    except Error as err:
        print(err)

    return connect


vconnect = databaseConnect()

name = input("Digite o seu Nome")
email = input("Digite o seu Email")
password = input("Digite uma senha segura!")
cpf = input("Digite seu CPF!")


USER_CREATE_SQL_QUERY = (
    "INSERT INTO users( NAME, EMAIL, PASSWORD, CPF) VALUES( '"
    + name
    + "', '"
    + email
    + "', '"
    + password
    + "', '"
    + cpf
    + "' );"
)


def createUser(connection, sql):
    try:
        con = connection.cursor()
        con.execute(sql)
        connection.commit()
        print(f"Create user succesfull")

    except Error as err:
        print(f"ERROR Create Table --->", err),


createUser(vconnect, USER_CREATE_SQL_QUERY)

vconnect.close()
