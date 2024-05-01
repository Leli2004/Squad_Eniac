from django import forms
from app_adotantes.models import Form_User
from app_animais.models import Animal


class PedidoAdocaoForm(forms.ModelForm):

    animal = forms.ModelChoiceField(queryset=Animal.objects.all(), widget=forms.HiddenInput())
    
    class Meta:
        model = Form_User
        fields = ["animal","nome", "email", "telefone", "quantidade_de_animais", "informações"]

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        telefone = cleaned_data.get('telefone')
        quant_animais = cleaned_data.get('quantidade_de_animais')
        info_geral = cleaned_data.get('informações')

        if not nome:
            self.add_error('nome', 'Este campo é obrigatório.')
        if not email:
            self.add_error('email', 'Este campo é obrigatório.')
        if not telefone:
            self.add_error('telefone', 'Este campo é obrigatório.')
        if not quant_animais:
            self.add_error('quant_animais', 'Este campo é obrigatório.')
        if not info_geral:
            self.add_error('informações', 'Este campo é obrigatório.')