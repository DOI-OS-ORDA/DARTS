from django.shortcuts import render
from .forms import SearchForm
from search.models import Document

def search(request):

    docs = 'test'
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = Document.objects.all()
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'docs': docs})
