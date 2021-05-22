
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

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

try:

    for car in session.query(Cars).all():
        print(car)

except:
   # Rollback in case there is any error
   print "Error occurred"
