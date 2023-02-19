from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from typing import List # Dict,

# from src.database import get_async_session
from src.files.models import FILES_M
# from src.files.schemas import FILES_S


router_files = APIRouter(
    prefix="/files",
    tags=["Файлы"]
)


# operation_type: str,
# -> list[City]
#, response_model=List[FILES_S]
# session: AsyncSession = Depends(get_async_session)
@router_files.get("")
async def well_get_all_count() :
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        # table_exist = ngo.
        well_all_count = await FILES_M.objects.count()

        # log.info(f"count load successfuly: {well_all_count}")
        content = {"msg": "Success", "count": well_all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {FILES_M.Meta.tablename}", "err": str(e)}

        print(str_err)
        # log.info(str_err)
    return content

    # try:
    #     # .limit(20)
    #     # query = select(FILES.select()).fetch()
    #     # await session.execute(text("SET search_path TO public;"))
    #     query = select(FILES_M).limit(20)
    #     results = await session.execute(query)
    #
    #     # query = select(FILES_M).limit(20)
    #     # result = await session.execute(query)
    #
    #     # result.all(),
    #     return {
    #         "status": "success",
    #         "data": [dict(result) for result in results],
    #         "details": None
    #     }
    # except Exception as e:
    #     # Передать ошибку разработчикам
    #     raise HTTPException(status_code=500, detail={
    #         "status": "error",
    #         "data": None,
    #         "details": str(e.__str__())
    #     })

# @router.post("")
# async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}
