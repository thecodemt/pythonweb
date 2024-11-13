pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // 从 Git 仓库检出指定的分支
                git branch: 'master', url: 'https://github.com/thecodemt/pythonweb.git'
            }
        }

        stage('Build and Test') {
            agent {
                docker {
                    image 'python:3.8'  // 使用 Python 3.8 的 Docker 镜像
                    args '-u root'  // 以 root 身份运行容器
                }
            }
            steps {
                // 安装依赖
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                
                // 运行测试
                sh 'pytest test.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                // 构建 Docker 镜像
                script {
                    sh 'docker build -t flask_app .'
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                // 使用凭据登录到 Docker Registry
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    // 登录到 Docker Registry
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                }

                // 推送 Docker 镜像到 Docker Registry
                sh 'docker push jackpot007/flask_app:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
