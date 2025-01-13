from django.http import HttpResponseRedirect

from search.forms import UploadFileForm
from search.models import Document
from search.operations.text_conversion import TextConversion

class DocumentUpload:
    def call(self, form, request):
        match form.is_valid():
            case True:
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

            case False:
                return form

    def params(self):
        pass
