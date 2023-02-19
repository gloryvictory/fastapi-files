from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from typing import List # Dict,

from src.database import get_async_session
from src.files.models import FILES_M
from src.files.schemas import FILES_S


router_files = APIRouter(
    prefix="/files",
    tags=["Файлы"]
)


# operation_type: str,
# -> list[City]
#, response_model=List[FILES_S]
@router_files.get("")
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)) :
    try:
        # .limit(20)
        # query = select(FILES.select()).fetch()
        # await session.execute(text("SET search_path TO public;"))
        query = select(FILES_M).limit(20)
        results = await session.execute(query)

        # query = select(FILES_M).limit(20)
        # result = await session.execute(query)

        # result.all(),
        return {
            "status": "success",
            "data": [dict(result) for result in results],
            "details": None
        }
    except Exception as e:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": str(e.__str__())
        })

# @router.post("")
# async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(operation).values(**new_operation.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success"}
