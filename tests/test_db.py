from sqlalchemy import create_engine

from GUI.model.models import *
from setting import create_db
from sqlalchemy.orm import sessionmaker

from setting.config import SQLALCHEMY_DIR
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float,Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime
TestBase = declarative_base()

class Father(TestBase):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    datetime = Column(DateTime, default=datetime.now())
    children = relationship("Children", backref = "father", cascade="all")


class Children(TestBase):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    father_id = Column(String(50), ForeignKey('father.name'))
    datetime = Column(DateTime, default=datetime.now())


class Test_db():

    engine = create_engine("sqlite:///tests/data/test.db")
    def test_create(self):
        TestBase.metadata.create_all(self.engine)

    def test_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        # a = Father(name='lidingke', password='123')
        # session.add(a)
        # session.commit()
        b = Children(name='liuqi2')
        session.add(b)
        session.commit()


