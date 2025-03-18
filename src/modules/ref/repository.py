from typing import Dict, List, Optional, Tuple

import requests
from websockets import broadcast
from websockets.server import WebSocketServerProtocol

from src.modules.ref.entity import Location


class RefDWHRepository:
    __url: str

    def __init__(self, hostname: str, route: str, port: Optional[int] = None, protocol: str = "http"):
        self.__url = f"{protocol}://{hostname}:{port}/{route}" if (port) else f"{protocol}://{hostname}/{route}"


    def get_lokasi_data(self, params: Optional[dict] = None) -> List[Location]:
        """
        Get Init Data
        """
        req = requests.get(self.__url, params=params)
        req.raise_for_status()

        __data = req.json()
        data = [Location.model_validate(d) for d in __data]
        return data


class RefBIRepository:
    __ws_list: Dict[str, Tuple[WebSocketServerProtocol, Optional[dict]]]

    def __init__(self):
        self.__ws_list = {}


    def add_ws(self, ws: WebSocketServerProtocol, ws_id: str) -> None:
        """
        Adding new WebSocket Client to Pool
        """
        self.__ws_list[ws_id] = (ws, {})

    
    async def send(self, ws_id: str, message: str):
        """
        Send message to Specific WebSocket (by ID)
        """
        ws, _ = self.__ws_list[ws_id]
        await ws.send(message)
