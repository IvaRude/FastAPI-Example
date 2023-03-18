import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

import src.api.schemas as schemas
import src.db.dal as dal
from src.db.base import get_session

app = FastAPI()


@app.get('/units', response_model=list[schemas.Unit])
async def get_units(session: AsyncSession = Depends(get_session)):
    return await dal.get_units_from_db(session)


@app.get('/units/{unit_id}', response_model=schemas.Unit)
async def get_unit(unit_id: int, session: AsyncSession = Depends(get_session)):
    return await dal.get_unit(unit_id, session)


@app.post('/unit')
async def post_unit(unit: schemas.Unit, session: AsyncSession = Depends(get_session)):
    await dal.insert_unit_into_db(unit, session)


# @app.exception_handler(schemas.ValidationError)
# async def validation_error(request: Request, exc: schemas.ValidationError | RequestValidationError):
#     return JSONResponse(
#         status_code=400,
#         content={'code': 400,
#                  'message': 'Validation Failed'}
#     )
#
#
# @app.exception_handler(RequestValidationError)
# async def request_validation_error(request: Request, exc: RequestValidationError):
#     return await validation_error(request, exc)
#
#
# @app.exception_handler(schemas.ItemNotFoundError)
# async def item_not_found(request: Request, exc: schemas.ItemNotFoundError):
#     return JSONResponse(
#         status_code=404,
#         content={'code': 404,
#                  'message': 'Item not found'}
#     )
#
#
# @app.post('/imports')
# async def imports(shop_unit_import_request: schemas.ShopUnitImportRequest, session: AsyncSession = Depends(get_session)):
#     update_date = shop_unit_import_request.updateDate
#     items = shop_unit_import_request.items
#     await dal.imports(session, items, update_date)
#
#
# @app.delete('/delete/{id}')
# async def delete(id: uuid.UUID, session: AsyncSession = Depends(get_session)):
#     await dal.delete(session, id)
#
#
# @app.get('/nodes/{id}', response_model=schemas.ShopUnit)
# async def nodes(id: uuid.UUID, session: AsyncSession = Depends(get_session)):
#     return await dal.nodes(session, id)
#
#
# @app.get('/sales', response_model=schemas.ShopUnitStatisticResponse)
# async def sales(date: datetime, session: AsyncSession = Depends(get_session)):
#     return await dal.sales(session, date)
#
#
# @app.get('/node/{id}/statistic', response_model=schemas.ShopUnitStatisticResponse)
# async def node_statistic(id: uuid.UUID, dateStart: datetime = None, dateEnd: datetime = None, session: AsyncSession = Depends(get_session)):
#     return await dal.node_statistic(session, id, dateStart, dateEnd)
#
#
# # @app.post("/cities/")
# # async def add_city(city: CitySchema, session: AsyncSession = Depends(get_session)):
# #     city = service.add_city(session, city.name, city.population)
# #     try:
# #         await session.commit()
# #         return city
# #     except IntegrityError as ex:
# #         await session.rollback()
# #         raise DuplicatedEntryError("The city is already stored")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
