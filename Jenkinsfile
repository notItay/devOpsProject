pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/notItay/devOpsProject.git'
            }
        }
        stage('rest_app.py') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python rest_app.py'
                    } else {
                        sh 'nohup python rest_app.py &'
                    }
                }
            }
        }
        stage('web_app.py') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python web_app.py'
                    } else {
                        sh 'nohup python web_app.py &'
                    }
                }
            }
        }
        stage('backend_testing.py') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python backend_testing.py'
                    } else {
                        sh 'python backend_testing.py'
                    }
                }
            }
        }
        stage('frontend_testing.py') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python frontend_testing.py'
                    } else {
                        sh 'python frontend_testing.py'
                    }
                }
            }
        }
        stage('clean_environment.py') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python clean_environment.py'
                    } else {
                        sh 'python clean_environment.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}