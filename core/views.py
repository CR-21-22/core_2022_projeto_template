from django.shortcuts import redirect, render
from .models import Topico, Conteudo
from .forms import TopicoForm, ConteudoForm

# Create your views here.
def index_view(request):
    return render(request, 'core/index.html')


def topicos_view(request):

    topicos = Topico.objects.all().order_by('ordem')

    context = {
        'topicos':topicos
    }

    return render(request, 'core/topicos.html', context)


def edita_topicos_view(request):

    topicos = Topico.objects.all().order_by('ordem')

    context = {
        'topicos':topicos
    }

    return render(request, 'core/edita_topicos.html', context)


def novo_topico_view(request):

    topico_form = TopicoForm(request.POST or None)
    if topico_form.is_valid():
        topico_form.save()
        return redirect('core:edita_topicos')

    context = {'topico_form':topico_form}
    return render(request, 'core/novo_topico.html', context)


def edita_topico_view(request, topico_id):

    topico = Topico.objects.get(id=topico_id)
    topico_form = TopicoForm(request.POST or None, instance=topico)
    if request.method == "POST" and topico_form.is_valid():
        topico_form.save()
        return redirect('core:edita_topicos')

    context = {'topico_form':topico_form, 'topico_id':topico_id}
    return render(request, 'core/edita_topico.html', context)


def apaga_topico_view(request, topico_id):
    topico = Topico.objects.get(id=topico_id)
    topico.delete()
    return redirect('core:edita_topicos')


def novo_conteudo_view(request):

    conteudo_form = ConteudoForm(request.POST or None)
    if conteudo_form.is_valid():
        conteudo_form.save()
        return redirect('core:edita_topicos')

    context = {'conteudo_form':conteudo_form}
    return render(request, 'core/novo_conteudo.html', context)


def edita_conteudo_view(request, conteudo_id):

    conteudo = Conteudo.objects.get(id=conteudo_id)
    conteudo_form = ConteudoForm(request.POST or None, instance=conteudo)
    if request.method == "POST" and conteudo_form.is_valid():
        conteudo_form.save()
        return redirect('core:edita_topicos')

    context = {'conteudo_form':conteudo_form, 'conteudo_id':conteudo_id}
    return render(request, 'core/edita_conteudo.html', context)


def apaga_conteudo_view(request, conteudo_id):
    conteudo = Conteudo.objects.get(id=conteudo_id)
    conteudo.delete()
    return redirect('core:edita_topicos')
