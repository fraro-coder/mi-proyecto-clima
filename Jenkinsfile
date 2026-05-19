pipeline {
    agent any

    environment {
        API_KEY_PROYECTO = "f906fe751bf244a57edaea1f1c99fd66"
    }

    stages {
        stage('Clonar') {
            steps {
                echo 'Repositorio cargado'
            }
        }

        stage('Construir Docker') {
            steps {
                sh 'chmod +x build.sh'
                sh './build.sh'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline OK'
            }
        }
    }
}
