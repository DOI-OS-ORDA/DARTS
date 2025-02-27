from search.repositories.repository import Repository
from search.models import Document


class DocumentsRepository(Repository):
    relation = Document
