from django import forms
from .models import Portfolio, ContentSection
from django.forms import inlineformset_factory

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['titulo_projeto', 'nome_exibicao']
        # widgets = {
        #     # Torna o título e o slug invisíveis no HTML
        #     'titulo_projeto': forms.HiddenInput(),
        #     'slug': forms.HiddenInput(),
        #     # Mantém o seletor de cor
        #     'cor_fundo': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dizemos ao Django que o slug não é obrigatório NO FORMULÁRIO
        # (mas ele continua sendo obrigatório no Banco de Dados)
        if 'slug' in self.fields:
            self.fields['slug'].required = False

class ContentSectionForm(forms.ModelForm):
    class Meta:
        model = ContentSection
        fields = ['titulo_secao', 'conteudo', 'cor_bloco', 'ordem'] # ADICIONE cor_bloco AQUI
        widgets = {
            'cor_bloco': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
            'conteudo': forms.Textarea(attrs={'rows': 3}),
            'ordem': forms.HiddenInput(),
        }

# O Formset deve usar o seu ContentSectionForm personalizado
SectionFormSet = inlineformset_factory(
    Portfolio,
    ContentSection,
    form=ContentSectionForm, # <--- IMPORTANTE: Usar o form que definimos acima
    extra=1,
    can_delete=True
)