import threading
import time
from django.shortcuts import redirect, render
from googleapiclient import discovery
from google.oauth2 import service_account
import os
from django.conf import settings
from ASR2.logic.producer import sendRequest
from deployment import turnOffApp

credentials_path = os.path.join(settings.BASE_DIR, 'ASR2', 'static', 'json', 'credentials.json')
credentials = service_account.Credentials.from_service_account_file(credentials_path)
service = discovery.build('compute', 'v1', credentials=credentials)

def delayedAction():
    time.sleep(120)
    sendRequest({'Action': 'Restart Load Balancer'})

def deployment(request):
    instances = {}
    for instance in 'abcd':
        instanceName = f'banco-alpes-{instance}'
        instances[instance] = getInstanceStatus(instanceName)['status']

    if request.method == 'POST':
        instance = request.POST.get('instance')
        if instance == 'turn-off':
            turnOffApp()
        elif instances[instance[-1]] == 'RUNNING':
            stopInstance(instance)
            threading.Thread(target=delayedAction).start()
        else:
            startInstance(instance)
            threading.Thread(target=delayedAction).start()
        return redirect('deployment')
    return render(request, 'ASR2/deployment.html', context={'instances': instances})

def startInstance(instanceName):
    req = service.instances().start(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = req.execute()
    return response

def getInstanceStatus(instanceName):
    req = service.instances().get(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = req.execute()
    return response

def stopInstance(instanceName):
    req = service.instances().stop(project='arquisoft-202410', zone='us-central1-a', instance=instanceName)
    response = req.execute()
    return response
