import asyncio
import websockets
import json


class WebSocketClient:
    def __init__(self, url):
        self.url = url
    
    async def sendTx(self, tx):
        async with websockets.connect(self.url) as websocket:
            await websocket.send(json.dumps(tx))
            response = await websocket.recv()
            return json.loads(response)
        