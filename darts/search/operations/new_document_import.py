# CaseID
# CaseName
# DocumentID
# DocumentName
# Description
# OriginalFileName
# Category
# Type
# FundingRequestYR -> What does Funding Request Year belong to?
# DocumentDate
# EnteredBy
# EnteredDate
# ModifiedBy
# ModifiedDate
# Public
import gc
import os
import pandas
from subprocess import CalledProcessError  # nosec B404

from search.operations.text_conversion import TextConversion
from search.structs.struct import Struct
from search.repositories.cases import CasesRepository as CaseRepo
from search.models import Document


class NewDocumentImport:

    def __init__(self, metadata_file: str = "/app/test_data/new_metadata.csv"):
        self.metadata_file = metadata_file
        self.text_converter = TextConversion

    def call(self):
        print("----> [START] Starting document import...")
        dataframe = pandas.read_csv(self.metadata_file)
        for i in range(len(dataframe)):
            self.do_import(dataframe.iloc[i])

    def do_import(self, row_data):
        row = Struct(dict(row_data))
        real_file_name = (
            f"/app/test_data/heaping_bowl/{int(row.DocumentID)}_{row.OriginalFileName}"
        )

        print(f"----> Importing {real_file_name}...")

        case = CaseRepo().find_or_create(int(row.CaseID), {"name": row.CaseName})

        with os.fdopen(os.open(real_file_name, os.O_RDONLY), "rb") as file:
            try:
                Document.objects.get(pk=int(row.DocumentID))
            except Document.DoesNotExist:
                try:
                    document = Document(
                        id=int(row.DocumentID),
                        body=self.text_converter.from_filepath(real_file_name),
                        case_id=case.id,
                        category=row.Category,
                        file=file.read(),
                        filename=os.path.basename(row.OriginalFileName),
                        public=True,
                        title=row.DocumentName,
                        type=row.Type,
                    )
                    document.save()
                    del document
                    gc.collect()
                except CalledProcessError:
                    print(f"Couldn't import {real_file_name}")

        # Reading the file then setting Document#file to a test set of bytes
        # works quickly and is fine.

        # The problem happens when the Document#file = bytea.
        # So it's not garbage collection in here -- it's something with
        # how the document is created. What if we did the document model directly?

        # TODO Next: set up person accounts, find by slug
        # document_entered_user = UserRepo.find_or_create({ 'slug': row.EnteredBy })

        # document_entered_event = EventRepo.create({
        #     'type': 'DocumentEntered',
        #     'data': {
        #         'document': document.id,
        #         'user': user.id,
        #         'timestamp': row.EnteredDate,
        #     }
        # })

        # document_modified_user = UserRepo.find_or_create({ 'slug': row.ModifiedBy })

        # document_modified_event = EventRepo.create({
        #     'type': 'DocumentModified',
        #     'data': {
        #         'document': document.id,
        #         'user': user.id,
        #         'timestamp': row.EnteredDate,
        #     }
        # })
