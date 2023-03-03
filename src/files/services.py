from src import cfg
from src.files.models import FILES_M
import asyncpg


async def files_get_all_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_count = await FILES_M.objects.count()
        # log.info(f"count load successfuly: {all_count}")
        content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {FILES_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def files_get_by_root_folder(root_folder: str):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_ = await FILES_M.objects.all(FILES_M.root_folder == root_folder)
        all_count = len(all_)
        # log.info(f"count load successfuly: {all_count}")
        content = {
            "msg": "Success",
            "count": all_count,
            "data": all_
        }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {FILES_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content


async def files_get_by_query(str_query: str):
    content = {"msg": f"Unknown error"}
    str_query_local = str_query.strip().replace(" ", "&")
    try:
        print(str_query)
        all_ = await FILES_M.objects.filter(file_path_fts__match=str_query_local).all()
        # all_ = await FILES_M.objects.filter(FILES_M.file_path_fts.match(str_query_local)).all()
        all_count = len(all_)
        content = {
            "msg": "Success",
            "count": all_count,
            "data": all_
        }
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read from table {FILES_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content

# async def files_get_by_query(str_query: str):
#     content = {"msg": f"Unknown error"}
#     # log = set_logger(settings.WELL_FILE_LOG)
#     try:
#         # books = (
#         #     await Book.objects.filter(Book.author.name.icontains("tolkien"))
#         #     .order_by(Book.year.desc())
#         #     .all()
#         # )
#         # надо сохранять поисковый запрос...
#         print(str_query)
#         # order_by(Book.year.desc())
#         all_ = await FILES_M.objects.filter(FILES_M.file_path.icontains(str_query)).all()
#         all_count = len(all_)
#         # log.info(f"count load successfuly: {all_count}")
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": all_
#             }
#         return content
#     except Exception as e:
#         str_err = "Exception occurred " + str(e)
#         content = {"msg": f"reload fail. can't read from table {FILES_M.Meta.tablename}", "err": str(e)}
#         print(str_err)
#         # log.info(str_err)
#     return content


# async def files_get_by_query2(str_query: str):
#     content = {"msg": f"Unknown error"}
#     str_query_local =  str_query.strip().replace(" ", "&")
#     try:
#         print(str_query)
#         DB_DSN = f"postgresql://{cfg.DB_USER}:{cfg.DB_PASS}@{cfg.DB_HOST}:{cfg.DB_PORT}/{cfg.DB_NAME}"
#         conn = await asyncpg.connect(DB_DSN)
#         all_ = await FILES_M.objects.filter()
#         str_sql = f"SELECT * FROM files WHERE file_path_fts @@ to_tsquery('{str_query_local}') order by ts_rank(file_path_fts, plainto_tsquery('{str_query_local}'));"
#         row = await conn.fetch( str_sql )
#         all_count = len(row)
#         content = {
#             "msg": "Success",
#             "count": all_count,
#             "data": row
#             }
#         await conn.close()
#         return content
#     except Exception as e:
#         str_err = "Exception occurred " + str(e)
#         content = {"msg": f"reload fail. can't read from table {FILES_M.Meta.tablename}", "err": str(e)}
#         print(str_err)
#         # log.info(str_err)
#     return content
