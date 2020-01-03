from aiohttp import web
from graph import stacked_area_chart

async def index(request):
    stacked_area_chart.save()
    return web.json_response({'test': 'test'})