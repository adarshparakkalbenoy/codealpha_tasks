def main():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 310,
        "GOOGL": 135,
        "AMZN": 120,
    }

    print("Stock Portfolio Tracker")
    print("Available stock prices:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price}")

    portfolio = {}
    while True:
        symbol = input("Enter stock symbol 'e.g., AAPL' (or press Enter to finish): ").strip().upper()
        if not symbol:
            break

        if symbol not in stock_prices:
            print(f"Unknown symbol '{symbol}'. Please use one of: {', '.join(stock_prices.keys())}")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid positive integer for quantity.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total_value = 0
    print("\nPortfolio Summary:")
    for symbol, quantity in portfolio.items():
        value = stock_prices[symbol] * quantity
        total_value += value
        print(f"  {symbol}: {quantity} shares x ${stock_prices[symbol]} = ${value}")

    print(f"Total investment value: ${total_value}")

    save_choice = input("Save portfolio summary to .txt and .csv files? (y/n): ").strip().lower()
    if save_choice == "y":
        save_summary(portfolio, stock_prices, total_value)
        print("Saved portfolio summary to 'portfolio_summary.txt' and 'portfolio_summary.csv'.")
    else:
        print("Summary not saved.")


def save_summary(portfolio, stock_prices, total_value):
    txt_path = "portfolio_summary.txt"
    csv_path = "portfolio_summary.csv"

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("Stock Portfolio Summary\n")
        txt_file.write("========================\n")
        for symbol, quantity in portfolio.items():
            value = stock_prices[symbol] * quantity
            txt_file.write(f"{symbol}: {quantity} shares x ${stock_prices[symbol]} = ${value}\n")
        txt_file.write(f"\nTotal investment value: ${total_value}\n")

    with open(csv_path, "w", encoding="utf-8") as csv_file:
        csv_file.write("Stock,Quantity,Price,Value\n")
        for symbol, quantity in portfolio.items():
            value = stock_prices[symbol] * quantity
            csv_file.write(f"{symbol},{quantity},{stock_prices[symbol]},{value}\n")
        csv_file.write(f"TOTAL,,,{total_value}\n")


if __name__ == "__main__":
    main()
