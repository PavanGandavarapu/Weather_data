import os
import requests

# Define the URL of the GitHub API for the directory contents
api_url = "https://api.github.com/repos/corteva/code-challenge-template/contents/wx_data"

# Define the local directory to save the files
local_dir = "wx_data"

# Create the local directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

# Fetch the list of files in the directory
response = requests.get(api_url)
response.raise_for_status()  # Check if the request was successful
files = response.json()

# Download each file
for file in files:
    if file['type'] == 'file':  # Ensure it's a file and not a directory
        file_url = file['download_url']
        file_name = file['name']
        file_path = os.path.join(local_dir, file_name)

        print(f"Downloading {file_name}...")
        file_response = requests.get(file_url)
        file_response.raise_for_status()

        # Save the file locally
        with open(file_path, 'wb') as f:
            f.write(file_response.content)

        print(f"Saved {file_name} to {file_path}")

print("All files downloaded successfully.")
