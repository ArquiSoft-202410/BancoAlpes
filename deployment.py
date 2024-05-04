from googleapiclient import discovery
from google.oauth2 import service_account
from credentials import runCredentials

runCredentials()

credentials = service_account.Credentials.from_service_account_file('ASR2/static/json/credentials.json')
service = discovery.build('compute', 'v1', credentials=credentials)

def startInstance(instanceName):
    request = service.instances().start(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response

def stopInstance(instanceName):
    request = service.instances().stop(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response

def turnOffApp():
    instances = ['rabbit-instance', 'db-instance', 'banco-alpes-d', 'banco-alpes-c', 'banco-alpes-b', 'banco-alpes-a', 'kong-instance']
    for instance in instances:
        stopInstance(instance)
        print(f'Stopping {instance}')

instances = ['db-instance', 'banco-alpes-a', 'rabbit-instance', 'kong-instance']

def runDeployment():
    for instance in instances:
        startInstance(instance)
        print(f'Starting {instance}')

runDeployment()