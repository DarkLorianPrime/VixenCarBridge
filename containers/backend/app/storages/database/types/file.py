import datetime
import re
import uuid
from typing import Optional, Any

from fastapi import UploadFile
from sqlalchemy import TypeDecorator, types, Dialect

from storages.cdn.s3_minio import get_minio


class File(TypeDecorator):
    cache_ok = True

    impl = types.String

    def __init__(
            self,
            bucket: str,
            is_need_folder: bool = True
    ):
        super().__init__()
        self.bucket = bucket
        self.folder = is_need_folder

    def process_bind_param(self, value: Optional[UploadFile], _: Dialect) -> Any:
        if not value:
            return

        folder = ""
        if self.folder:
            folder = datetime.datetime.now().strftime("%Y%m%d")

        minio = get_minio()
        filename_uuid = uuid.uuid4()
        file_type = re.search(r"(\.[0-9a-z]+)$", value.filename or "")
        filename = f"{folder}/{str(filename_uuid)}"
        if file_type:
            filename += file_type.group(0)

        minio.put_object(
            bucket_name=self.bucket,
            object_name=filename,
            data=value.file,
            length=-1,
            part_size=10485760
        )

        return filename
