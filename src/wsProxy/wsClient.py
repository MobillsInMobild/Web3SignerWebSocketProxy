import asyncio
import websockets
import json

class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri

    async def send_transaction(self, transaction):
        async with websockets.connect(self.uri) as websocket:
            print(f"Sending: {transaction}")
            await websocket.send(json.dumps(transaction))
            response = await websocket.recv()
            print(f"Response: {response}")
            return response

    def send(self, transaction):
        return asyncio.run(self.send_transaction(transaction))