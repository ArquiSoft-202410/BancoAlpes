from django.shortcuts import render
from googleapiclient import discovery
from google.oauth2 import service_account

def deployment(request):
    if request.method == 'POST':
        instance = request.POST.get('instance')
        startInstance(instance)
    return render(request, 'ASR2/deployment.html')

def startInstance(instanceName):
    credentials = service_account.Credentials.from_service_account_file('/apps/ASR2/static/json/credentials.json')
    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().start(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response
