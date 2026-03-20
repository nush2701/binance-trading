import os
from binance.client import Client
from .logging_config import setup_logger

logger = setup_logger(__name__)

class BinanceFuturesClient:
    """Wrapper around python-binance client tailored for Futures Testnet by default."""
    
    def __init__(self, api_key: str = None, api_secret: str = None, testnet: bool = True):
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            raise ValueError(
                "API credentials missing. Please provide api_key and api_secret "
                "or set BINANCE_API_KEY and BINANCE_API_SECRET environment variables."
            )
        
        self.client = Client(self.api_key, self.api_secret, testnet=testnet)
        logger.info(f"Initialized Binance Client (Testnet: {testnet})")
        
    def get_futures_balance(self):
        """Retrieve the futures account balance."""
        try:
            return self.client.futures_account_balance()
        except Exception as e:
            logger.error(f"Error fetching futures balance: {e}")
            raise
