from aiohttp import web
from aiohttp_validate import validate
from graph import transform_cfd_data, stacked_area_chart
from .requests import generation as request_generation
from .responses import generation as response_generation

@validate(
    request_schema = request_generation.get_generation_request(),
    response_schema = None
)
async def index(request, *args):
    (x, y, labels) = transform_cfd_data.transform(request)
    stacked_area_chart.save(x, y, labels)

    return web.json_response(response_generation.get_generation_response())