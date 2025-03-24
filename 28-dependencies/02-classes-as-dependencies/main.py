from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


# class CommonQueryParams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit


@dataclass
class CommonQueryParams:
    q: str | None = None
    skip: int = 0
    limit: int = 100


@app.get("/items/")
# async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):  # Short
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
