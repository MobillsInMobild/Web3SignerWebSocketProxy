import asyncio
import websockets


class WebSocketServer:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.loop = None
        self.connections = set()

    async def handler(self, websocket, path):
        self.connections.add(websocket)
        try :
            async for message in websocket:
                for connection in self.connections:
                    if connection != websocket:
                        print(f"Forwarding message: {message}")
                        await connection.send(message)
        finally:
            self.connections.remove(websocket)

    def start(self):
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            start_server = websockets.serve(self.handler, self.host, self.port)
            self.loop.run_until_complete(start_server)
            print(f"WebSocket server started on ws://{self.host}:{self.port}")
            self.loop.run_forever()
        except Exception as e:
            print(f"WebSocket server failed to start: {e}")

    def is_running(self):
        return self.loop is not None and self.loop.is_running()

    def stop(self):
        if self.loop:
            self.loop.stop()
            print(f"WebSocket server stopped on ws://{self.host}:{self.port}")
