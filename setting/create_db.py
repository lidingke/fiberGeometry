#coding:utf-8
from migrate.versioning import api
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from setting.config import SQLALCHEMY_DIR
import sqlalchemy
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

from GUI.model.models import Base

engine = create_engine(SQLALCHEMY_DIR)
Base.metadata.create_all(engine)
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#     api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)