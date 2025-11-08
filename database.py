from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# -------------------------
# Database connection setup
# -------------------------
username = "root"
password = "ahmed2628"
hostname = "localhost"
port = 3305
database_name = "blogs"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# -------------------------
# Define your table model
# -------------------------

# -------------------------
# Create tables in the DB
# -------------------------
Base.metadata.create_all(bind=engine)

# -------------------------
# Read Excel and insert data
# -------------------------


db = SessionLocal()

db.commit()

# -------------------------
# Query all users
# -------------------------


# Close session
db.close()
