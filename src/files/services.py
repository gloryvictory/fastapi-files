from src.files.models import FILES_M


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


async def files_get_by_area(area: str):
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        # books = (
        #     await Book.objects.filter(Book.author.name.icontains("tolkien"))
        #     .order_by(Book.year.desc())
        #     .all()
        # )
        print(area)
        all_ = await FILES_M.objects.contains(area)
            # all(FILES_M.root_folder == area)

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
        content = {"msg": f"reload fail. can't read from table {FILES_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content
