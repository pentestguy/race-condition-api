import requests
import threading
import time
import random

def withdraw():
    url = "http://172.17.0.2:5000/withdraw"
    payload = {"account_id": 1, "amount": 10}
    
    # Introduce a random delay to increase the chance of a race condition
    time.sleep(random.uniform(0.01, 0.1))
    
    response = requests.post(url, json=payload)
    
    # Print the response from the server
    print(response.json())

def main():
    threads = []
    for _ in range(10):  # Simulate 10 concurrent requests
        thread = threading.Thread(target=withdraw)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
