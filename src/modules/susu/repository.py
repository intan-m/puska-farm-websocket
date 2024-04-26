from typing import Dict, List, Tuple
from websockets import broadcast
from websockets.server import WebSocketServerProtocol

from src.modules.susu.entity import SusuMasterData

from src.helper.api import APIHelper


class SusuDWHRepository:
    __api: APIHelper
    __url: str

    def __init__(self, api: APIHelper, url: str):
        self.__api = api
        self.__url = url

    def get_init_data(self) -> SusuMasterData:
        """
        Get Init Data
        """
        init_data = self.__api.request(
            self.__url,
            Model = SusuMasterData
        )
        return init_data


class SusuBIRepository:
    __ws_list: Dict[str, WebSocketServerProtocol]

    def __init__(self):
        self.__ws_list = {}
    

    def add_ws(self, ws: WebSocketServerProtocol, ws_id: str) -> None:
        """
        Adding new WebSocket Client to Pool
        """
        self.__ws_list[ws_id] = ws
    

    def get_ws_pool(self) -> List[WebSocketServerProtocol]:
        """
        Get List of WebSockets from Pool
        """
        return list(self.__ws_list.values())

    
    async def send(self, ws_id: str, message: str):
        """
        Send message to Specific WebSocket (by ID)
        """
        ws = self.__ws_list[ws_id]
        await ws.send(message)


class SusuETLRepository:
    def __init__(self):
        pass


    def broadcast(self, ws_list: List[WebSocketServerProtocol], message: str):
        """
        Broadcast message to List (pool) of WebSocket using Assigned WebSocket.
        """
        broadcast(set(ws_list), message)
    

    def validate(self, data: dict) -> Tuple[SusuMasterData, bool]:
        """
        Validate data and return modelled data.
        """
        pass