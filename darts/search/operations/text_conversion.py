import os
import subprocess  # nosec B404


class TextConversion:

    command_path = "/app/bin/doc"

    @classmethod
    def from_filepath(cls, file_path: str):
        params = [cls.command_path, cls.ext(file_path), "path", file_path]
        return subprocess.check_output(params, shell=False).decode(  # nosec B603
            encoding="utf-8"
        )

    @classmethod
    def from_file_bytes(cls, filename: str, file_bytes: bytes):
        params = [cls.command_path, cls.ext(filename), "bytes"]
        return subprocess.check_output(  # nosec B603
            params, input=file_bytes, shell=False
        ).decode(encoding="utf-8")

    @classmethod
    def ext(cls, file_path):
        base, ext = os.path.splitext(file_path)
        # Trim the first character to remove the leading dot (ex: ".docx" -> "docx")
        return ext[1:]
