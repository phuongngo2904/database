import mysql.connector
import time
import hashlib
from datetime import datetime
import logging

logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger("music")
logging.basicConfig(filename='Log/record.txt', level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
# Establish a connection
mydb=mysql.connector.connect( # change the host, user,password to your own sql workbench
    host="localhost",
    user="root",
    password="phuongngo")

# Cursor used to communicate with MySQL
logger.info('successfully connect to the database')
cursor=mydb.cursor()


# Open and read init_db script
# Separate statements by ';'
logger.info('Open and read SQL script')
with open('SQL/init_db.sql', encoding='UTF-8') as f:
    commands = f.read().split(';')

# Hash the password
password = "qwertyuiop"
hashed_password = hashlib.sha1(password.encode("UTF-8")).hexdigest()

for command in commands:
    if command.find('INSERT INTO user VALUES'):
        # Allow 1 second to pass to get different values
        time.sleep(1)
        now = datetime.now()
        # Set the MySQL session variables --> MySQL session different than connector session
        user_variables = {'user_password': hashed_password, 'user_date_created': now, 'user_last_login': now}
        mydb.reset_session(user_variables)
        cursor.execute(command)
        logger.info('executing command')
        mydb.commit()
    else:
        logger.info('executing command')
        cursor.execute(command)

mydb.commit()
logger.info('commited all changes to database')

with open('SQL/init_procedures.sql', encoding='UTF-8') as f:
    commands = f.read().split(';')