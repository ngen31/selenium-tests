pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        sh 'pytest --maxfail=1 --disable-warnings -q --junitxml=results.xml'
      }
    }
    stage('Publish Results') {
      steps {
        junit 'results.xml'
      }
    }
  }
}
