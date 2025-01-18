import glob, os
from darts.repositories import DocumentsRepository
from search.operations.document_import import DocumentImport

# To do: DI the repository and config file path
# make "repo.documents" a factory
# def __init__(self, folder_path: str = Provide["config.documents_pattern"], repository = Provide["repo.documents"]):
class DocumentsImport:
    def __init__(self, documents_dir: str, metadata_file: str, repository = DocumentsRepository()):
        self.documents_dir = documents_dir
        self.metadata_file = metadata_file
        self.repository = repository


    def call(self):
        print(f"----> [START] Starting document import...")
        filepaths = glob.glob(self.documents_dir)
        for path in filepaths:
            print(f"----> Importing {path}...")
            metadata = self.find_metadata()
            DocumentImport(path, metadata['title'], metadata['public'], self.repository).call()
        print(f"----> [END] Document import complete!")


    # Each filename appears to be prepended with a NRDARDocumentID, thus we match files to ids
    def find_metadata(filepath):
        #os.path.basename(filepath)
        return({'title': 'A Fake Title', 'public': True})

