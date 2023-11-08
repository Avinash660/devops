pipeline {
    agent any

    stage('Check for File Changes') {
    steps {
        sh 'python file-check.py'
    }
}

    stage('Check PR Approval') {
        script {
            def pr = currentBuild.rawBuild.getCause(
                com.cloudbees.jenkins.plugins.bitbucket.PullRequestCause
            )

            if (pr) {
                def approver = pr.getUser()
                def approvalStatus = pr.isApproved()

                if (approvalStatus) {
                    echo "PR approved by ${approver}"
                } else {
                    currentBuild.result = 'ABORTED'
                    error "PR not approved. Aborting the build."
                }
            }
        }
    }
    
    stages {
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
k
