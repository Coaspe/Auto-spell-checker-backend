from django.http import HttpResponse, HttpRequest
import os
import boto3
from enum import Enum


class ObjectKey(Enum):
    PATCHER_OBJECT_KEY = "PATCHER_OBJECT_KEY"
    EXECUTOR_OBJECT_KEY = "EXECUTOR_OBJECT_KEY"


OBJECT_KEY = "object_key"
LASTEST_VERSION = "LASTEST_VERSION"
BUCKET_NAME = "BUCKET_NAME"
AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
CONTENT_TYPE = "application/octet-stream"
CONTENT_DISPOSITION = "Content-Disposition"
CONTENT_DISPOSITION_VAL = 'attachment; filename="auto spell checker.exe"'
BODY = "Body"


def index(request: HttpRequest):
    return HttpResponse("Hello!")


def lastest_version(request: HttpRequest):
    return HttpResponse(os.getenv(LASTEST_VERSION))


def download_exe(request: HttpRequest):
    # Download auto_spell_checker.exe from AWS S3 and return it to the user
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv(AWS_ACCESS_KEY_ID),
        aws_secret_access_key=os.getenv(AWS_SECRET_ACCESS_KEY),
    )

    try:
        # Download the file from S3 bucket
        response = s3_client.get_object(
            Bucket=os.getenv(BUCKET_NAME), Key=os.getenv(request.GET[OBJECT_KEY])
        )

        file_content = response[BODY].read()

        response = HttpResponse(file_content, content_type=CONTENT_TYPE)
        response[CONTENT_DISPOSITION] = CONTENT_DISPOSITION_VAL

        return response

    except Exception as e:
        return HttpResponse(f"Error downloading file from S3: {e}", status=500)
