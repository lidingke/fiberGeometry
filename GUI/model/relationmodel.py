import pdb

from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from setting.parameter import SQLALCHEMY_DIR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    job_id = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)

    password = Column(String(200), nullable=False)
    add_time = Column(DateTime, default=datetime.now())
    resultcontext = relationship("ResultContext", back_populates="account")

    def __repr__(self):
        return "{}_{}".format(self.name,self.job_id)


class ResultContext(Base):
    __tablename__ = 'resultcontext'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sharpindex = Column(Float, nullable=False)
    fiber_type = Column(String(50), default="test")
    fiber_producer = Column(String(50), nullable=False)
    fiber_number = Column(String(50), default="001")
    fiber_length = Column(Float, nullable=False)
    instrument = Column(String(50), nullable=False)
    add_time = Column(DateTime, default=datetime.now())

    #relations:up
    worker = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="resultcontext")
    #relations:down
    cvresult = relationship("CVResult", back_populates="cvcontext")
    opresult = relationship("OPResult", back_populates="opcontext")


    def __repr__(self):
        return "{}_{}".format(self.instrument,self.id,self.account)

class CVResult(Base):
    __tablename__ = 'cvresults'
    id = Column(Integer, primary_key=True, autoincrement=True)
    corediameter = Column(Float, nullable=False)
    claddiameter = Column(Float, nullable=False)
    coreroundness = Column(Float, nullable=False)
    cladroundness = Column(Float, nullable=False)
    concentricity = Column(Float, nullable=False)

    cvresult_id = Column(Integer, ForeignKey('resultcontext.id'))
    cvcontext = relationship("ResultContext", back_populates="cvresult")

    def __repr__(self):
        return "{}um,{}um,{}um,{}um,{}".format(
            self.corediameter,self.claddiameter,
            self.coreroundness,self.cladroundness,
            self.concentricity
        )


class OPResult(Base):
    __tablename__ = 'opresults'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # wavelength = Column(Float, nullable=False)
    path = Column(String(50), nullable=False)
    opresult_id  = Column(Integer, ForeignKey('resultcontext.id'))
    opcontext = relationship("ResultContext", back_populates="opresult")

    def __repr__(self):
        return "{}".format(self.path)
