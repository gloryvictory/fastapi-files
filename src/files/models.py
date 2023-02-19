from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT

metadata = MetaData()

# # , nullable=True
# FILES_M = Table(
#     "files",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("root_folder", TEXT),
#     Column("file_path", TEXT),
#     Column("file_folder", TEXT),
#     Column("file_name", String),
#     Column("file_ext", String),
#     Column("file_size", BIGINT),
#     Column("file_ctime", TIMESTAMP),
#     Column("file_mtime", TIMESTAMP),
#     Column("date_m", String),
#     Column("date_u", String),
#     Column("fpath", TEXT),
#     Column("fpath_md5", TEXT),
#     Column("lastupdate", TIMESTAMP),
# )

from datetime import datetime
import ormar

from src.database import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class FILES_M(ormar.Model):
    class Meta(MainMeta):
        tablename = "files"
        pass

    id: int = ormar.Integer(primary_key=True)
    root_folder: str = ormar.Text()
    file_path: str = ormar.Text()
    file_folder: str = ormar.Text()
    file_name: str = ormar.String(max_length=255)
    file_ext: str = ormar.String(max_length=11)
    file_size: str = ormar.BigInteger()
    file_ctime: str = ormar.DateTime(default=datetime.now)
    file_mtime: str = ormar.DateTime(default=datetime.now)
    date_c: str = ormar.String(max_length=11)
    date_m: str = ormar.String(max_length=11)
    date_u: str = ormar.String(max_length=11)
    fpath: str = ormar.Text()
    fpath_md5: str = ormar.Text()
    lastupdate: datetime = ormar.DateTime(default=datetime.now)