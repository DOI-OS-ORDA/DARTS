from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
