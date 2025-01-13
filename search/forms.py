from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100)

class UploadFileForm(forms.Form):
    title = forms.CharField(label="Document title", max_length=255)
    file = forms.FileField()
