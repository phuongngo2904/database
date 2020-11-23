import mysql.connector
import logging

def db():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="phuongngo",
        database="the_music_teacher")
    return mydb

def record():
    logging.root.setLevel(logging.NOTSET)
    logger = logging.getLogger("music")
    logging.basicConfig(filename='../Log/record.txt', level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
    return logger