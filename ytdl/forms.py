from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Ingrese la URL del video a descargar' }), label=False)
