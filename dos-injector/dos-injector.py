import subprocess
import time
import json
import os

# URL to send the requests to
url1 = "https://accounts.harness.io/gateway/pipeline/api/webhook/custom/y0EjvXxVSs-gHhqde_9qrg/v3?accountIdentifier=MjBmNzA5YzAtZmViNC00Mj&orgIdentifier=default&projectIdentifier=Mock_Incident&pipelineIdentifier=test_pipeline&triggerIdentifier=customtrigger2"

url2 = "https://accounts.harness.io/gateway/pipeline/api/webhook/custom/MF7wJkhXQvOrguzz-sNzQg/v3?accountIdentifier=MjBmNzA5YzAtZmViNC00Mj&orgIdentifier=default&projectIdentifier=Mock_Incident&pipelineIdentifier=test_pipeline&triggerIdentifier=custom"
url3 = "https://accounts.harness.io/gateway/pipeline/api/webhook/custom/A4vTAktfTH-rvvMNsLRuDA/v3?accountIdentifier=MjBmNzA5YzAtZmViNC00Mj&orgIdentifier=default&projectIdentifier=Mock_Incident&pipelineIdentifier=test_pipeline&triggerIdentifier=trigger3"
url4 = "https://accounts.harness.io/gateway/pipeline/api/webhook/custom/MEgeQfKRQCe25R_VrqU_6g/v3?accountIdentifier=MjBmNzA5YzAtZmViNC00Mj&orgIdentifier=default&projectIdentifier=Mock_Incident&pipelineIdentifier=test_pipeline&triggerIdentifier=trigger4"
url5 = "https://accounts.harness.io/gateway/pipeline/api/webhook/custom/NQyBUgRSTpqXU2D01xsczw/v3?accountIdentifier=MjBmNzA5YzAtZmViNC00Mj&orgIdentifier=default&projectIdentifier=Mock_Incident&pipelineIdentifier=test_pipeline&triggerIdentifier=trigger5"
# Data to be sent in the POST request
data = {
    "key1": "value1",
    "key2": "value2"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Number of requests to send
num_requests = int(os.environ.get("NUM_REQUESTS", 5))

# Interval between requests (in seconds)
interval = int(os.environ.get("INTERVAL", 1))

# Loop to send the requests
for i in range(1, num_requests + 1):
    print(f"Sending request #{i} to {url1}")
    # Using curl to send a POST request with the Content-Type application/json
    subprocess.run([
        "curl", "-X", "POST", url1,
        "-H", "Content-Type: application/json",
        "-d", json_data
    ])
    print(f"Request #{i} completed")

    print(f"Sending request #{i} to {url2}")
    # Using curl to send a POST request with the Content-Type application/json
    subprocess.run([
        "curl", "-X", "POST", url2,
        "-H", "Content-Type: application/json",
        "-d", json_data
    ])
    print(f"Request #{i} completed")

    print(f"Sending request #{i} to {url3}")
    # Using curl to send a POST request with the Content-Type application/json
    subprocess.run([
        "curl", "-X", "POST", url3,
        "-H", "Content-Type: application/json",
        "-d", json_data
    ])
    print(f"Request #{i} completed")

    print(f"Sending request #{i} to {url4}")
    # Using curl to send a POST request with the Content-Type application/json
    subprocess.run([
        "curl", "-X", "POST", url4,
        "-H", "Content-Type: application/json",
        "-d", json_data
    ])
    print(f"Request #{i} completed")

    print(f"Sending request #{i} to {url5}")
    # Using curl to send a POST request with the Content-Type application/json
    subprocess.run([
        "curl", "-X", "POST", url5,
        "-H", "Content-Type: application/json",
        "-d", json_data
    ])
    print(f"Request #{i} completed")


    # Wait for the specified interval before the next request
    if i < num_requests:
        print(f"Waiting for {interval} seconds...")
        time.sleep(interval)

print("Completed all requests.")

