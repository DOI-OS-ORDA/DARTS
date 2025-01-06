import os
import subprocess

class TextConversion:

    @classmethod
    def call(cls, file_path):
        return subprocess.check_output(cls.command_text(file_path), shell=True).decode(encoding='utf-8')

    def command_text(file_path):
        base, ext = os.path.splitext(file_path)
        match ext:
            case ".docx":
                return f'pandoc -f docx -t markdown "{file_path}"'
            case ".pdf":
                return f'pdftotext "{file_path}" -'
