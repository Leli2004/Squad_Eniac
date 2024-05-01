from django.shortcuts import render
from app_voluntarios.forms import VoluntariosForms

# Create your views here.
def voluntarios(request):
    if request.method == 'POST':
        form = VoluntariosForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'voluntarios.html', {'form': form, 'sucesso': True})
    else:
        form = VoluntariosForms()
    return render(request, 'voluntarios.html', {'form': form}) 

    