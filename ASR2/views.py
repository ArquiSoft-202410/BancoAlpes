from django.shortcuts import redirect, render
from googleapiclient import discovery
from google.oauth2 import service_account
import os
from django.conf import settings

credentials_path = os.path.join(settings.BASE_DIR,'ASR2', 'static', 'json', 'credentials.json')
credentials = service_account.Credentials.from_service_account_file(credentials_path)
service = discovery.build('compute', 'v1', credentials=credentials)

def deployment(request):
    instances = {}
    for instance in 'bcd':
        instanceName = f'banco-alpes-{instance}'
        instances[instance] = getInstanceStatus(instanceName)['status']

    if request.method == 'POST':
        instance = request.POST.get('instance')
        if instances[instance[-1]] == 'RUNNING':
            stopInstance(instance)
        else:
            startInstance(instance)
        return redirect('deployment')
    return render(request, 'ASR2/deployment.html', context={'instances': instances})

def startInstance(instanceName):
    request = service.instances().start(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response

def getInstanceStatus(instanceName):
    request = service.instances().get(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response

def stopInstance(instanceName):
    request = service.instances().stop(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = request.execute()
    return response