from playhouse.postgres_ext import (
    Model,TextField,BigAutoField, DateTimeField
)
from datetime import datetime
from db import db
class FileUploader(Model):
    id = BigAutoField(primary_key=True)
    file_name = TextField(index=True)
    # performed_by_id = CharField(index=True)
    file_path = TextField()
    created_at = DateTimeField(default = datetime.now())

    class Meta:
        database = db
        table_name = "file_uploader"