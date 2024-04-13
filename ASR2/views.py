from django.shortcuts import render
from googleapiclient import discovery
from google.oauth2 import service_account
import os
from django.conf import settings

def deployment(request):
    if request.method == 'POST':
        instance = request.POST.get('instance')
        startInstance(instance)
    return render(request, 'ASR2/deployment.html')

def startInstance(instanceName):
    credentials_path = os.path.join(settings.BASE_DIR, 'static', 'json', 'bancoalpes-419917-aba7af2b5ab1.json')
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().start(project='bancoalpes-419917', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response
