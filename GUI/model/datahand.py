import pickle
from sqlalchemy import Column, String, create_engine, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from GUI.model.relationmodel import Account, ResultContext, CVResult, OPResult

Base = declarative_base()


class ResultSheet(Base):
    __tablename__ = 'result_sheet'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    core_diameter = Column(Float())
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

relation_engine = create_engine("sqlite:///setting/test_relation_result.db")
RDBSession = sessionmaker(bind=relation_engine)

def update_cv_data(result):
    #todo:default user
    session = RDBSession()
    user = session.query(Account).filter_by(name='lidingke').one()

    context = ResultContext(
        sharpindex= result['sharpindex'],
        fiber_type=result["fibertype"],
        fiber_producer=result["producer"],
        fiber_number=result["fiberNo"],
        fiber_length=result["fiberLength"],
        instrument='abc',
        worker=user.id
    )
    session.add(context)
    session.commit()
    #('corediameter', 'claddiameter', 'coreroundness','cladroundness', 'concentricity')
    cvresult = CVResult(
        corediameter=result["corediameter"],
        claddiameter=result["claddiameter"],
        coreroundness=result["coreroundness"],
        cladroundness=result["cladroundness"],
        concentricity=result["concentricity"],
        cvresult_id=context.id
    )
    session.add(cvresult)
    session.commit()

def update_op_data(result):
    #todo:default user
    session = RDBSession()
    user = session.query(Account).filter_by(name='lidingke').one()

    context = ResultContext(
        sharpindex= result['sharpindex'],
        fiber_type=result["fibertype"],
        fiber_producer=result["producer"],
        fiber_number=result["fiberNo"],
        fiber_length=result["fiberLength"],
        instrument='abc',
        worker=user.id
    )
    session.add(context)
    session.commit()
    #('corediameter', 'claddiameter', 'coreroundness','cladroundness', 'concentricity')
    opresult = OPResult(
        waves=result["attwaves"],
        powers=result["attpowers"],
        opresult_id=context.id
    )

    session.add(opresult)
    session.commit()


import matplotlib.pyplot as plt

def read_show_from_db(pk=3):
    session = RDBSession()
    num = session.query(ResultContext).count()
    # last = session.query(ResultContext).filter_by(id = nums)
    result = session.query(OPResult).filter_by(opresult_id=num).one()
    waves = result.waves
    waves = pickle.loads(waves)
    powers = result.powers
    powers = pickle.loads(powers)
    fig = plt.figure(len(powers))
    ax1 = fig.add_subplot(111)
    ax1.plot(waves,powers)
    # ax2 = ax1.twinx()
    # ax2.plot(range(len(sharps)),origin,color='red')
    # ax2.title(dir_)
    plt.show()
    # pass