import argparse
import sys
from dotenv import load_dotenv

from .client import BinanceFuturesClient
from .orders import OrderManager
from .logging_config import setup_logger

logger = setup_logger("cli")

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    
    # Required arguments
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--quantity", type=float, required=True, help="Amount of the asset to trade")
    
    # Optional arguments
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT'], default='MARKET', help="Order type (MARKET or LIMIT)")
    parser.add_argument("--price", type=float, help="Requested price (Required if type is LIMIT)")
    parser.add_argument("--prod", action="store_true", help="Run on production environment (default is testnet)")

    args = parser.parse_args()

    if args.type == 'LIMIT' and args.price is None:
        parser.error("--price is required when order type is LIMIT")

    # Load environment variables (e.g., API keys) from a .env file if it exists
    load_dotenv()

    try:
        # Initializing client and order manager
        testnet = not args.prod
        client = BinanceFuturesClient(testnet=testnet)
        order_manager = OrderManager(client)
        
        if args.type == 'MARKET':
            order_manager.place_market_order(args.symbol, args.side, args.quantity)
        elif args.type == 'LIMIT':
            order_manager.place_limit_order(args.symbol, args.side, args.quantity, args.price)
            
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
