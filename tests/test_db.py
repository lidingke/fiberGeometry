#coding:utf-8

from setting import parameter
REAL_SQLALCHEMY_DIR = parameter.SQLALCHEMY_DIR
parameter.SQLALCHEMY_DIR = "sqlite:///tests/data/test.db"
from GUI.model.models import *
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float,Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime
TestBase = declarative_base()
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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


para = {}
para['fiberLength'] = '1'
para['worker'] = '3780'
para['producer'] = '1'
para['fiberNo'] = '1'
para['fibertype'] = '1'
para['fibertypeindex'] = '1'
para['date'] = datetime.now()
para['title'] = u'光纤端面几何测试报告'
para['corediameter'] = 1
para['claddiameter'] = 1
para['coreroundness'] = 1
para['cladroundness'] = 1
para['concentricity'] = 1
para['sharpindex'] = 1


class Test_db():

    engine = create_engine(SQLALCHEMY_DIR)
    Session = sessionmaker(bind=engine)
    session = Session()
    def test_create_test(self):
        Base.metadata.create_all(self.engine)


    def test_session(self):

        b = Children(name='liuqi2')
        self.session.add(b)
        self.session.commit()
        self.session.delete(b)
        self.session.commit()

    def test_Account(self):
        exit_ = self.session.query(Account).filter(Account.name=='3780').count()
        if not exit_:
            _ = Account(name='3780',password='123456')
            self.session.add(_)
            self.session.commit()

    def test_dict_in(self):
        session_add_by_account(para)

def ttest_create_real():
    logger.info("REAL_SQLALCHEMY_DIR "+REAL_SQLALCHEMY_DIR)
    engine = create_engine(REAL_SQLALCHEMY_DIR)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    exit_ = session.query(Account).filter(Account.name == '3780').count()
    if not exit_:
        _ = Account(name='3780', password='123456')
        session.add(_)
        session.commit()

class tTest_session():

    def test_dict_in(self):

        session_add_by_account(para)


