from datetime import datetime

from pydantic import BaseModel


class FILES_S(BaseModel):
    id: int
    root_folder: str
    file_path: str
    file_folder: str
    file_name: str
    file_ext: str
    file_size: str
    file_ctime: datetime
    file_mtime: datetime
    date_m: str
    date_u: str
    date_m: str
    fpath: str
    fpath_md5: str
    lastupdate: datetime

    class Config:
        orm_mode = True
