import re
import json
import logging
import secrets
from typing import Optional
from websockets.server import WebSocketServerProtocol

from src.modules.ternak.repository import (
    TernakBIRepository,
    TernakETLRepository,
    TernakDWHRepository,
)


class TernakUsecase:
    __repo_dwh: TernakDWHRepository
    __repo_bi: TernakBIRepository
    __repo_etl: TernakETLRepository

    def __init__(self, repo_dwh: TernakDWHRepository, repo_bi: TernakBIRepository, repo_etl: TernakETLRepository):
        self.__repo_dwh = repo_dwh
        self.__repo_bi = repo_bi
        self.__repo_etl = repo_etl
    

    async def add_bi_ws(self, ws: WebSocketServerProtocol, filters: Optional[dict]):
        # Add New WebSocket
        ws_id = secrets.token_urlsafe(12)
        logging.info(f"Adding New WebSocket for bi-ternak: {ws_id}")

        self.__repo_bi.add_ws(ws, ws_id)
        await self.__repo_bi.send(ws_id, json.dumps({
            "status": "OK",
            "id": ws_id,
            "type": "web",
            "category": "ternak",
        }))

        data = self.__repo_dwh.get_data(params=filters)
        if data:
            await self.__repo_bi.send(ws_id, data.model_dump_json())

        # Updating WebSocket Filters
        async for message in ws:
            try:
                cln_message = re.sub(r"(\w+)\s*:", r'"\1"', message.replace("'", '"'))
                logging.info(cln_message)
                update: dict = json.loads(cln_message)
                filters = update.pop("filters")
                
                logging.info(f"Updating WebSocket '{ws_id}' filters: {filters}")
                self.__repo_bi.add_ws(ws, ws_id, filters)
                data = self.__repo_dwh.get_data(params=filters)
                if data:
                    await self.__repo_bi.send(ws_id, data.model_dump_json())

            except json.JSONDecodeError:
                logging.error(f"Error while Parsing JSON from '{ws_id}': {str(message)}")
            except KeyError as e:
                logging.error(f"{str(e)} not found in JSON from '{ws_id}'")
    
    
    def broadcast(self):
        ws_list = self.__repo_bi.get_ws_pool()
        for ws, filters in ws_list:
            new_data = self.__repo_dwh.get_data(filters)
            if new_data:
                self.__repo_etl.send(ws, new_data.model_dump_json())
