pipeline {
  agent { label 'windows' }
  options { timestamps(); ansiColor('xterm'); }
  stages {
    stage('Install') {
      options { timeout(time: 5, unit: 'MINUTES') }
      steps {
        bat '''
          call C:\\Users\\AhmedAbdEl-Megeed\\python-selenium-venv\\Scripts\\activate
          pip install --upgrade pip
          pip install -r requirements.txt --no-input --disable-pip-version-check
        '''
        //bat 'py -m pip install --upgrade pip'
        //bat 'py -m pip install -r requirements.txt --no-input --disable-pip-version-check'
      }
    }
    stage('Tests') {
      options { timeout(time: 10, unit: 'MINUTES') }
      steps {
        bat '''
            call C:\\Users\\AhmedAbdEl-Megeed\\python-selenium-venv\\Scripts\\activate
            python -m pytest -q --junitxml=reports/junit/pytest.xml --maxfail=1 -k "not slow"
        '''
      }
      post { always { junit allowEmptyResults: true, testResults: 'reports/junit/*.xml' } }
    }
  }
}
