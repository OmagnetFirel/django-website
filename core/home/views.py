from django.shortcuts import render, HttpResponse
from post.models import Publicacao
# Create your views here.

def index(request):
    post_random = Publicacao.objects.order_by('?')[:4]
    post_latest = Publicacao.objects.order_by('updated_at')
    context = {
        'post_random': post_random,
        'post_latest':post_latest,
    }
    return render(request, 'index.html', context) 