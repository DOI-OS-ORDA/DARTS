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
import os
import pandas
import re

from search.operations.text_conversion import TextConversion
from search.structs.struct import Struct
from search.repositories.cases import CasesRepository as CaseRepo
from search.repositories.documents import DocumentsRepository as DocRepo
# from search.repositories.events import EventsRepository
# from search.repositories.users import UsersRepository


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
        print(f"----> Importing {row.OriginalFileName}...")

        case = CaseRepo().find_or_create(int(row.CaseID), { 'name': row.CaseName })

        real_file_name = f"/app/test_data/heaping_bowl/{int(row.DocumentID)}_{row.OriginalFileName}"

        document = DocRepo().find_or_create(int(row.DocumentID), {
            'body': self.text_converter.from_filepath(real_file_name),
            'case_id': case.id,
            'category': row.Category,
            'file': open(real_file_name, "rb").read(),
            'filename': os.path.basename(row.OriginalFileName),
            'public': True,
            'title': row.DocumentName,
            'type': row.Type,
        })

        # document_entered_user = UserRepository.find_or_create({ 'slug': row.EnteredBy })

        # document_entered_event = EventRepository.create({
        #     'data': {
        #         'type': 'DocumentEntered',
        #         'document': document.id,
        #         'user': user.id,
        #         'timestamp': row.EnteredDate,
        #     }
        # })

        # document_modified_user = UserRepository.find_or_create({ 'slug': row.ModifiedBy })

        # document_modified_event = EventRepository.create({
        #     'data': {
        #         'type': 'DocumentModified',
        #         'document': document.id,
        #         'user': user.id,
        #         'timestamp': row.EnteredDate,
        #     }
        # })
