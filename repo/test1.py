# Python program to alert when a commit takes place in github
# To monitor commits in a Github repository and receive an alert when a 
# commit takes place, you can use the Github API to query the repository for
# the latest commit and compare it with the previous commit.
# Here's an example Python program that uses the Github API and the requests library to monitor a Github repository:

import subprocess
import requests 
import time 
# Replace these with your own values
github_username = 'sivaa-h' 
github_repository = 'tech' 
github_access_token = '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'
# Initialize the last commit hash to None 
last_commit_hash = None 
# Continuously check for new commits 
while True: # Construct the Github API URL 
    api_url = f'https://api.github.com/repos/sivaa-h/tech/commits'
     # Make a request to the Github API 
    headers = {'Authorization': f"token {'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'}"} 
    response = requests.get(api_url, headers=headers)
     # Get the latest commit hash 
    latest_commit_hash = response.json()[0]['sha'] 
    # If this is the first time we're checking, set the last commit hash 
    if last_commit_hash is None: 
        last_commit_hash = latest_commit_hash 
    # If the latest commit hash is different from the last commit hash, print an alert 
    if latest_commit_hash != last_commit_hash: 
        print(f'A new commit ({latest_commit_hash}) has been made to {github_username}/{github_repository}!')
    # Set the last commit hash to the latest commit hash 
    last_commit_hash = latest_commit_hash 
    
    latest_commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    print("Latest commit hash:", latest_commit_hash)    
    command = ["git", "checkout", latest_commit_hash]
    output = subprocess.check_output(command,stderr=subprocess.STDOUT)
    # check if the output indicates success
    if "Already on" in output.decode("utf-8"):
        print("Already on latest commit")
    else:
        print("Checked out latest commit")
    # Wait for 60 seconds before checking again 
    time.sleep(60) 

# Make sure to replace the placeholders for github_username, github_repository, and github_access_token with your own values.
# You can generate a Github access token by following the instructions here.
# This program continuously checks for new commits every 60 seconds. 
# If a new commit is detected, it prints an alert to the console. 
# You can modify this program to send an email, a text message, or any other type of notification based on your specific needs.