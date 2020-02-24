#!groovy
def PROJECT_NAME = "waarnemingen-boten"
def SLACK_CHANNEL = '#waarnemingen-deployments'
def PLAYBOOK = 'deploy-waarnemingen-boten.yml'
def PLAYBOOK_INVENTORY = 'acceptance'
def SLACK_MESSAGE = [
    "title_link": BUILD_URL,
    "fields": [
        ["title": "Project","value": PROJECT_NAME],
        ["title":"Branch", "value": BRANCH_NAME, "short":true],
        ["title":"Build number", "value": BUILD_NUMBER, "short":true]
    ]
]



pipeline {
    agent any

    environment {
        SHORT_UUID = sh( script: "uuidgen | cut -d '-' -f1", returnStdout: true).trim()
        def IS_RELEASE = "${env.BRANCH_NAME ==~ "release/.*"}"
        COMPOSE_PROJECT_NAME = "${PROJECT_NAME}-${env.SHORT_UUID}"
        VERSION = env.BRANCH_NAME.replace('/', '-').toLowerCase().replace(
            'master', 'latest'
        )
    }

    stages {
        stage('Test') {
            steps {
                sh 'make test'
            }
        }

        stage('Build') {
            steps {
                sh 'make build'
            }
        }

        stage('Push and deploy') {
            when { 
                anyOf {
                    branch 'master'
                    buildingTag()
                    environment name: 'IS_RELEASE', value: 'true'
                }
            }
            stages {
                stage('Push') {
                    steps {
                        retry(3) {
                            sh 'make push'
                        }
                    }
                }

                stage('Deploy to acceptance') {
                    when { environment name: 'IS_RELEASE', value: 'true' }
                    steps {
                        sh 'echo Deploy acceptance'
                        build job: 'Subtask_Openstack_Playbook', parameters: [
                            string(name: 'PLAYBOOK', value: PLAYBOOK),
                            string(name: 'INVENTORY', value: PLAYBOOK_INVENTORY),
                            string(
                                name: 'PLAYBOOKPARAMS', 
                                value: "-e deployversion=${VERSION}"
                            )
                        ], wait: true
                    }
                }
            }
        }

    }
    post {
        always {
            sh 'make clean'
        }
        success {
            script {
                if ( env.IS_RELEASE == true )
                slackSend(channel: SLACK_CHANNEL, attachments: [SLACK_MESSAGE << 
                    [
                        "color": "#36a64f",
                        "title": "Build succeeded :rocket:",
                    ]
                ])
            }
        }
        failure {
            script {
                if ( env.IS_RELEASE == true )
                slackSend(channel: SLACK_CHANNEL, attachments: [SLACK_MESSAGE << 
                    [
                        "color": "#D53030",
                        "title": "Build failed :fire:",
                    ]
                ])
            }
        }
    }
}

