import requests

# GitHub repository and PR details
github_owner = "owner"
github_repo = "repository"
pr_number = "PR_NUMBER"
github_token = "GITHUB_TOKEN"  # Replace with your GitHub Personal Access Token
files_to_check = ["kk.txt", "test.txt"]  # Files to check for changes

# Jenkins job details
jenkins_url = "http://jenkins-server"
job_name = "jenkins-job"
next_stage = "Next_Stage_Name"
jenkins_token = "JENKINS_TOKEN"  # Replace with your Jenkins API token

# GitHub API URL to get PR details
github_pr_url = f"https://api.github.com/repos/{github_owner}/{github_repo}/pulls/{pr_number}/files"

# Jenkins API URL to trigger the next stage
jenkins_next_stage_url = f"{jenkins_url}/job/{job_name}/{next_stage}/build"
jenkins_auth = (jenkins_token, '')

# Function to trigger the next Jenkins stage
def trigger_next_stage():
    response = requests.post(jenkins_next_stage_url, auth=jenkins_auth)
    if response.status_code == 201:
        print("Next stage triggered successfully.")
    else:
        print(f"Failed to trigger the next stage. Status code: {response.status_code}")

# Get PR files from GitHub
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.get(github_pr_url, headers=headers)

if response.status_code == 200:
    pr_files = response.json()
    modified_files = [file['filename'] for file in pr_files]
    for file in files_to_check:
        if file in modified_files:
            print(f"File '{file}' has changed.")
            trigger_next_stage()
            break  # Exit loop once any specified file is found
    else:
        print("No specified files have changed. Skipping the next stage.")
else:
    print(f"Failed to retrieve PR files from GitHub. Status code: {response.status_code}")
