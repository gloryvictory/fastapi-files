from fastapi import APIRouter, Depends, HTTPException

from src.files.services import files_get_all_count, files_get_by_root_folder, files_get_by_area


router_files = APIRouter(
    # prefix="/files",
    tags=["Файлы"]
)


@router_files.get(path='/count',
                 status_code=200,
                 name='Получить количество Файлов',
                 tags=['Файлы'],
                 description='Получает количество Файлов')
async def get_count():
    content = await files_get_all_count()
    return content


# response_model = List[FILES_S],
@router_files.get(path="/{root_folder}",
                 status_code=200,
                 name='Получить список Файлов по ROOT_FOLDER',
                 tags=['Файлы'],
                 description='Получает список Файлов по конкретной ROOT_FOLDER'
                 )
async def get_by_root_folder(root_folder: str):
    content = await files_get_by_root_folder(root_folder)
    return content


@router_files.get(path="/{area}",
                  status_code=200,
                  name='Получить список Файлов по Площади',
                  tags=['Файлы'],
                  description='Получает список Файлов по конкретной Площади'
                  )
async def get_by_area(area: str):
    content = await files_get_by_area(area)
    return content







    #     return {
    #         "status": "success",
    #         "data": [dict(result) for result in results],
    #         "details": None
    #     }
    # {
    #         "status": "error",
    #         "data": None,
    #         "details": str(e.__str__())
    #     })

