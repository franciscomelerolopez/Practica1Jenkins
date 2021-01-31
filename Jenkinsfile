pipeline {
    agent any

    stages {
        stage('Construir') {
            steps {
                echo "          -------------CONSTRUYENDO MI SOFTWARE/CODE"
                echo "          Creando entorno virtual"
                sh 'virtualenv entorno_virtual'
                echo "          Activando el entorno_virtual"
                sh '. entorno_virtual/bin/activate'
                //sh 'pip3 --version'
                //echo "          Instalando los requerimientos concretos de este proyecto"
                //sh 'pip3 install -r requirements.txt'
                echo "          Instalando aplicación para testear"
                sh 'pip3 install pytest'
                echo "           Instalado aplicación/libreria necesaria para este proyecto concreto"
                sh 'pip3 install flask'
                echo "           Terminando de instalar requerimientos"
            }
        }
        stage('Test') {
            steps {
                echo "Ejecutando y probando"
                sh 'python3 src/main.py &'
                //sh 'pytest src/test_main.py'
                //echo "            Puedes probarla durante 20 segundos esta aplicación en modo local"   
            }
        }
        stage('Build Docker') {
            steps {
                echo "			  Construyendo la imagen de "
                sh 'docker build -t $Imagen .'
                //echo "			Tageando la imagen para poderla subir posteriormente"
                //docker tag $Imagen franciscomelero/$Imagen
                echo "			Subiendo la imagen repositorio de docker hub"
                sh' docker push $Imagen:latest'
                echo "			Borrando la imagen en modo local, aunque la dejamos para que no tarde tanto"
                sh 'docker rmi $Imagen:latest'
            }
        }
        stage('Desplegando') {
            steps {
                echo "			  Construyendo la imagen de "
                sh 'scp -i /home/jenkins/keyHLC docker-compose.yml root@51.178.25.195:/root/HLC/docker'
                sh 'ssh -i /home/jenkins/keyHLC "docker-compose -f /root/HLC/docker/docker-ompose.yml down'
                sh 'ssh -i /home/jenkins/keyHLC "docker-compose -f /root/HLC/docker/docker-ompose.yml up -d'
                //echo "			Tageando la imagen para poderla subir posteriormente"
                //docker tag $Imagen franciscomelero/$Imagen
                //echo "			Subiendo la imagen repositorio de docker hub"
                //sh' docker push $Imagen:latest'
                //echo "			Borrando la imagen en modo local, aunque la dejamos para que no tarde tanto"
                //sh 'docker rmi $Imagen:latest'
            }
        }
    }   
}
