from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT

metadata = MetaData()

# , nullable=True
FILES_M = Table(
    "files",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("root_folder", TEXT),
    Column("file_path", TEXT),
    Column("file_folder", TEXT),
    Column("file_name", String),
    Column("file_ext", String),
    Column("file_size", BIGINT),
    Column("file_ctime", TIMESTAMP),
    Column("file_mtime", TIMESTAMP),
    Column("date_m", String),
    Column("date_u", String),
    Column("fpath", TEXT),
    Column("fpath_md5", TEXT),
    Column("lastupdate", TIMESTAMP),
)
