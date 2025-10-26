from django import forms


class TranslationForm(forms.Form):
    CHOICES = [
        ('Желехівка', "Желехівка"),
        ('Максимовичівка', "Максимовичівка"),
        ('Кулішівка', "Кулішівка"),
        ('Драгоманівка', "Драгоманівка"),
            ]
    dialect = forms.ChoiceField(choices=CHOICES, label='Правопис')
    query = forms.CharField(widget=forms.Textarea, label='Текст')
