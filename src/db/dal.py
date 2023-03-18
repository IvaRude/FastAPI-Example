from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

import src.api.schemas as schemas
import src.db.models as models


async def serialize_model_unit_to_schema(unit: models.Unit) -> schemas.Unit:
    return schemas.Unit(id=unit.id,
                        parent_id=unit.parent_id,
                        name=unit.name,
                        price=unit.price
                        )


async def get_units_from_db(session: AsyncSession) -> list[schemas.Unit]:
    results = await session.execute(select(models.Unit))
    return [await serialize_model_unit_to_schema(result['Unit']) for result in results]


async def insert_unit_into_db(unit: schemas.Unit, session: AsyncSession):
    await session.execute(insert(models.Unit).values(dict(unit.dict(), is_deleted=False)))
    await session.commit()


async def get_unit(unit_id: int, session: AsyncSession) -> schemas.Unit:
    unit = (await session.execute(select(models.Unit).filter(models.Unit.id == unit_id))).first()
    return await serialize_model_unit_to_schema(unit['Unit'])
