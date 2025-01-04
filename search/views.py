from django.shortcuts import render
from .forms import SearchForm
from search.models import Document
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import os
import subprocess
from django.http import FileResponse
import io
import mimetypes

from darts.operations import DocumentSearch

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        query = request.POST.get('query')
        results = DocumentSearch().call(query)
        return render(request, 'search.html', {'form': form, 'results': results, 'searched': True, query: query})
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
            file = upload.read()
            body = __convert_doc(name, file)

            newdoc = Document(file = file, filename = name, body = body)
            newdoc.save()
            return HttpResponseRedirect('/upload/')

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'count': count})


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})

def view_doc(request):
    doc_name = request.GET.get('doc')
    document = Document.objects.get(filename = doc_name)

    buffer = io.BytesIO(document.file)
    buffer.seek(0)
    mimetype = mimetypes.guess_type(document.filename)[0]
    return FileResponse(buffer, filename=document.filename, content_type=mimetype)


def __convert_doc(name, file):
    base, ext = os.path.splitext(name)
    if ext == '.docx':
        command = f'pandoc -f docx -t markdown'
    elif ext == '.pdf':
        command = f'pdftotext - -'

    # pass file contents via stdin, get converted file via stdout
    return subprocess.check_output(command, input=file, shell=True).decode(encoding='utf-8')


