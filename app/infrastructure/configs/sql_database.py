from os import getenv
from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

database_url = getenv("DATABASE_URL", "")
db_engine = create_engine(database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)


def get_session():
    with Session(db_engine) as session:
        yield session
