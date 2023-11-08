pipeline {
    agent any

    stages {
        stage('Check for File Changes') {
            steps {
                sh 'python file-check.py'
            }
            }

        stage('Check PR Approval') {
            steps {
                script {
                    def prNumber = 1  // Replace with the PR number you want to check
                    def githubToken = 'YOUR_GITHUB_TOKEN'  // Replace with your GitHub Personal Access Token (PAT)

                    // Make a request to the GitHub API to get PR details
                    def apiUrl = "https://api.github.com/repos/owner/repo/pulls/$prNumber"
                    def response = httpRequest(
                        httpMode: 'GET',
                        url: apiUrl,
                        authentication: 'YOUR_CREDENTIALS_ID',  // Create a Jenkins credential with your GitHub PAT
                        responseHandle: 'json'
                    )

                    def pr = response.data

                    if (pr.review_requested == 0) {
                        echo "PR is not approved"
                        currentBuild.result = 'ABORTED'
                        error('PR is not approved, halting the build')
                    } else {
                        echo "PR is approved, proceeding to the next stage"
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test app') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        }
    }

