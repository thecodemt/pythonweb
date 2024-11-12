pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // 从 Git 仓库检出指定的分支
                git branch: 'master', url: 'https://github.com/thecodemt/pythonweb.git'
            }
        }

        stage('Build') {
            steps {
                // 设置 Python 环境并安装依赖
                script {
                    sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                // 运行测试
                script {
                    sh 'pytest test_sample.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                // 构建 Docker 镜像
                script {
                    sh 'docker build -t my_flask_app .'
                }
            }
        }

        stage('Deploy') {
            steps {
                // 部署到服务器
                script {
                    sh '''
                    echo "Deploying to server..."
                    '''
                }
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
