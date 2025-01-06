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

from search.operations.document_search import DocumentSearch
from search.operations.text_conversion import TextConversion

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        query = request.POST.get('query')
        results = DocumentSearch(query).results()
        return render(request, 'search.html', {'form': form, 'results': results, 'searched': True, 'query': query})
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form})


def upload(request):
    count = Document.objects.count
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = request.FILES['file']
            filename = upload.name
            body = TextConversion.from_file_bytes(filename, upload.read())
            newdoc = Document(
              file = upload.read(),
              filename = filename,
              body = body
            )
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


