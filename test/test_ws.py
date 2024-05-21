import sys
import asyncio
import json
import websockets
from typing import Optional


async def main(category: str):
    async with websockets.connect("ws://localhost:9000") as websocket:
        await websocket.send(json.dumps({"type": f"bi-{category}"}))
        while True:
            try:
                response = await websocket.recv()
                print(json.dumps(json.loads(response), indent=2))
            except websockets.ConnectionClosedOK:
                break


_, category = sys.argv
asyncio.run(main(category))