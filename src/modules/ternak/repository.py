import requests
from typing import Dict, List, Optional, Tuple
from websockets import broadcast
from websockets.server import WebSocketServerProtocol

from src.modules.ternak.entity import TernakMasterData


class TernakDWHRepository:
    __url: str

    def __init__(self, hostname: str, route: str, port: Optional[int] = None, protocol: str = "http"):
        self.__url = f"{protocol}://{hostname}:{port}/{route}" if (port) else f"{protocol}://{hostname}/{route}"

    def get_init_data(self) -> TernakMasterData:
        """
        Get Init Data
        """
        req = requests.get(self.__url)
        req.raise_for_status()

        init_data = TernakMasterData.model_validate(req.json())
        return init_data


class TernakBIRepository:
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


class TernakETLRepository:
    def __init__(self):
        pass


    def broadcast(self, ws_list: List[WebSocketServerProtocol], message: str):
        """
        Broadcast message to List (pool) of WebSocket using Assigned WebSocket.
        """
        broadcast(set(ws_list), message)
    

    def validate(self, data: dict) -> Tuple[TernakMasterData, bool]:
        """
        Validate data and return modelled data.
        """
        pass