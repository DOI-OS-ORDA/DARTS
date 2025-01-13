from django.shortcuts import render

from .forms import SearchForm, UploadFileForm
from .models import Document
from .operations.document_search import DocumentSearch
from .operations.document_upload import DocumentUpload
from .operations.document_view import DocumentView
from .repositories.search_results import SearchResultsRepository

def search(request):
    match request.method:
        case 'POST':
            form = SearchForm(request.POST)
            query = request.POST.get('query')
            results = SearchResultsRepository().call(query)
            params = {'form': form, 'results': results, 'searched': True, 'query': query}
        case 'GET':
            form = SearchForm()
            params = {'form': form}

    return render(request, 'search.html', params)


def upload(request):
    match request.method:
        case 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            DocumentUpload().call(form, request)
        case 'GET':
            form = UploadFileForm()

    return render(request,
        'upload.html',
        {'form': form, 'count': Document.objects.count}
    )


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})


def view_doc(request):
    return DocumentView().call(request)


