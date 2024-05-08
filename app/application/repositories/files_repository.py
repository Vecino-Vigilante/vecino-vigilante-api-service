from abc import ABC, abstractmethod
import base64
import imghdr

class FilesRepository(ABC):
    
    def get_path_with_extension(self, path: str, file_bytes: bytes):
        extension = imghdr.what(None, h=file_bytes)
        return f"{path}.{extension}" if extension else path

    def upload_base64(self, base64str: str, path: str):
        file_bytes = base64.b64decode(base64str)
        relative_path = self.get_path_with_extension(path, file_bytes)
        return self.upload_object(file_bytes, relative_path)
    
    @abstractmethod
    def upload_object(self, file_bytes: bytes, filepath: str) -> str:
        pass
    