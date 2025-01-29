from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .context_processors import current_user
from .forms import SearchForm, UploadFileForm
from .models import Document
from .operations.document_search import DocumentSearch
from .operations.document_upload import DocumentUpload
from .operations.document_view import DocumentView
from .repositories.search_results import SearchResultsRepository
from .repositories.users import UsersRepository


class Search(View):

    def post(self, request):
        query = request.POST.get('query')
        context = {
            'form': SearchForm(request.POST),
            'query': query,
            'results': DocumentSearch(query, searcher = current_user(request)['current_user']).call(),
            'searched': True,
        }
        return render(request, 'search.html', context)

    def get(self, request):
        context = { 'form': SearchForm() }
        return render(request, 'search.html', context)


def set_user(request, **kwargs):
    request.session.update({"user.type": kwargs.get('type')})
    return HttpResponseRedirect('/search')


class Upload(View):

    def post(self, request):
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

    def get(self, request):
        context = {
          'form': UploadFileForm(),
          'count': Document.objects.count
        }
        return render(request, 'upload.html', context)


def list(request):
    docs = Document.objects.all()
    return render(request, 'list.html', {'docs': docs})


def view_doc(request, id, slug=None):
    if slug == None:
        doc = Document.objects.get(pk=id)
        return redirect('document', id, doc.slug)

    buffer, filename, mimetype = DocumentView(id).call()
    return FileResponse(buffer, filename=filename, content_type=mimetype)


