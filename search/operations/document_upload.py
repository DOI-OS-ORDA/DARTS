from django.http import HttpResponseRedirect

from search.models import Document
from search.operations.text_conversion import TextConversion
from search.operations.filename_normalizer import FilenameNormalizer

class DocumentUpload:

    def call(self, file, title, repo=Document):
        filename = file.name
        file_bytes = file.read()
        self.repo(
          body = TextConversion.from_file_bytes(filename, file_bytes),
          file = file_bytes,
          filename = filename,
          filename_normal = FilenameNormalizer().call(filename),
          title = title,
        ).save()
