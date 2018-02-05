import pickle

import xlwt
from sqlalchemy import Column, String, create_engine, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from setting.config import SQLALCHEMY_DIR
from GUI.model.relationmodel import Account, ResultContext, CVResult, OPResult
from util.pltplot import figure_plot

Base = declarative_base()
relation_engine = create_engine(SQLALCHEMY_DIR)
RDBSession = sessionmaker(bind=relation_engine)


class ResultSheet(Base):
    __tablename__ = 'result_sheet'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    core_diameter = Column(Float())
    clad_diameter = Column(Float())
    core_roundness = Column(Float())
    clad_roundness = Column(Float())
    concentricity = Column(Float())


def update_cv_data(result):
    # todo:default user
    session = RDBSession()
    user = session.query(Account).filter_by(name='lidingke').one()

    context = ResultContext(
        sharpindex=result['sharpindex'],
        fiber_type=result["fibertype"],
        fiber_producer=result["producer"],
        fiber_number=result["fiberNo"],
        fiber_length=result["fiberLength"],
        instrument='abc',
        worker=user.id
    )
    session.add(context)
    session.commit()
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
    # todo:default user
    session = RDBSession()
    user = session.query(Account).filter_by(name='lidingke').one()

    context = ResultContext(
        sharpindex=result['sharpindex'],
        fiber_type=result["fibertype"],
        fiber_producer=result["producer"],
        fiber_number=result["fiberNo"],
        fiber_length=result["fiberLength"],
        instrument='abc',
        worker=user.id
    )
    session.add(context)
    session.commit()
    opresult = OPResult(
        waves=result["attwaves"],
        powers=result["attpowers"],
        opresult_id=context.id
    )

    session.add(opresult)
    session.commit()


def read_from_db(pk=None):
    session = RDBSession()
    if None == pk:
        pk = session.query(ResultContext).count()
    result = session.query(OPResult).filter_by(opresult_id=pk).one()
    waves = result.waves
    waves = pickle.loads(waves)
    powers = result.powers
    powers = pickle.loads(powers)
    return waves, powers


def read_show_from_db(pk=None):
    waves, powers = read_from_db(pk)
    figure_plot(waves, powers)


def read_xlsx_from_db(pk=None):
    waves, powers = read_from_db(pk)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    for i, w in enumerate(waves):
        sheet1.write(i, 0, w)
    for i, p in enumerate(powers):
        sheet1.write(i, 1, p)
    f.save("setting\\lastdata.xls")
