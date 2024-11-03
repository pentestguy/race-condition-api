# Race Condition API Demo

This project demonstrates race conditions in an API. It includes endpoints for depositing, withdrawing, and checking account balances.

## Setup

### Requirements

- Python 3.8+
- Docker

### Running Locally

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Initialize the database:
    ```bash
    python init_db.py
    ```

3. Run the application:
    ```bash
    python app.py
    ```

The API will be accessible at `http://localhost:5000`.

### Running with Docker

1. Build the Docker image:
    ```bash
    docker build -t race-condition-api .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 race-condition-api
    ```

The API will be accessible at `http://localhost:5000` within the container.

### Testing the API

Use tools like `curl` or Postman to test the API endpoints:

- **Check Balance**:
    ```bash
    curl "http://localhost:5000/check_balance?account_id=1"
    ```

- **Deposit**:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"account_id": 1, "amount": 50}' http://localhost:5000/deposit
    ```

- **Withdraw**:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"account_id": 1, "amount": 50}' http://localhost:5000/withdraw
    ```

### Testing Race Conditions

To test for race conditions, use a script or tool to send multiple concurrent `POST` requests to the `/withdraw` endpoint.

