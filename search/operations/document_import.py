from darts.repositories import DocumentsRepository
from search.operations.text_conversion import TextConversion

import string
import random

class DocumentImport:

    # @inject
    # def __init__(self, file_path: str, repository = Provide["repo.documents"], converter = ["ops.text"]):
    def __init__(self, file_path: str, repository = DocumentsRepository(), converter = TextConversion):
        self.file_path = file_path
        self.repository = repository
        self.text_converter = converter


    def call(self) -> None:
        self.repository.add(
            filename = self.file_path.split('/')[-1],
            file = open(self.file_path, "rb").read(),
            body = self.text_converter.from_filepath(self.file_path),
            title = ''.join(random.choice(string.ascii_uppercase) for _ in range(10)),
            public = random.choice([True, False])
        )
