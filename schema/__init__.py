# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql+psycopg2://alembic@localhost/alembic"
)
meta = MetaData(engine)
Base = declarative_base(metadata=meta)
