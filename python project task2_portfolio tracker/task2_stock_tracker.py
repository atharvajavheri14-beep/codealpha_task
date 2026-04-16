import csv
import os

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 185,
    "META": 490,
    "NFLX": 620,
    "NVDA": 875,
}


def display_available_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11}")
    print("-" * 30)


def get_portfolio():
    portfolio = {}
    print("\nEnter your stock holdings (type 'done' when finished):")

    while True:
        symbol = input("\nStock symbol (or 'done'): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our database. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")

    return portfolio


def calculate_portfolio(portfolio):
    results = []
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        results.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })

    return results, total_value


def display_portfolio(results, total_value):
    print("\n" + "=" * 55)
    print("PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Symbol':<10} {'Qty':>6} {'Price':>12} {'Total Value':>14}")
    print("-" * 55)

    for row in results:
        print(f"{row['symbol']:<10} {row['quantity']:>6} ${row['price']:>11} ${row['value']:>13,}")

    print("-" * 55)
    print(f"{'TOTAL PORTFOLIO VALUE':>42} ${total_value:>13,}")
    print("=" * 55)


def save_to_csv(results, total_value, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "quantity", "price", "value"])
        writer.writeheader()
        writer.writerows(results)
        writer.writerow({"symbol": "TOTAL", "quantity": "", "price": "", "value": total_value})

    print(f"\nPortfolio saved to '{filename}'")


def stock_tracker():
    print("=" * 40)
    print("  STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    display_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    results, total_value = calculate_portfolio(portfolio)
    display_portfolio(results, total_value)

    save_choice = input("\nSave portfolio to CSV? (yes/no): ").lower().strip()
    if save_choice in ("yes", "y"):
        save_to_csv(results, total_value)


if __name__ == "__main__":
    stock_tracker()
