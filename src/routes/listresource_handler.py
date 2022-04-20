import psycopg2
from config import  config
from routes.onboardResource_handler import cursor
def listresources():
    return {
        "status":"success"
    }