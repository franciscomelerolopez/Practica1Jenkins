pipeline {
    agent any

    stages {
        stage('Construir') {
            steps {
                #!/bin/bash
                echo "          -------------CONSTRUYENDO MI SOFTWARE/CODE"
                echo "          Creando entorno virtual"
                virtualenv --python=python3 entorno_virtual
                echo "          Activando el entorno_virtual"
                source entorno_virtual/bin/activate
                echo "          Instalando los requerimientos concretos de este proyecto"
                pip install -r requirements.txt
                echo "          Instalando aplicación para testear"
                pip install pytest
                echo "           Instalado aplicación/libreria necesaria para este proyecto concreto"
                pip install flask
                echo "           Terminando de instalar requerimientos"

                echo "          Ejecutando la aplicación para testear en modo local sin docker"
            }
        }
        stage('Lanzar_Testeo') {
            steps {
                python $WORKSPACE/src/main.py &
                cd src && pytest && cd ..
                echo "            Puedes probarla durante 20 segundos esta aplicación en modo local"   
            }
        }
        stage('ConstruyentoTest') {
            steps {
                echo "			  Construyendo la imagen de "
                docker build -t $Imagen .
                #echo "			Tageando la imagen para poderla subir posteriormente"
                #docker tag $Imagen franciscomelero/$Imagen
                echo "			Subiendo la imagen repositorio de docker hub"
                docker push $Imagen:latest
                echo "			Borrando la imagen en modo local, aunque la dejamos para que no tarde tanto"
                docker rmi $Imagen:latest
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
