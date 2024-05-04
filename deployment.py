from googleapiclient import discovery
from google.oauth2 import service_account
import os
from django.conf import settings
from .credentials import run as runCredentials

runCredentials()

credentials_path = os.path.join(settings.BASE_DIR,'ASR2', 'static', 'json', 'credentials.json')
credentials = service_account.Credentials.from_service_account_file(credentials_path)
service = discovery.build('compute', 'v1', credentials=credentials)

def startInstance(instanceName):
    request = service.instances().start(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response

instances = ['db-instance', 'banco-alpes-a', 'rabbit-instance', 'kong-instance']

for instance in instances:
    startInstance(instance)
    print(f'Starting {instance}')