import glob, os, pandas, random, string
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
        metadata = pandas.read_csv(self.metadata_file)
        for path in filepaths:
            print(f"----> Importing {path}...")
            datarow = self.has_metadata(metadata, path)
            if datarow is False:
                md = self.fake_metadata()
            else:
                md = self.get_metadata(datarow)
            DocumentImport(path, md['title'], md['public'], self.repository).call()
        print(f"----> [END] Document import complete!")


    def has_metadata(self, metadata, path):
        nrdarid = os.path.basename(path).split('_')[0]
        if not nrdarid.isdigit(): return(False) # if filename starts with NRDARDocumentID
        datarow = metadata[metadata['NRDARDocumentID']==int(nrdarid)] # find the metadata
        return(False if datarow.empty else datarow)


    def get_metadata(self, datarow):
        return({
            'public': datarow['PubliclyDisplayed'].iloc[0],
            'title':  datarow['Document Name'].iloc[0],
            'type':   datarow['Type'].iloc[0],
            'desc':   datarow['Description'].iloc[0],
            'date':   datarow['DocumentDt'].iloc[0],
        })


    def fake_metadata(self):
        return({
            'public': random.choice([True, False]),
            'title':  ''.join(random.choice(string.ascii_uppercase) for _ in range(10)),
            'type':   'Fake',
            'desc':   'A test file with fake metadata',
            'date':   '1/1/1970',
        })

