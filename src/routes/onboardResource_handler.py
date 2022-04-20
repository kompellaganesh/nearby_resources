from config import  config
from flask import request,make_response,copy_current_request_context
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database=config.configurations['database']['database'], 
   user=config.configurations['database']['user'], 
   password=config.configurations['database']['password'], 
   host=config.configurations['database']['host'], 
   port= config.configurations['database']['port']
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
def onboardResource():
    mydict={
        "status":"success"
    }
    return mydict

# def insertInDB(sql):
#     print(sql)
#     cursor.execute(sql)
#     id_of_new_row = cursor.fetchone()[0]
#     print(id_of_new_row)
#     return id_of_new_row

# def updateInDB(sql):
#     cursor.execute(sql)
