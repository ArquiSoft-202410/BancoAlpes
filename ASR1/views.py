from django.shortcuts import redirect, render
from .forms import DatosPersonalesForm
from .logic.producer import sendRequest

def form(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            formData = {
                'nombres': form.cleaned_data['nombres'],
                'apellidos': form.cleaned_data['apellidos'],
                'pais': form.cleaned_data['pais'],
                'ciudad': form.cleaned_data['ciudad'],
                'numero': "57" + str(form.cleaned_data['numero']),
                'email': form.cleaned_data['email']
            }
            sendRequest(formData)
            return render(request, "ASR1/check.html")
        else:
            print(form.errors)
    else:
        form = DatosPersonalesForm()
    return render(request, "ASR1/form.html", {'form': form})