from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float,Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime
Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    datetime = Column(DateTime, default=datetime.now())
    parameter_id = relationship("Parameter", backref = "account", cascade="all")


class Parameter(Base):
    __tablename__ = 'parameter'
    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, default=datetime.now())
    sharpness = Column(Float, nullable=False)
    fiber_type = Column(String(50), nullable=False)
    fiber_length = Column(String(50), nullable=False)
    producer = Column(String(50), nullable=False)
    fiber_number = Column(String(50), nullable=False)
    worker = Column(String(50), nullable=False)
    account_id = Column(Integer, ForeignKey('account.account_id'))
    result_id = relationship("Result", backref = "parameter")


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    core_diameter = Column(Float, nullable=False)
    clad_diameter = Column(Float, nullable=False)
    core_roundness = Column(Float, nullable=False)
    clad_roundness = Column(Float, nullable=False)
    concentricity = Column(Float, nullable=False)
    result_datetime = Column(Integer, ForeignKey('parameter.datetime'))

