import io
import mimetypes

from search.models import Document

class DocumentView:

    def __init__(self, id, repo=Document):
        self.id = id
        self.repository = repo


    def call(self):
        document = self.repository.objects.get(pk = self.id)
        buffer = io.BytesIO(document.file)
        buffer.seek(0)
        mimetype = mimetypes.guess_type(document.filename)[0]
        return [buffer, document.filename, mimetype]
