from database import Base, engine
from model import Book


Base.metadata.create_all(bind=engine)