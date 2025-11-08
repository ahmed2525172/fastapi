from sqlalchemy import Column, Integer, String
from database import Base  # your database.py file

class Blog(Base):
    __tablename__ = "items"  # must match your existing table name
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))           # adjust length to match your table
    body = Column(String(255))    # adjust length to match your table
