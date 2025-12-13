from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    
    # Campo Telefone solicitado no slide 85
    telefone = forms.CharField(
        label='Telefone / WhatsApp',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'})
    )

    # Campo Assunto solicitado no slide 86 com choices
    ASSUNTO_CHOICES = [
        ('suporte', 'Suporte técnico'),
        ('comercial', 'Comercial'),
        ('reclamacao', 'Reclamação'),
        ('parceria', 'Parceria'),
        ('financeiro', 'Financeiro'),
    ]
    
    assunto = forms.ChoiceField(
        choices=ASSUNTO_CHOICES,
        label='Assunto do contato',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )

class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'})
    )
    preco = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Preço',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço do produto'})
    )