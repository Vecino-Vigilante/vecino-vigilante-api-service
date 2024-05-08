import boto3
from os import getenv, path

from dotenv import load_dotenv

from app.application.repositories.files_repository import FilesRepository

load_dotenv()

class AWSS3FilesRepositoryImpl(FilesRepository):
    BUCKET_NAME = getenv("AWS_S3_BUCKET_NAME")
    PATH = getenv("AWSS3_BUCKET_ROOT_FOLDER")
    REGION = getenv("AWS_S3_REGION")
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    )

    def upload_object(self, file_bytes: bytes, filepath: str) -> str:
        self.s3_client.put_object(
            Body=file_bytes, Bucket=self.BUCKET_NAME, Key=path.join(self.PATH, filepath)
        )
        return self.get_object_url(filepath)

    def get_object_url(self, filepath: str) -> str:
        path_in_bucket = path.join(self.PATH, filepath)
        return f"https://{self.BUCKET_NAME}.s3.{self.REGION}.amazonaws.com/{path_in_bucket}"