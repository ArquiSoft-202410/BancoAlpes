from django.shortcuts import render

from ASR1.logic.ASR5 import generateSignature, verifySignature
from ASR1.models import DatosPersonales
from .forms import DatosPersonalesForm
from .logic.producer import sendRequest

def form(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            newData = form.save(commit=False)
            dataToSign = f"{newData.nombres}{newData.apellidos}{newData.pais}{newData.ciudad}57{newData.numero}{newData.email}"
            newData.firma = generateSignature(dataToSign)
            newData.save()
            sendRequest(form.cleaned_data)
            return render(request, "ASR1/check.html")
        else:
            print(form.errors)
    else:
        form = DatosPersonalesForm()
    return render(request, "ASR1/form.html", {'form': form})

def users(request):
    users = DatosPersonales.objects.all()
    for user in users:
        user.state = verifySignature(f"{user.nombres}{user.apellidos}{user.pais}{user.ciudad}57{user.numero}{user.email}", user.firma)
    return render(request, "ASR1/users.html", {'users': users})