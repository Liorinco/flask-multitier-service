from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from service import config

engine = create_engine(config.DATABASE_URI, echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
