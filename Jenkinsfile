pipeline {
  agent { label 'windows' }
  stages {
    stage('Checkout'){ steps { checkout scm } }
    stage('Install'){
      steps {
        bat 'py -m pip install --upgrade pip'
        bat 'py -m pip install -r requirements.txt'
      }
    }
    stage('Tests'){
      steps {
        bat 'py -m pytest --maxfail=1 -q --junitxml=results.xml'
      }
    }
    stage('Publish'){
      steps { junit 'results.xml' }
    }
  }
}
