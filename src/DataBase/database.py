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


USER_SQL_QUERY = """CREATE TABLE users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(50),
    EMAIL VARCHAR(50),
    PASSWORD VARCHAR(50),
    CPF VARCHAR(14),
    TIMESTAMP DATE
);"""

CLIENT_SQL_QUERY = """CREATE TABLE clients(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    SOCIAL_REASON VARCHAR(80),
    FANTASY_NAME VARCHAR(80),
    CNPJ VARCHAR(18),
    IE VARCHAR(18),
    EMAIL VARCHAR(50),
    PHONE VARCHAR(10),
    ADDRESS VARCHAR(120),
    CITY VARCHAR(30),
    STATE VARCHAR(20),
    CEP VARCHAR(9),
    TIMESTAMP DATE
);"""

PI_SQL_QUERY = """CREATE TABLE pis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NUMBER INTEGER,
    DATE_OF_ISSUE DATE,
    PIT_NUMBER VARCHAR(13),
    PLAN_NUMBER VARCHAR(13),
    SPREADSHEET INTEGER,
    START_DATE DATE,
    END_DATE DATE,
    GROSS_VALUE FLOAT,
    NET_VALUE FLOAT,
    COMMISSION_VALUE FLOAT,
    CLIENT_ID INTEGER REFERENCES clients(ID),
    TIMESTAMP DATE 
);"""


def createTable(connection, sql):
    try:
        con = connection.cursor()
        con.execute(sql)
        print(f"Create table succesfull")

    except Error as err:
        print(f"ERROR Create Table --->", err)


createTable(vconnect, USER_SQL_QUERY)

createTable(vconnect, CLIENT_SQL_QUERY)

createTable(vconnect, PI_SQL_QUERY)

vconnect.close()
