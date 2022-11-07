from django.forms import ModelForm
from .models import Topico, Conteudo


class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'


class ConteudoForm(ModelForm):
    class Meta:
        model = Conteudo
        fields = '__all__'