pipeline {
    agent any

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
                echo 'Pipeline completado correctamente'
            }
        }
    }
}
