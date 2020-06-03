from django import forms

class CommentForm(forms.Form):
    autheur = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Votre Nom"
        })
    )
    contenu = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Laisse un commentaire"
        })
    )