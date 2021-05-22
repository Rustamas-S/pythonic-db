
import MySQLdb
import logging

user = 'root'
password = '1My_sql!SQL'

db = MySQLdb.connect(host="localhost", user=user, passwd=password)
print db

create_database = """CREATE DATABASE IF NOT EXISTS cinematic"""
use_database = "USE cinematic"

create_table_directors = """
CREATE TABLE IF NOT EXISTS directors (
    director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    rating INT
    );
"""

### https://www.w3schools.com/sql/sql_foreignkey.asp
create_table_movies = """
CREATE TABLE IF NOT EXISTS movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    title VARCHAR(30), 
    year INT, 
    category VARCHAR(10), 
    director_id INT, 
    rating INT,
      FOREIGN KEY (director_id) REFERENCES directors(director_id)
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
    print cursor

    cursor.execute(create_database)
    print "DB created OK"

    cursor.execute(use_database)
    print "DB select OK"

    logger.info('DB OK: ' + create_database + " executed.")

    cursor.execute(create_table_directors)
    logger.info('DB OK: ' + create_table_directors + " executed.")

    cursor.execute(create_table_movies)
    logger.info('DB OK: ' + create_table_movies + " executed.")

    db.commit()
    print "DB tables OK"

except Exception as e:

    logger.error('DB Error: ' + str(e))
