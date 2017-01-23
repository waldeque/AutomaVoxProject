from django import forms
from .models import Conta
from .models import Condominio
from .models import Inquilino
from .models import GrupoConta
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # nome = forms.CharField(required=True)
    # sobrenome = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


    #Pegar os dados so usuário e passar para as variáveis
    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class CadastroConta(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ('grupoContas',
            'codigo_conta',
            'condominio',
            'cpf_inquilino',
            'nome_inquilino',
            'valor',
            'vencimento')


class CadastroGrupoConta(forms.ModelForm):
    class Meta:
        model = GrupoConta
        fields = ("codigo_grupo",
                  "nome_grupo")


class CadastroCondominio(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = ("codigo_condominio",
            "nome_condominio",
            "logradouro",
            "numero",
            "bairro",
            "cep",
            "complemento",
            "cidade",
            "estado")

class CadastroInquilino(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = ("cpf_inquilino",
            "rg_inquilino",
            "uf",
            "nome_inquilino",
            "sobrenome_inquilino",
            "sexo_inquilino",
            "nascimento")