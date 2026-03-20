import os
from typing import Optional
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
            logger.info("API Request: fetching futures account balance")
            response = self.client.futures_account_balance()
            logger.info("API Response: fetched balance successfully")
            return response
        except Exception as e:
            logger.error(f"API Error fetching futures balance: {e}")
            raise

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: Optional[float] = None):
        """Place an order and log the request/response."""
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            if order_type == 'LIMIT' and price is not None:
                params['timeInForce'] = 'GTC'
                params['price'] = price
                
            logger.info(f"API Request (futures_create_order) | Params: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"API Response: Order ID {response.get('orderId')} | Status {response.get('status')}")
            return response
        except Exception as e:
            logger.error(f"API Error placing order: {e}")
            raise
