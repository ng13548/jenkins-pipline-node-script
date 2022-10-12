pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
        sh 'python install paho-mqtt'
      }
    }
    stage('hello') {
      steps {
        sh 'python publish.py'
      }
    }
  }
}
