from aiohttp import web
from main import create_app

web.run_app(main.create_app(), port=port)
