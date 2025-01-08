import glob
from darts.repositories import DocumentsRepository
from search.operations.document_import import DocumentImport

# To do: DI the repository and config file path
# make "repo.documents" a factory
# def __init__(self, folder_path: str = Provide["config.documents_pattern"], repository = Provide["repo.documents"]):
class DocumentsImport:
    def __init__(self, folder_path: str = './darts/docs/*', repository = DocumentsRepository()):
        self.folder_path = folder_path
        self.repository = repository

    def call(self):
        print(f"----> [START] Starting document import...")
        filepaths = glob.glob(self.folder_path)
        for path in filepaths:
            print(f"----> Importing {path}...")
            DocumentImport(path, self.repository).call()
        print(f"----> [END] Document import complete!")
