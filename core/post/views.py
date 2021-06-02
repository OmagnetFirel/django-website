from django.shortcuts import HttpResponseRedirect
from .models import Comentario
from .forms import FormComentario

# Create your views here.


def addComentario(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = FormComentario(request.POST)
        if form.is_valid():
            dados = Comentario()
            dados.name= form.cleaned_data['name']
            dados.email = form.cleaned_data['email']
            dados.comentario = form.cleaned_data['comentario']
            dados.post_id = id
            dados.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)