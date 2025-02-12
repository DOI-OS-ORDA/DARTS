import os
import subprocess

class TextConversion:

    @classmethod
    def from_filepath(cls, file_path: str):
        return subprocess.check_output(cls.command_text(file_path), shell=True).decode(encoding='utf-8')

    @classmethod
    def from_file_bytes(cls, filename: str, file_bytes: bytes):
        return subprocess.check_output(cls.command_text_bytes(filename), input=file_bytes, shell=True).decode(encoding='utf-8')

    def command_text(file_path):
        base, ext = os.path.splitext(file_path)
        match ext:
            case ".docx":
                return f'pandoc -d pandoc.yml -f docx -t markdown "{file_path}"'
            case ".pdf":
                return f'pdftotext "{file_path}" -'

    def command_text_bytes(filename):
        base, ext = os.path.splitext(filename)
        match ext:
            case ".docx":
                return f'pandoc -d pandoc.yml -f docx -t markdown'
            case ".pdf":
                return f'pdftotext - -'
