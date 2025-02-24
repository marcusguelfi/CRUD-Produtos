from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produto

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Obrigatório. Informe um email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade']