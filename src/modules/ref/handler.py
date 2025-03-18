from websockets.server import WebSocketServerProtocol

from src.modules.ref.usecase import RefUsecase


class RefHandler:
    __usecase: RefUsecase

    def __init__(self, usecase: RefUsecase):
        self.__usecase = usecase


    async def lokasi_handler(self, ws: WebSocketServerProtocol, filters: dict):
        """
        Adding Lokasi Handler to WebSocket Pool
        """
        await self.__usecase.add_lokasi_ws(ws, filters)
