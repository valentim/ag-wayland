from aiohttp import web
from main import create_app
import os

port = os.getenv('PORT')

web.run_app(create_app(), port=port)
