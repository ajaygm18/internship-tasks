from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

db_url = "postgresql://postgres:1818@localhost:5432/ajay"
engine = create_engine(db_url)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

class Candidate(Base):

    __tablename__ = 'candidate'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    education = Column(String)
    previousCTC = Column(Float, nullable=True)
    experience = Column(Integer, nullable=True)


class Admin(Base):

    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
