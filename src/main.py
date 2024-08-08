import os
import json
import logging
from typing import Optional

import ssl
import asyncio
import websockets
from kink import di
from functools import partial
from websockets import WebSocketServerProtocol

from src.modules.susu.handler import SusuHandler
from src.modules.ternak.handler import TernakHandler

from src.helper.config import CONFIG


async def handler(
    ws: WebSocketServerProtocol,
    susu_handler: SusuHandler,
    ternak_handler: TernakHandler,
):
    """
    Handle a connection and dispatch it according to who is connecting.
    """
    message = await ws.recv()
    event: dict = json.loads(message)
    assert "type" in event
    assert isinstance(event["type"], str)

    ev_type: str = event["type"]
    if (ev_type.split("-")[0] == "bi"):
        BI_HANDLER = {
            "bi-susu": susu_handler.bi_handler,
            "bi-ternak": ternak_handler.bi_handler,
        }
        if ev_type in BI_HANDLER:
            await BI_HANDLER[ev_type](ws)
    
    elif (ev_type.split("-")[0] == "etl"):
        ETL_HANDLER = {
            "etl-susu": susu_handler.etl_handler,
            "etl-ternak": ternak_handler.etl_handler,
        }
        if ev_type in ETL_HANDLER:
            await ETL_HANDLER[ev_type](ws)


async def main(ssl_context: Optional[ssl.SSLContext]):
    # Init Handler
    susu_handler = di[SusuHandler]
    ternak_handler = di[TernakHandler]

    inj_handler = partial(
        handler,
        susu_handler = susu_handler,
        ternak_handler = ternak_handler,
    )

    if ssl_context:
        async with websockets.serve(inj_handler, "*", 5000, ssl=ssl_context):
            await asyncio.Future() # Run Forever
    else:
        async with websockets.serve(inj_handler, "*", 5000):
            await asyncio.Future() # Run Forever


if __name__ == "__main__":
    logging.basicConfig(
        level = logging.INFO,
        format = "[%(asctime)s] %(levelname)s - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
    )

    if CONFIG.CERT_DIR:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(
            certfile = os.path.join(CONFIG.CERT_DIR, "fullchain.pem"),
            keyfile = os.path.join(CONFIG.CERT_DIR, "privkey.pem"),
        )
    else:
        ssl_context = None

    asyncio.run(main(ssl_context))
