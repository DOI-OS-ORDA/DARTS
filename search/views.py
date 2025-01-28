from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import SearchForm, UploadFileForm
from .models import Document
from .operations.document_search import DocumentSearch
from .operations.document_upload import DocumentUpload
from .operations.document_view import DocumentView
from .repositories.search_results import SearchResultsRepository
from .repositories.users import UsersRepository

def search(request):
    match request.method:
        case 'POST':
            query = request.POST.get('query')
            current_user = UsersRepository.get(request.session.get("user.type", "guest"))
            params = {
                'form': SearchForm(request.POST),
                'query': query,
                'results': DocumentSearch(query, searcher = current_user).call(),
                'searched': True,
                'user_types': UsersRepository.all(),
                'user_type': current_user.name,
            }
            return render(request, 'search.html', params)
        case 'GET':
            form = SearchForm()
            params = {
                'form': form,
                'user_types': UsersRepository.all(),
                'user_type': UsersRepository.get(request.session.get("user.type", "guest")).name
            }
            return render(request, 'search.html', params)

def set_user(request, **kwargs):
    request.session.update({"user.type": kwargs.get('type')})
    return HttpResponseRedirect('/search')

def upload(request):
    match request.method:
        case 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            match form.is_valid():
                case True:
                    DocumentUpload().call(
                        request.FILES['file'],
                        request.POST.get('title'),
                        request.POST.get('public'),
                    )
                    return HttpResponseRedirect('/upload/')
                case False:
                    return form
        case 'GET':
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form, 'count': Document.objects.count})


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})


def view_doc(request, id, slug=None):
    if slug == None:
        doc = Document.objects.get(pk=id)
        return redirect('document', id, doc.slug)

    buffer, filename, mimetype = DocumentView(id).call()
    return FileResponse(buffer, filename=filename, content_type=mimetype)


