from aiohttp import web
from graph import stacked_area_chart
from datetime import datetime

async def index(request):
    json_data = await request.json()
    labels = []
    x = []
    y = []
    for key in json_data:
        value = json_data[key]
        labels.append(key)
        sub_y = []
        for data in value:
            new_x = data['x']
            date = datetime.fromtimestamp(new_x)
            date_string = date.strftime("%Y/%m/%d")
            if date_string not in x:
                x.append(date_string)
            
            sub_y.append(data['y'])
        y.append(sub_y)

    stacked_area_chart.save(x, y, labels)
    return web.json_response(json_data)