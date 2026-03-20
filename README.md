# Binance Futures Trading Bot

A minimalistic, clean, and production-ready Python trading bot wrapper for interacting with the Binance Futures API.

By default, the bot runs on the **Binance Futures Testnet**, making it safe for testing your algorithmic strategies without risking real assets.

---

## Features

- **Futures Trading Support**: Allows you to easily place `MARKET` and `LIMIT` orders.
- **Testnet & Production Support**: Runs on Testnet by default to prevent accidental loss of funds. You can toggle production mode via CLI.
- **Input Validation**: Automatically validates your trading pairs, quantity, price, and side (BUY/SELL) before hitting the API.
- **Robust Error Handling**: Provides clear, friendly error messages directly in the CLI instead of ugly stack traces.
- **Comprehensive Logging**: Tracks API requests, responses, order placements, and errors to both the console and a local `bot.log` file.

---

## Prerequisites

- Python 3.8+
- A Binance account (and Binance Futures Testnet account)
- API Keys for Binance/Binance Testnet

---

## Installation

1. **Clone the repository** (or navigate to your working directory):
   ```bash
   cd binance-trading-bot
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: This strictly relies on the official `python-binance` module.*

---

## Configuration

The bot uses environment variables to securely store your API keys. Make sure to create a `.env` file in the root directory (alongside `run.py`) and include your API keys:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

If these are not provided in the `.env` file, the bot will notify you and exit.

---

## Project Structure

```
binance-trading-bot/
├── .env                  # Environment configuration file (API Keys)
├── requirements.txt      # Python dependencies (python-binance, etc.)
├── run.py                # Main entry point for the bot
└── src/
    ├── __init__.py
    ├── cli.py            # CLI argument parsing and execution flow
    ├── client.py         # Binance API wrapper handling authentication and API requests
    ├── logging_config.py # Centralized logging settings (logs to stdout and bot.log)
    ├── orders.py         # Formats and passes target orders to the client wrapper
    └── validators.py     # Simple validation logic for quantity, price, symbol, and side
```

---

## Usage Example

The bot uses a Command-Line Interface (CLI). You can run it via `run.py`.

### Required Arguments
- `--symbol`: Trading pair symbol (e.g., `BTCUSDT`)
- `--side`: Order side (`BUY` or `SELL`)
- `--quantity`: Amount of the asset to trade

### Optional Arguments
- `--type`: Order type (`MARKET` or `LIMIT`). Defaults to `MARKET`.
- `--price`: Requested execution price (Required if `--type LIMIT` is selected).
- `--prod`: Add this flag to run on the primary Binance production environment. 

### Examples

**1. Place a Market BUY Order on Testnet (Default)**
```bash
python run.py --symbol BTCUSDT --side BUY --quantity 0.01
```

**2. Place a Limit SELL Order on Testnet**
```bash
python run.py --symbol ETHUSDT --side SELL --quantity 0.5 --type LIMIT --price 2500.50
```

**3. Place a Market BUY Order on PRODUCTION (Live Funds)**
```bash
python run.py --symbol SOLUSDT --side BUY --quantity 2.0 --prod
```

### Expected Output

Upon running a command, the bot prints an order summary. Once executed successfully, you'll receive a confirmation containing the order's core metrics:

```text
--- Order Summary ---
Symbol:   ETHUSDT
Side:     SELL
Type:     LIMIT
Quantity: 0.5
Price:    2500.50
---------------------

✅ Order Executed Successfully!
Order ID:     123456789
Status:       NEW
Executed Qty: 0.0
Avg Price:    2500.50
```

---

## Logging

To ensure completely transparent operations, the bot logs events utilizing the Python `logging` library. 

- **Console Output**: A concise stream of high-level statuses.
- **File Output (`bot.log`)**: Detailed traces, including raw API request bodies, direct API responses from Binance, explicit execution timestamps, and comprehensive error outputs if a trade fails.
