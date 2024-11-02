# init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Account, Base

# Set up the database connection
engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a test account with ID 1 and an initial balance of 100
if not session.query(Account).filter_by(id=1).first():
    test_account = Account(id=1, balance=100.0)
    session.add(test_account)
    session.commit()
    print("Database initialized with a test account.")
else:
    print("Test account already exists.")

# Close the session
session.close()
