import argparse
import asyncio
import websockets
from wsProxy.networks import NETWORKS


class WebSocketServer:
    def __init__(self, network, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.network = network
        self.loop = None
        self.chainId = NETWORKS[network]["chainId"]
        self.connections = set()

    async def handler(self, websocket, path):
        self.connections.add(websocket)
        try:
            async for message in websocket:
                sender_address = websocket.remote_address
                print(f"Receive Message from {sender_address}: {message}")
                for connection in self.connections:
                    if connection != websocket:
                        receiver_address = connection.remote_address
                        print(f"Forwarding message from {sender_address} to {receiver_address}: {message}")                        
                        await connection.send(message)
                        print(f"Message forwarded from {sender_address} to {receiver_address}: {message}")
        finally:
            self.connections.remove(websocket)

    async def start_server(self):
        self.server = await websockets.serve(self.handler, self.host, self.port)
        print(f"WebSocket server started on ws://{self.host}:{self.port}")
        await self.server.wait_closed()

    def start(self):
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.start_server())
        except Exception as e:
            print(f"WebSocket server failed to start: {e}")

    def is_running(self):
        return self.loop is not None and self.loop.is_running()

    def stop(self):
        if self.loop:
            for task in asyncio.all_tasks(self.loop):
                task.cancel()
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            self.loop.stop()
            print(f"WebSocket server stopped on ws://{self.host}:{self.port}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a WebSocket server.")
    parser.add_argument("network", type=str, help="The network to connect to.")
    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="The host of the WebSocket server.",
    )
    parser.add_argument(
        "--port", type=int, default=8765, help="The port of the WebSocket server."
    )

    args = parser.parse_args()

    server = WebSocketServer(network=args.network, host=args.host, port=args.port)
    try:
        server.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop()
