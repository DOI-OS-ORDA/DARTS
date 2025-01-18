from django.core.management.base import BaseCommand, CommandError
from search.operations.documents_import import DocumentsImport


class Command(BaseCommand):
    help = "Imports documents into the database, converting PDFs/Word Docs to text"

    def add_arguments(self, parser):
        parser.add_argument("documents_path", nargs="?", type=str, default="test_data/docs/*")

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(f'Loading documents from {options["documents_path"]}')
        )
        DocumentsImport(options["documents_path"]).call()
        self.stdout.write(
            self.style.SUCCESS('Successfully imported documents')
        )
