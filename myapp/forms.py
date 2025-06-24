from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-form'})
    )
    apellido = forms.CharField(
        label="Apellido",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-form'})
    )
    ci = forms.CharField(
        label="CI",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'input-form'})
    )
    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'input-form'})
    )
    contrasena = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'input-form'})
    )