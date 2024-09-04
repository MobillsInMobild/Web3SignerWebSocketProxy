# Web3SignerWebSocketProxy

Web3SignerWebSocketProxy is a project that provides a WebSocket proxy for sending Ethereum transactions using a web-based interface. 

## Features

- **Any Wallet**: Implementations can construct transactions via scripts, but initiate transactions via any metamask/rabby-compatible wallet (Safe, Argus, hardware wallets, etc.).

- **No private key import**: Sending transactions without importing the private key in web3.py avoids the possibility of some accidental private key leakage.


## Getting Started

### Prerequisites

- Python 3.7+
- Node.js
- MetaMask or any other wallet extension that implements the Ethereum JSON-RPC Specification installed in your browser

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Web3SignerWebSocketProxy.git
    cd Web3SignerWebSocketProxy
    ```

2. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Demo

1. Open `proxy.html` in your browser to access the web interface.To handle possible CORS issues, you may need to install the [Cross Domain CORS Extension](https://chromewebstore.google.com/detail/mjhpgnbimicffchbodmgfnemoghjakai) on your browser.

1. Start the WebSocket server:
    ```sh
    python demo.py
    ```

### Usage

- Open the web interface in your browser.
- Connect your MetaMask wallet.
- The WebSocket server will handle incoming transaction requests and forward them to the connected clients for signing.

## Project Structure

- `wsServer.py`: WebSocket server implementation.
- `wsClient.py`: WebSocket client implementation.
- `proxy.html`: Web interface for interacting with the WebSocket server.
- `demo.py`: Example script demonstrating how to use the WebSocket server and client.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [websockets](https://websockets.readthedocs.io/) - WebSocket library for Python
- [ethers.js](https://docs.ethers.io/v5/) - Library for interacting with the Ethereum blockchain
