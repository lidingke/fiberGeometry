from sqlalchemy import Column, String, create_engine, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ResultSheet(Base):

    __tablename__ = 'result_sheet'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    core_diameter = Column(Float() )
    clad_diameter = Column(Float())
    core_roundness = Column(Float())
    clad_roundness = Column(Float())
    concentricity = Column(Float())


engine = create_engine("sqlite:///setting/cv_result.db")
# conn = engine.connect()
DBSession = sessionmaker(bind=engine)

def session_add(result):
    session = DBSession()
    session.add(result)
    session.commit()
    session.close()