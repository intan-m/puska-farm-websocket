import json
import logging
import secrets
from websockets.server import WebSocketServerProtocol

from src.modules.ref.repository import (
    RefDWHRepository,
    RefBIRepository
)

class RefUsecase:
    __repo_dwh: RefDWHRepository

    def __init__(self, repo_dwh: RefDWHRepository, repo_bi: RefBIRepository):
        self.__repo_dwh = repo_dwh
        self.__repo_bi = repo_bi


    async def add_lokasi_ws(self, ws: WebSocketServerProtocol, filters: dict):
        # Add New WebSocket
        ws_id = secrets.token_urlsafe(12)
        logging.info(f"Adding New WebSocket for ref: {ws_id}.")

        self.__repo_bi.add_ws(ws, ws_id)
        await self.__repo_bi.send(ws_id, json.dumps({
            "status": "OK",
            "id": ws_id,
            "type": "web",
            "category": "ternak",
        }))

        # Send Data
        data = self.__repo_dwh.get_lokasi_data(params=filters)
        await self.__repo_bi.send(ws_id, [d.model_dump_json() for d in data])

        # Waiting New requests
        async for message in ws:
            pass
