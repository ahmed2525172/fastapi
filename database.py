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
database_name = "testdb"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# -------------------------
# Define your table model
# -------------------------
class User(Base):
    __tablename__ = "users"
    Id = Column(Integer, primary_key=True, index=True)
    Firstname = Column(String(100))
    Lastname = Column(String(100))

# -------------------------
# Create tables in the DB
# -------------------------
Base.metadata.create_all(bind=engine)

# -------------------------
# Read Excel and insert data
# -------------------------
df = pd.read_excel(r'c:\Users\Ahmed\Downloads\sample_people.xlsx')

db = SessionLocal()

for _, row in df.iterrows():
    user = User(Id=row['Id'], Firstname=row['Firstname'], Lastname=row['Lastname'])
    db.add(user)

db.commit()

# -------------------------
# Query all users
# -------------------------
users = db.query(User).all()

for user in users:
    print(user.Id, user.Firstname, user.Lastname)

# Close session
db.close()
