# app.py

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from threading import Lock  # Import Lock

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///bank.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Create a global lock
lock = Lock()

# Account Model
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=100.0)  # Initial balance

Base.metadata.create_all(engine)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    account_id = data.get('account_id')
    amount = data.get('amount')

    with lock:  # Acquire the lock before proceeding
        session = Session()
        account = session.query(Account).filter_by(id=account_id).first()

        # Simulate delay to create a race condition vulnerability
        time.sleep(2)

        if account and account.balance >= amount:
            account.balance -= amount
            session.commit()
            response = {'status': 'success', 'balance': account.balance}
        else:
            response = {'status': 'error', 'message': 'Insufficient balance or account not found'}
        
        session.close()
        return jsonify(response)

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    account_id = data.get('account_id')
    amount = data.get('amount')

    session = Session()
    account = session.query(Account).filter_by(id=account_id).first()

    if account:
        account.balance += amount
        session.commit()
        response = {'status': 'success', 'balance': account.balance}
    else:
        response = {'status': 'error', 'message': 'Account not found'}
    
    session.close()
    return jsonify(response)

@app.route('/check_balance', methods=['GET'])
def check_balance():
    account_id = request.args.get('account_id', type=int)
    session = Session()
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        response = {'status': 'success', 'balance': account.balance}
    else:
        response = {'status': 'error', 'message': 'Account not found'}
    session.close()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
