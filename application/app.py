from litestar import Litestar, get

from .config import Settings, get_settings


@get("/")
async def settings() -> Settings:
    return get_settings()


app = Litestar(route_handlers=[settings], on_startup=(get_settings,))
