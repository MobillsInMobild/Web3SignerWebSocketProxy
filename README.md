# Web3SignerWebSocketProxy

Web3SignerWebSocketProxy is a project that provides a WebSocket proxy for sending Ethereum transactions using a web-based interface. 

## Features

- **Any Wallet**: Implementations can construct transactions via scripts, but initiate transactions via any metamask/rabby-compatible wallet (Safe, Argus, hardware wallets, etc.).

- **No private key import**: Sending transactions without importing the private key in web3.py avoids the possibility of some accidental private key leakage.

- **Foundy Support**: This proxy can be used in foundy `--rpc-url` to be able to deploy contracts by signing them with a browser wallet (the native forge command arguments only support Trezor, ledger, and now more Remote wallets).

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js
- MetaMask or any other wallet extension that implements the Ethereum JSON-RPC Specification installed in your browser

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MobillsInMobild/Web3SignerWebSocketProxy
    cd Web3SignerWebSocketProxy
    ```

2. Install Python wsProxy Module:
    ```sh
    cd src
    pip install wsProxy/
    ```

### Running the Demo

#### web3_demo

1. Open `proxy.html` in your browser by [Live Server (Five Server)](https://marketplace.visualstudio.com/items?itemName=yandeu.five-server) to access the web interface.To handle possible CORS issues, you may need to install the [Cross Domain CORS Extension](https://chromewebstore.google.com/detail/mjhpgnbimicffchbodmgfnemoghjakai) on your browser.

2. Start `web3_demo.py`:
    ```sh
    cd demo
    python web3_demo.py
    ```

3. Sign transactions on your browser and check your signed transactions on the blockchain browser.

#### forge_demo

1. Open `proxy.html` in your browser in the same way. 

2. Run wsServer:
    ```sh
    python -m wsProxy.wsServer [network]
    ```

3. Use the `forge create` command to deploy the contract. The contract used here is from the "Creating an NFT with Solmate" demo in the Foundry documentation. Note that the `--rpc-url` configuration is in `foundry.toml`, specifically the WebSocket URL for wsProxy. Both `--unlock` and `--from` are required command arguments.

    ```sh
    forge create NFT --rpc-url=proxy --unlocked --from [wallet_address]  --constructor-args-path constructor-args.txt 
    ```

3. Or use the `forge script` command to deploy the contract. 

    ```sh
    forge script script/NFT.s.sol --rpc-url=proxy --broadcast --sender=[wallet_address]  --unlocked
    ```

5. Sign transactions on your browser and check your signed transactions on the blockchain browser.

### Usage

- Open the web interface in your browser.
- Connect your MetaMask wallet.
- The WebSocket server will handle incoming transaction requests and forward them to the connected clients for signing.

## Project Structure

- `src/`: Contains the main source code.
  - `wsProxy/`: WebSocket proxy module.
  - `proxy.html`: Web interface for demonstrating transaction signing using the WebSocket proxy.
- `demo/`: Contains demonstration code.
  - `web3_demo.py`: Example showing how to use the WebSocket proxy for web3py signing.
  - `forge_demo/`: Example showing how to use the WebSocket proxy for forge signing.
    - `foundry.toml`: Foundry configuration file, including WebSocket URL and other settings.
- `README.md`: Project documentation.

## Potential Bug

**Issue**: There is a potential bug in the system where, if a transaction signature takes too long, Forge may throw an error：

> ERROR alloy_transport_ws: failed to deserialize message err=missing field `params` at line 1 column 15

When this error occurs, Forge attempts to resend the transaction that is waiting to be signed.

**Impact**: Due to the nonce used in the transaction process, these duplicate transactions do not affect the actual transactions on the blockchain. At present, there seems to be no adverse effects.



## Acknowledgements

- [websockets](https://websockets.readthedocs.io/) - WebSocket library for Python
- [ethers.js](https://docs.ethers.io/v5/) - Library for interacting with the Ethereum blockchain
