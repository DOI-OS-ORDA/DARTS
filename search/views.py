from django.shortcuts import render
from .forms import SearchForm
from search.models import Document
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = Document.objects.all()
        return render(request, 'search.html', {'form': form, 'docs': docs})
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form})


def upload(request):
    count = Document.objects.count
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = request.FILES['file']
            newdoc = Document(file_binary = upload.read() , file_name = upload.name)
            newdoc.save()
            return HttpResponseRedirect('/upload/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'count': count})


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})

