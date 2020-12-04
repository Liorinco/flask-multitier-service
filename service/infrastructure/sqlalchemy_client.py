from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SQLAlchemyClient:
    def __init__(self, database_uri: str) -> object:
        super().__init__()
        engine = create_engine(database_uri, echo=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()
