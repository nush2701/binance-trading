from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT
from .client import BinanceFuturesClient
from .validators import validate_symbol, validate_quantity, validate_price, validate_side
from .logging_config import setup_logger

logger = setup_logger(__name__)

class OrderManager:
    """Handles the placement of market and limit orders."""
    
    def __init__(self, client: BinanceFuturesClient):
        self.client = client
        
    def place_market_order(self, symbol: str, side: str, quantity: float):
        if not validate_symbol(symbol) or not validate_quantity(quantity) or not validate_side(side):
            raise ValueError("Invalid symbol, side, or quantity provided.")
            
        logger.info(f"Placing MARKET {side} order for {quantity} {symbol}")
        try:
            response = self.client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market order successful: Order ID {response.get('orderId')}")
            return response
        except Exception as e:
            logger.error(f"Failed to place market order: {e}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        if not validate_symbol(symbol) or not validate_quantity(quantity) \
                or not validate_price(price) or not validate_side(side):
            raise ValueError("Invalid symbol, side, quantity, or price provided.")
            
        logger.info(f"Placing LIMIT {side} order for {quantity} {symbol} at price {price}")
        try:
            response = self.client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit order successful: Order ID {response.get('orderId')}")
            return response
        except Exception as e:
            logger.error(f"Failed to place limit order: {e}")
            raise
