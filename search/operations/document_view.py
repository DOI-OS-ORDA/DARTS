import io
import mimetypes

from search.models import Document

class DocumentView:

    def __init__(self, filename, repo=Document):
        self.filename = filename
        self.repository = repo


    def call(self):
        document = self.repository.objects.get(filename = self.filename)
        buffer = io.BytesIO(document.file)
        buffer.seek(0)
        mimetype = mimetypes.guess_type(document.filename)[0]
        return [buffer, self.filename, mimetype]
