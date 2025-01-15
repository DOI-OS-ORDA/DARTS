import io
import mimetypes
from django.http import FileResponse

from search.models import Document

class DocumentView:
    def call(self, request):
        document = Document.objects.get(filename = request.GET.get('filename'))
        buffer = io.BytesIO(document.file)
        buffer.seek(0)
        mimetype = mimetypes.guess_type(document.filename)[0]
        return FileResponse(buffer, filename=document.filename, content_type=mimetype)
