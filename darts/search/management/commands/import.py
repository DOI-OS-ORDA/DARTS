from django.core.management.base import BaseCommand
from search.operations.new_document_import import NewDocumentImport


class Command(BaseCommand):
    help = "Imports documents into the database, converting PDFs/Word Docs to text"

    def add_arguments(self, parser):
        parser.add_argument(
            "documents_dir", nargs="?", type=str, default="test_data/docs/*"
        )
        parser.add_argument(
            "metadata_file",
            nargs="?",
            type=str,
            default="/app/test_data/new_metadata.csv",
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(f'Loading documents from {options["documents_dir"]}')
        )
        NewDocumentImport(options["metadata_file"]).call()
        self.stdout.write(self.style.SUCCESS("Successfully imported documents"))
