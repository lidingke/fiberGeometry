import pdb

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting.parameter import SQLALCHEMY_DIR
from GUI.model.relationmodel import Base,Account,ResultContext,CVResult,OPResult
import logging

logger = logging.getLogger(__name__)


def test_create_relation_model():
    SQLALCHEMY_DIR = "sqlite:///setting/test_relation_result.db"
    engine = create_engine(SQLALCHEMY_DIR)
    Base.metadata.create_all(engine)

    logger.warning("creat db by " + SQLALCHEMY_DIR)
    # DBSession.create
    # pdb.set_trace()


def test_insert_cvresult():
    SQLALCHEMY_DIR = "sqlite:///setting/test_relation_result.db"
    engine = create_engine(SQLALCHEMY_DIR)
    Session = sessionmaker(bind=engine)
    session = Session()
    # pdb.set_trace()
    user = session.query(Account).filter_by(name='lidingke').one()
    print "user:",user

    context = ResultContext(
        sharpindex= 123,
        fiber_type='G652',
        fiber_producer='YOFC',
        fiber_number='ABC',
        fiber_length=2,
        instrument='abc',
        worker=user.id
    )
    session.add(context)
    session.commit()

    cvresult = CVResult(
        corediameter=9,
        claddiameter=125,
        coreroundness=0.1,
        cladroundness=0.1,
        concentricity=0.1,
        cvresult_id=context.id
    )
    session.add(cvresult)
    session.commit()

    opresult = OPResult(
        path='/',
        opresult_id=context.id
    )

    session.add(opresult)
    session.commit()

