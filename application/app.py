from litestar import Litestar

from .config import sql_alchemy_plugin


app = Litestar(plugins=[sql_alchemy_plugin])
