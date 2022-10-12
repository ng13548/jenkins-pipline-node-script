pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
        sh 'pip3 install paho-mqtt'
      }
    }
    stage('hello') {
      steps {
        sh 'python publish.py'
      }
    }
  }
}
