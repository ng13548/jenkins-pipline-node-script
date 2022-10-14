pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'node --version'
        sh 'npm install mqtt'
      }
    }
    stage('hello') {
      steps {
        sh 'node mqtt-pub.js'
      }
    }
  }
}
