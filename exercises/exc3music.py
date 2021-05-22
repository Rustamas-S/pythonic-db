
import MySQLdb
import logging

user = 'root'
password = '1My_sql!SQL'

db = MySQLdb.connect(host="localhost", user=user, passwd=password)

create_database = """CREATE DATABASE IF NOT EXISTS music;USE music;"""
create_tables = """
CREATE TABLE instruments(
    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    family VARCHAR(30) NOT NULL,
    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
);
"""

logger = logging.getLogger('errorlog')
hdlr = logging.FileHandler('errors.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

try:
    cursor = db.cursor()
    cursor.execute(create_database)
    db.commit()

    logger.info('DB OK: ' + create_database + " executed.")

#except Exception, e:
#similarly:

except Exception as e:

    logger.error('DB Error: ' + str(e))

    #db.commit()
    #cursor.execute(create_tables)