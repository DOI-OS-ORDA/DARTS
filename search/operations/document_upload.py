from django.http import HttpResponseRedirect

from search.forms import UploadFileForm
from search.models import Document
from search.operations.text_conversion import TextConversion
from search.operations.filename_normalizer import FilenameNormalizer

class DocumentUpload:
    def call(self, form, request):
        match form.is_valid():
            case True:
                upload = request.FILES['file']
                filename = upload.name
                body = TextConversion.from_file_bytes(filename, upload.read())
                newdoc = Document(
                  body = body,
                  file = upload.read(),
                  filename = filename,
                  filename_normal = FilenameNormalizer().call(filename),
                  title = request.POST.get('title'),
                )
                newdoc.save()
                return HttpResponseRedirect('/upload/')

            case False:
                return form
