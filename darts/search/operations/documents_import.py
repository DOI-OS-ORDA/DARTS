import glob
import os
import pandas
import random
import string

from search.models import Document
from search.operations.document_import import DocumentImport


# To do: DI the repository and config file path
# make "repo.documents" a factory
class DocumentsImport:
    def __init__(self, documents_dir: str, metadata_file: str, repository=Document):
        self.documents_dir = documents_dir
        self.metadata_file = metadata_file
        self.repository = repository

    def call(self):
        print("----> [START] Starting document import...")
        filepaths = glob.glob(self.documents_dir)
        metadata = pandas.read_csv(self.metadata_file)
        for path in filepaths:
            print(f"----> Importing {path}...")
            md = self.choose_metadata(metadata, path)
            DocumentImport(path, md["title"], md["public"], self.repository).call()
        print("----> [END] Document import complete!")

    def choose_metadata(self, metadata, path):
        datarow = self.has_metadata(metadata, path)
        if datarow is False:  # lacking real metadata, fall back to randomly-generated
            return self.fake_metadata()
        else:
            return self.get_metadata(datarow)

    def has_metadata(self, metadata, path):
        nrdarid = os.path.basename(path).split("_")[0]
        if not nrdarid.isdigit():
            return False  # if filename starts with NRDARDocumentID
        datarow = metadata[
            metadata["NRDARDocumentID"] == int(nrdarid)
        ]  # find metadata by id
        return False if datarow.empty else datarow

    def get_metadata(self, datarow):
        return {
            "public": datarow["PubliclyDisplayed"].iloc[0],
            "title": datarow["Document Name"].iloc[0],
        }

    def fake_metadata(self):
        return {
            "public": random.choice([True, False]),
            "title": "".join(random.choice(string.ascii_uppercase) for _ in range(10)),
        }
