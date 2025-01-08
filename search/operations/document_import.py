from darts.repositories import DocumentsRepository
from search.operations.text_conversion import TextConversion

class DocumentImport:

    # @inject
    # def __init__(self, file_path: str, repository = Provide["repo.documents"], converter = ["ops.text"]):
    def __init__(self, file_path: str, repository = DocumentsRepository(), converter = TextConversion):
        self.file_path = file_path
        self.repository = repository
        self.text_converter = converter

    def call(self) -> None:
        self.repository.add(
            filename = self.file_path,
            file = open(self.file_path, "rb").read(),
            body = self.text_converter.from_filepath(self.file_path)
        )
