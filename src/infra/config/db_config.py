from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Constants: Definition database information
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "3006"
# DB_NAME = "postgres"
DB_NAME = "app_bank"


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.session = None

    def get_engine(self):
        """Return connection engine
        :param  -   None
        :return -   engine connection to database
        """

        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        self.session = Session(engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
