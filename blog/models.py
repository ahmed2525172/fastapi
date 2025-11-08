from sqlalchemy import Column, Integer, String
from database import Base  # your database.py file

class Item(Base):
    __tablename__ = "users"  # must match your existing table name

    Id = Column(Integer, primary_key=True, index=True)
    Firstname = Column(String(100))           # adjust length to match your table
    Lastname = Column(String(100))    # adjust length to match your table
