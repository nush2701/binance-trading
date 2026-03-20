def validate_symbol(symbol: str) -> bool:
    """Basic validation for trading symbol format (e.g., BTCUSDT)."""
    if not symbol or not isinstance(symbol, str):
        return False
    return symbol.isalnum()

def validate_quantity(quantity: float) -> bool:
    """Ensure order quantity is a positive number."""
    return isinstance(quantity, (int, float)) and quantity > 0

def validate_price(price: float) -> bool:
    """Ensure order price is a positive number."""
    return isinstance(price, (int, float)) and price > 0

def validate_side(side: str) -> bool:
    """Ensure the order side is either BUY or SELL."""
    return side in ["BUY", "SELL"]
