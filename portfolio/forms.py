from django import forms
from .models import Portfolio, ContentSection
from django.forms import inlineformset_factory

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['titulo_projeto', 'nome_exibicao','cor_header', 'cor_nav', 'cor_footer', 'cor_fundo']

        widgets = {
            # 'titulo_projeto': forms.HiddenInput(),
            'slug': forms.HiddenInput(),
            'cor_fundo': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
            'cor_header': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
            'cor_nav': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
            'cor_footer': forms.TextInput(attrs={'type': 'color', 'class': 'form-control-color'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:
            self.fields['slug'].required = False
        self.instance.slug = "temp-slug"

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