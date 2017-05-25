# -*- coding: utf-8 -*-
from datetime import datetime
from aiohttp import web
from aiohttp_swagger import setup_swagger


async def ping(request):
    """Pong service status
    """
    return web.json_response(
        {
            'status': 'ok',
            'msg': 'pong',
            'datetime': datetime.utcnow().isoformat()
        }
    )

async def swagger_config(request):
    """Swagger API definition endpoint.
    """
    return web.Response(text=open('swagger_api.yaml', 'r').read(), content_type="application/yaml")



app = web.Application()
app.router.add_route('GET', "/ping", ping)
app.router.add_route('GET', '/config.yaml', swagger_config)

setup_swagger(app, swagger_from_file="swagger_api.yaml")

web.run_app(app, host="127.0.0.1", port=8888)
