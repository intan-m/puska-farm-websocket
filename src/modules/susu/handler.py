import json
from websockets.server import WebSocketServerProtocol

from src.modules.susu.usecase import SusuUsecase


class SusuHandler:
    __usecase: SusuUsecase

    def __init__(self, usecase: SusuUsecase):
        self.__usecase = usecase

    
    async def bi_handler(self, ws: WebSocketServerProtocol):
        """
        Adding BI Handler to WebSocket Pool
        """
        await self.__usecase.add_bi_ws(ws)
    

    async def etl_handler(self, ws: WebSocketServerProtocol, message: str):
        """
        Adding ETL Handler to WebSocket Producer
        """
        self.__usecase.broadcast(json.dumps(message))
        await ws.close()