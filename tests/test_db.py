from sqlalchemy import create_engine

from GUI.model.models import Base
from setting import create_db
from sqlalchemy.orm import sessionmaker

from setting.config import SQLALCHEMY_DIR

engine = create_engine(SQLALCHEMY_DIR)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=create_db.engine)