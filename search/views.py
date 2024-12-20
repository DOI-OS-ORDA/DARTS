from django.shortcuts import render
from .forms import SearchForm
from search.models import Document
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = Document.objects.all()
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form, 'docs': docs})

def upload(request):
    count = Document.objects.count
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(file_binary = request.FILES['file'].read())
            newdoc.save()
            return HttpResponseRedirect('/upload/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'count': count})
