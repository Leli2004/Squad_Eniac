from django import forms
from app_voluntarios.models import Voluntario

class VoluntariosForms(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'email', 'telefone', 'profissão', 'info_geral']

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        telefone = cleaned_data.get('telefone')
        profissao = cleaned_data.get('profissão')
        info_geral = cleaned_data.get('info_geral')

        if not nome:
            self.add_error('nome', 'Este campo é obrigatório.')
        if not email:
            self.add_error('email', 'Este campo é obrigatório.')
        if not telefone:
            self.add_error('telefone', 'Este campo é obrigatório.')
        if not profissao:
            self.add_error('profissão', 'Este campo é obrigatório.')
        if not info_geral:
            self.add_error('informações', 'Este campo é obrigatório.')
