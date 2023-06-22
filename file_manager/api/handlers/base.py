from aiohttp.web_urldispatcher import View
from asyncpgsa import PG
from aiohttp.web_exceptions import HTTPNotFound
from sqlalchemy import select, exists


class BaseView(View):
    URL_PATH: str

    @property
    def pg(self) -> PG:
        return self.request.app['pg']

    # TODO check that id exists in db
    def check_id_exists(self):
        query = select([])
