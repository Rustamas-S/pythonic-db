
import MySQLdb
import logging

user = 'root'
password = '1My_sql!SQL'

db = MySQLdb.connect(host="localhost", user=user, passwd=password, db='cinematic')
print db

directors = [ ('Frank', 'Darabont', 7),
              ('Francis Ford', 'Coppola', 8),
              ('Quentin', 'Tarantino', 10),
              ('Christopher', 'Nolan', 9),
              ('David', 'Fincher', 7)]


shitf_ids = 25
movies = movies = [ ('The Shawshank Redemption', 1994, 'Drama', shitf_ids+1, 8),
                    ('The Green Mile', 1999, 'Drama', shitf_ids+1, 6),
                    ('The Godfather', 1972, 'Crime', shitf_ids+2, 7),
                    ('The Godfather III', 1990, 'Crime', shitf_ids+2, 6),
                    ('Pulp Fiction', 1994, 'Crime', shitf_ids+3, 9),
                    ('Inglourious Basterds', 2009, 'War', shitf_ids+3, 8),
                    ('The Dark Knight', 2008, 'Action', shitf_ids+4, 9),
                    ('Interstellar', 2014, 'Sci-fi', shitf_ids+4, 8),
                    ('The Prestige', 2006, 'Drama', shitf_ids+4, 10),
                    ('Fight Club', 1999, 'Drama', shitf_ids+5, 7),
                    ('Zodiac', 2007, 'Crime', shitf_ids+5, 5),
                    ('Seven', 1995, 'Drama', shitf_ids+5, 8),
                    ('Alien 3', 1992, 'Horror', shitf_ids+5, 5)]

logger = logging.getLogger('errorlog')
hdlr = logging.FileHandler('errors.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

#
# CREATE TABLE IF NOT EXISTS directors (
#     director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     name VARCHAR(30) NOT NULL,
#     surname VARCHAR(30) NOT NULL,
#     rating INT
#     );

def insert_directors(connection, directors):
    if not directors:
        return

    ##DELETE FROM directors;
    insert_sql = """
    INSERT INTO directors (name, surname, rating) VALUES(%s, %s, %s)"""
    connection.cursor().executemany(insert_sql, directors)
    connection.commit()

# CREATE TABLE IF NOT EXISTS movies (
#     movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     title VARCHAR(30),
#     year INT,
#     category VARCHAR(10),
#     director_id INT,
#     rating INT,
#       FOREIGN KEY (director_id) REFERENCES directors(director_id)
#     );

def insert_movies(connection, movies):
    if not movies:
        return
    insert_sql = """
    DELETE FROM movies;
    INSERT INTO movies (title, year, category, director_id, rating)
    VALUES(%s, %s, %s, %s, %s)"""
    connection.cursor().executemany(insert_sql, movies)
    connection.commit()

try:
    cursor = db.cursor()
    print cursor

    print "DB connect OK"

    insert_directors

    with db:
        insert_directors(db, directors)
        logger.info('DB OK: ' + " added)" )
        print directors

    cursor.execute("SELECT COUNT(*) FROM directors;")
    counter = cursor.fetchone()

    db.commit()
    print "DB tables OK, inserted %d" % counter

    with db:
        insert_movies(db, movies)
        logger.info('DB OK: ' + " added)")
        print movies

    cursor.execute("SELECT COUNT(*) FROM movies;")
    counter = cursor.fetchone()

    db.commit()
    print "DB tables OK, inserted %d" % counter

except Exception as e:

    logger.error('DB Error: ' + str(e))

