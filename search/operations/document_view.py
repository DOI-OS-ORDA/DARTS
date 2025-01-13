import io
import mimetypes
from django.http import FileResponse

from search.models import Document

class DocumentView:
    def call(self, request):
        doc_name = request.GET.get('doc')
        document = Document.objects.get(filename = doc_name)

        buffer = io.BytesIO(document.file)
        buffer.seek(0)
        mimetype = mimetypes.guess_type(document.filename)[0]
        return FileResponse(buffer, filename=document.filename, content_type=mimetype)
