from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(
    url=settings.database_url,
    connect_args={"check_same_thread": False},
    echo=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()


# создание бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


def get_init_db():
    global Base, engine
    Base.metadata.create_all(bind=engine)