# implenent an exponential backoff strategy that doubles the wait
# time between retries , strating from 1 sec , but stops after 5 sec

import time 

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1}: Waiting for {wait_time} seconds before retrying...")
    time.sleep(wait_time)
    wait_time *= 2  # double the wait time for the next attempt
    attempts += 1