pipeline {
  agent any
  stages {
    stage('node version check') {
      steps {
        sh 'node --version'
        sh 'npm install mqtt'
      }
    }
    stage('Subscribe to MQTT Event') {
      steps {
        sh 'node mqtt-sub.js'
      }
    }
  }
}
