from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        label = False,
        max_length = 140,
        widget = forms.TextInput(attrs={
            'class': 'usa-input',
            'id': 'search-field-en-big',
            'type': 'search',
            'name': 'search',
        })
    )

class UploadFileForm(forms.Form):
    title = forms.CharField(label="Document title", max_length=255)
    file = forms.FileField(
        label = "Upload a PDF or DOCX",
        widget = forms.TextInput(attrs={
            'class': 'usa-file-input',
            'id': 'file-input-single',
            'name': 'file-input-single',
            'type': 'file',
        })
    )
