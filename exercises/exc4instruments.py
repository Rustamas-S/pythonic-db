
import MySQLdb
import logging

user = 'root'
password = '1My_sql!SQL'

db = MySQLdb.connect(host="localhost", user=user, passwd=password, db='music')

create_tables = """
CREATE TABLE IF NOT EXISTS instruments(
    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    family VARCHAR(30) NOT NULL,
    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
);
"""

def insert_instruments(connection, instrument_values):
    if not instrument_values:
        return
    insert_sql = """INSERT INTO instruments (name, family, difficulty) VALUES(%s, %s, %s)"""
    connection.cursor().executemany(insert_sql, instrument_values)
    connection.commit()

def get_instruments_count(connection):
    get_count_sql = """SELECT family, count(*) as count FROM instruments GROUP BY family;"""
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(get_count_sql)
    return cursor.fetchall()

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

    instruments = [
        ('guitar', 'strings', 'medium'),
        ('piano', 'keyboard', 'hard'),
        ('harp', 'strings', 'hard'),
        ('triangle', 'percussion', 'easy'),
        ('flute', 'woodwind', 'medium'),
        ('violin', 'string', 'medium'),
        ('tambourine', 'percussion', 'easy'),
        ('organ', 'keyboard', 'hard')]

    with db:
        insert_instruments(db, instruments)
        logger.info('DB OK: ' + " added)" )
        print instruments

        result = get_instruments_count(db)
        print( "%d instrument GROUPS in DB" %  len(result) )

#except Exception, e:
#similarly:

except Exception as e:
    logger.error('DB Error: ' + str(e))
