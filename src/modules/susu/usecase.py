import json
import logging
import secrets
from websockets.server import WebSocketServerProtocol

from src.modules.susu.repository import (
    SusuBIRepository,
    SusuETLRepository,
    SusuDWHRepository,
)


class SusuUsecase:
    __repo_dwh: SusuDWHRepository
    __repo_bi: SusuBIRepository
    __repo_etl: SusuETLRepository

    def __init__(self, repo_dwh: SusuDWHRepository, repo_bi: SusuBIRepository, repo_etl: SusuETLRepository):
        self.__repo_dwh = repo_dwh
        self.__repo_bi = repo_bi
        self.__repo_etl = repo_etl
    

    async def add_bi_ws(self, ws: WebSocketServerProtocol):
        ws_id = secrets.token_urlsafe(12)
        logging.info(f"Adding New WebSocket for bi-susu: {ws_id}")

        self.__repo_bi.add_ws(ws, ws_id)
        await self.__repo_bi.send(ws_id, json.dumps({
            "status": "OK",
            "type": "web",
            "category": "susu",
            "id": ws_id,
        }))

        init_data = self.__repo_dwh.get_init_data()
        if init_data:
            await self.__repo_bi.send(ws_id, init_data.model_dump_json())

        async for message in ws:
            await self.__repo_bi.send(ws_id, message)
    
    
    def broadcast(self):
        ws_list = self.__repo_bi.get_ws_pool()
        new_data = self.__repo_dwh.get_init_data()
        if ws_list and new_data:
            self.__repo_etl.broadcast(ws_list, new_data.model_dump_json())
