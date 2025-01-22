from django.core.management.base import BaseCommand, CommandError
from search.operations.documents_import import DocumentsImport


class Command(BaseCommand):
    help = "Imports documents into the database, converting PDFs/Word Docs to text"

    def add_arguments(self, parser):
        parser.add_argument("documents_dir", nargs="?", type=str, default="test_data/docs/*")
        parser.add_argument("metadata_file", nargs="?", type=str, default="test_data/metadata.csv")

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(f'Loading documents from {options["documents_dir"]}')
        )
        DocumentsImport(options["documents_dir"], options["metadata_file"]).call()
        self.stdout.write(
            self.style.SUCCESS('Successfully imported documents')
        )
