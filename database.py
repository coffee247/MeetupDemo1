import numpy as np
import pymysql, json
from PyQt5.QtCore import Qt
from pymysql import MySQLError


class database():

    def __init__(self):
        self.conn = pymysql.connections.Connection
        self.cur = pymysql.cursors.Cursor


    ''' Method to initialize a database at first run or just use it if existed already '''
    def Connect(self):
        config = json.loads(open('config.json').read())  # load database connection parameters from config.json
        try:
            self.conn = pymysql.connect(host=config["db_Host"], port=config["db_Port"], user=config["db_root_User"],
                                   password=config["db_root_PWD"], db=config["db_Name"])
        except MySQLError as e:  # error if connect failed:  ASSUME database does not exist ... create database
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            self.conn = pymysql.connect(host=config["db_Host"], port=config["db_Port"], user=config["db_root_User"],
                                   password=config["db_root_PWD"])
            with self.conn:
                dbname = config["db_Name"]  # see db_Name in config.json
                print("Creating database {}".format(dbname))
                query = f"CREATE DATABASE IF NOT EXISTS {dbname}"  # create the database (if it does not exist)
                cur = self.conn.cursor()
                cur.execute(query)
                query = f"USE {dbname}"  # use the database whose name is defined by db_Name in config.json
                cur.execute(query)
                sql = open("db_setup.sql")  # open file db_setup.sql (database schema creation script)
                sql = sql.read()  # read the schema
                sql = sql.split(';')  # split into individual commands at semicolons.
                for command in sql:
                    cur.execute(command)  # execute the schema creation script (one command at a time)
        return self


    '''method to get a reference to an open database connection'''
    def getConn(self):
        return self.conn

    '''method to execute a SEQUEL COMMAND passed as a STRING parameter by the calling function'''
    def db_doQuery(self, commandString):
        cur = self.conn.cursor()
        cur.execute(commandString)
        rows = cur.fetchall()
        return rows

    '''method to populate a view with data
    query example: "select * from personsTable order by lastname asc" '''
    def populateView(self, caller, query, orderBy_Field, idx, model):
        myself = caller
        with myself.conn:
            myself.colIndex = idx
            myself.model = model
            data = self.db_doQuery(query)
            dataShape = np.array(data).shape
            for i in range(dataShape[0]):
                myself.model.insertRows(i)
                index = myself.model.createIndex(i, 0)
                myself.model.setData(index, data[i][myself.colIndex], Qt.EditRole)



def getPersonData(caller):
    self = caller
    # Fetch list of persons
    with self.conn:
        query = f"select * from persons"
        data = self.dbase.db_doQuery(query)
        dataShape = np.array(data).shape
        for i in range(dataShape[0]):
            for j in range(dataShape[1]):
                index = self.personsModel.createIndex(i, j)
                self.personsModel.setData(index, data[i][j], Qt.EditRole)
    self.PersonsView.setColumnHidden(0, True)