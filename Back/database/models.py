import enum
from typing import List

from sqlalchemy import Column, Integer, String, DateTime,  Date, ForeignKey, Enum, DECIMAL, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy_utils import EmailType, URLType

from .database import Base

passanger_order_association = Table('passanger_to_order', Base.metadata,
                                    Column('passanger_id', Integer, ForeignKey('passanger.id')),
                                    Column('order_id', Integer, ForeignKey('order.id'))
                                    )


class StationType(enum.Enum):
    BUS = "Bus"
    TRAIN = "Train"
    AIRPORT = "Airport"


class CustomerGender(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class CompanyType(enum.Enum):
    AIRLINE = "Airline"
    RAILWAY = "Railway"
    BUS = "Bus"


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String)
    username = Column(String)
    hashed_password = Column(String)

    admin = relationship("Admin", uselist=False, back_populates="user")
    moderator = relationship("Moderator", uselist=False, back_populates="user")
    customer = relationship("Customer", uselist=False, back_populates="user")
    extranet = relationship("Extranet", uselist=False, back_populates="user")


class Moderator(Base):
    __tablename__ = 'moderator'

    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="moderator")

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    passangers = relationship("Passanger", back_populates="customer")
    user = relationship("User", back_populates="customer")
    orders = relationship("Order", back_populates='customer')


class Extranet(Base):
    __tablename__ = 'extranet'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="extranet")
    companies = relationship('Company', back_populates='extranet')


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="admin")


# *****************************************************************************************


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True,)

    name = Column(String, unique=True, nullable=False)

    regions = relationship("Region", back_populates="country")


class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True,)

    name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))

    country = relationship("Country", back_populates="regions")
    cities = relationship("City", back_populates="region")


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'))

    region = relationship("Region", back_populates="cities")
    stations = relationship("Station", back_populates="city")




# *****************************************************************************************


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=False)
    company_link = Column(URLType)
    company_type = Column(Enum(CompanyType), nullable=False)
    extranet_id = Column(Integer, ForeignKey('extranet.id'))

    tickets = relationship("Ticket", back_populates='company')
    fares = relationship("Fare", back_populates="company")
    trips = relationship("Trip", back_populates="company")
    extranet = relationship("Extranet", back_populates='companies')


class Fare(Base):
    __tablename__ = 'fare'

    id = Column(Integer, primary_key=True, index=True)

    price = Column(DECIMAL, nullable=False)
    description = Column(String, nullable=True)
    company_id = Column(Integer, ForeignKey("company.id"))
    departure_station_id = Column(Integer, ForeignKey('station.id'))
    arrival_station_id = Column(Integer, ForeignKey('station.id'))

    company = relationship("Company", back_populates='fares')
    departure_station = relationship("Station", back_populates="departure_fares",foreign_keys=[departure_station_id])
    arrival_station = relationship("Station", back_populates="arrival_fares",foreign_keys=[arrival_station_id])
    ticket = relationship("Ticket", back_populates="fare")



class Station(Base):
    __tablename__ = 'station'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    station_type = Column(Enum(StationType), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))

    city = relationship("City", back_populates="stations")
    departure_fares = relationship("Fare", back_populates="departure_station", foreign_keys=[Fare.departure_station_id])
    arrival_fares = relationship("Fare", back_populates="arrival_station",foreign_keys=[Fare.arrival_station_id] )


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)

    fare_id = Column(Integer, ForeignKey('fare.id'))
    company_id = Column(Integer, ForeignKey('company.id'))

    trip = relationship("Trip", back_populates="ticket")
    company = relationship("Company", back_populates='tickets')
    fare = relationship("Fare", back_populates='ticket')




class Trip(Base):
    __tablename__ = 'trip'

    id = Column(Integer, primary_key=True)

    ticket_id = Column(Integer, ForeignKey('ticket.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    departure_date = Column(DateTime)
    
    ticket_count = Column(Integer, nullable=True, default=50)

    ticket = relationship('Ticket', back_populates='trip')
    company = relationship('Company', back_populates='trips')
    order = relationship('Order', back_populates='trip')


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
 
 
    customer_id = Column(Integer, ForeignKey('customer.id'))
    trip_id = Column(Integer, ForeignKey('trip.id'))
    ticket_count = Column(Integer, nullable=False)
    

    passangers = relationship("Passanger", secondary=passanger_order_association, back_populates='orders')
    trip = relationship('Trip',  uselist=False, back_populates='order')
    customer = relationship('Customer', back_populates='orders',)
    


class Passanger(Base):
    __tablename__ = 'passanger'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    second_name = Column(String)
    gender = Column(Enum(CustomerGender))
    passport_series = Column(String)
    birthday = Column(Date)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    customer = relationship("Customer", back_populates='passangers')
    orders = relationship("Order", secondary=passanger_order_association, back_populates='passangers')
