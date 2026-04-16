from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_PORT = 3306
DB_NAME = "fastapi"

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine->connect to the database
engine = create_engine(DB_URL)

# session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# base
Base = declarative_base()
