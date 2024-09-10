NETWORKS = {
    "eth": {
        "chainName": "Ethereum Mainnet",
        "chainId": 1,
        "nativeCurrency": {"name": "Ethereum", "symbol": "ETH", "decimals": 18},
        "rpcUrls": ["https://mainnet.infura.io/v3"],
        "blockExplorerUrls": ["https://etherscan.io"],
    },
    "arb": {
        "chainName": "Arbitrum One",
        "chainId": 42161,
        "nativeCurrency": {"symbol": "ETH", "decimals": 18},
        "rpcUrls": ["https://arb1.arbitrum.io/rpc"],
        "blockExplorerUrls": ["https://arbiscan.io"],
    },
    "sepolia": {
        "chainName": "Ethereum Sepolia",
        "chainId": 11155111,
        "nativeCurrency": {"symbol": "ETH", "decimals": 18},
        "rpcUrls": ["https://rpc.sepolia.org"],
        "blockExplorerUrls": ["https://sepolia.etherscan.io/"],
    },
    "bsc": {
        "chainName": "BNB Smart Chain",
        "chainId": 56,
        "nativeCurrency": {"symbol": "BNB", "decimals": 18},
        "rpcUrls": ["https://binance.llamarpc.com"],
        "blockExplorerUrls": ["https://bscscan.com"],
    },
    "base": {
        "chainName": "Base",
        "chainId": 8453,
        "nativeCurrency": {"symbol": "ETH", "decimals": 18},
        "rpcUrls": ["https://mainnet.base.org"],
        "blockExplorerUrls": ["https://basescan.org"],
    },
    "mantle": {
        "chainName": "Mantle",
        "chainId": 5000,
        "nativeCurrency": {"symbol": "MNT", "decimals": 18},
        "rpcUrls": ["https://rpc.ankr.com/mantle"],
        "blockExplorerUrls": ["https://explorer.mantle.xyz"],
    },
}
