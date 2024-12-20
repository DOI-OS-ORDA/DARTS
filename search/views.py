from django.shortcuts import render
from .forms import SearchForm
from search.models import Document
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import os
import subprocess

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = Document.objects.all() # TODO: replace with actual search query
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
            name = upload.name

            # TODO: break into fuctions, save search_text
            base, ext = os.path.splitext(name)
            match ext:
                case ".docx":
                    command = f'pandoc -f docx -t markdown "test_docs/{name}"'
                case ".pdf":
                    command = f'pdftotext "test_docs/{name}" -'
            body = subprocess.check_output(command, shell=True).decode(encoding='utf-8')

            newdoc = Document(file_binary = upload.read() , file_name = name, file_text = body)
            newdoc.save()
            return HttpResponseRedirect('/upload/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'count': count})


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})

