from typing import Optional
from websockets.server import WebSocketServerProtocol

from src.modules.ternak.usecase import TernakUsecase


class TernakHandler:
    __usecase: TernakUsecase

    def __init__(self, usecase: TernakUsecase):
        self.__usecase = usecase

    
    async def bi_handler(self, ws: WebSocketServerProtocol):
        """
        Adding BI Handler to WebSocket Pool
        """
        await self.__usecase.add_bi_ws(ws)
    

    async def etl_handler(self, ws: WebSocketServerProtocol):
        """
        Adding ETL Handler to WebSocket Producer
        """
        self.__usecase.broadcast()
        await ws.close()