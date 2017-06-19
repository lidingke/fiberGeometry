from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from setting.config import SQLALCHEMY_DIR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float,Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    account_id = Column(Integer, autoincrement=True)
    name = Column(String(50),  primary_key=True, autoincrement=True)
    password = Column(String(200), nullable=False)
    datetime = Column(DateTime, default=datetime.now())
    parameter_id = relationship("Result", backref = "account", cascade="all")

    @classmethod
    def is_exit(cls, user, password='123456'):
        cls.query


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    corediameter = Column(Float, nullable=False)
    claddiameter = Column(Float, nullable=False)
    coreroundness = Column(Float, nullable=False)
    cladroundness = Column(Float, nullable=False)
    concentricity = Column(Float, nullable=False)

    sharpness = Column(Float, nullable=False)
    fibertype = Column(String(50), nullable=False)
    fiberLength = Column(String(50), nullable=False)
    producer = Column(String(50), nullable=False)
    fiberNo = Column(String(50), nullable=False)
    # worker = Column(String(50), nullable=False)

    result_datetime = Column(Integer, ForeignKey('account.name'))

    KEYS = ('corediameter', 'claddiameter', 'coreroundness', 'cladroundness', 'concentricity',
            'sharpness', 'fibertype', 'fiberLength', 'producer', 'fiberNo')

engine = create_engine(SQLALCHEMY_DIR)
DBSession = sessionmaker(bind=engine)

def session_add_by_account(result):
    if
    session = DBSession()
    session.add(result)
    session.commit()
    session.close()