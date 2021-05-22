# Works only for Python2.7

# https://mysqlclient.readthedocs.io/user_guide.html
import MySQLdb

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

user = 'root'
password = '1My_sql!SQL'

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd=password      # your password
                     )       # name of the data base

cursor = db.cursor()
print cursor

cursor.execute("SHOW DATABASES")
data = cursor.fetchall()
print(data)

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd=password,  # your password
                     db="books" )          # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# Use all the SQL you like
cur.execute("SELECT * FROM Books")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()

eng = create_engine('mysql://root:1My_sql!SQL@localhost:3306/car_rental')
print(eng)

base = declarative_base()

class Cars(base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)

    def __repr__(self):
       return '<Car: id={self.car_id}, producer={self.producer}, model={self.model}, year={self.year}, ' \
              'horse_power={self.horse_power}, price_per_day={self.price_per_day}>'

class Clients(base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)

class Bookings(base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    car_id = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Booking: id={self.booking_id}, client_id={self.client_id}, car_id={self.car_id}, " \
               "start_date={self.start_date}, end_date={self.end_date}, total_amount={self.total_amount}>"

base.metadata.create_all(eng)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()
client_1 = Clients(name='Jan', surname='Kowalski', address='ul. Florianska 12', city='Krakow')
car_1 = Cars(producer='Seat', model='Leon', year=2016, horse_power=80, price_per_day=200)

session.add(client_1)
session.add(car_1)
session.commit()

Session = sessionmaker(bind=eng)
session = Session()

for client in session.query(Clients).all():
    print(client)

for car in session.query(Cars).all():
    print(car)