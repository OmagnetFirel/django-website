from django.shortcuts import render, HttpResponse
from post.models import Publicacao,Categoria,Comentario
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    ###PEGAR AS POSTAGENS/CATEGORIAS/ENFIM OQUE EU QUISER###
    post_random = Publicacao.objects.order_by('?')[:4]
    post_latest = Publicacao.objects.order_by('updated_at')[:4]
    categoria = Categoria.objects.all()
    
    
    context = {
        'post_random': post_random,
        'post_latest':post_latest,
        'categoria': categoria,
    }
    return render(request, 'index.html', context)



def blog(request):
    
    ###PEGAR AS POSTAGENS/CATEGORIAS/ENFIM O QUE EU QUISER###
    all_posts = Publicacao.objects.order_by('updated_at')
    categoria = Categoria.objects.all()
    ###PAGINAÇÃO###
    paginator = Paginator(all_posts,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ###CONTEXT###
    context = {
        'categoria':categoria,
        'page_obj':page_obj,
        }
     
    return render(request, 'paginas/todos_posts/blog.html', context)



def materia(request,id,slug):
    materia = Publicacao.objects.get(pk=id)
    comentario = Comentario.objects.filter(post_id=id, status='Lido')
    context = {
        'materia':materia,
        'comentario':comentario,
        }
     
    return render(request,"paginas/materia/materia.html", context)



def about(request):
    return HttpResponse('teste')