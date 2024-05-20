import boto3
from os import getenv, path

from app.application.repositories.files_repository import FilesRepository


class AWSS3FilesRepositoryImpl(FilesRepository):
    def __init__(self, root_folder: str = "documents"):
        self.BUCKET_NAME = getenv("AWS_S3_BUCKET_NAME")
        self.PATH = root_folder
        self.REGION = getenv("AWS_S3_REGION")
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
        )

    def upload_object(self, file_bytes: bytes, filepath: str) -> str:
        if not filepath.lower().endswith(".png"):
            filepath += ".png"

        self.s3_client.put_object(
            Body=file_bytes, Bucket=self.BUCKET_NAME, Key=path.join(self.PATH, filepath)
        )
        return self.get_object_url(filepath)

    def get_object_url(self, filepath: str) -> str:
        path_in_bucket = path.join(self.PATH, filepath)
        return f"https://{self.BUCKET_NAME}.s3.{self.REGION}.amazonaws.com/{path_in_bucket}"
