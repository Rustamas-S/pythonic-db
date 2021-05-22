import sqlite3
import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

# Demo in-memory DB
db = sqlite3.connect(':memory:')
# https://docs.python.org/3/library/sqlite3.html

cursor = db.cursor()
print cursor

create_tables = """
CREATE TABLE instruments(
    instrument_id,
    name,
    family,
    difficulty ENUM NOT NULL
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
    cursor.execute(create_tables)
    db.commit()

    logger.info('DB OK: ' + create_tables + " executed.")

except Exception as e:

    logger.error('DB Error: ' + str(e))
