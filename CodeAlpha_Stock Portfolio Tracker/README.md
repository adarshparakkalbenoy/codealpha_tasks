# Stock Portfolio Tracker

## Project Overview

The **Stock Portfolio Tracker** is a Python-based application designed to help users manage and calculate their stock portfolio investments. Users can input stock symbols and quantities, and the application automatically calculates the total investment value based on predefined stock prices. The results can be saved in both text (.txt) and CSV (.csv) formats for record-keeping and analysis.



---

## Features

✅ **Interactive Stock Input** — Users can enter multiple stock symbols and quantities through a command-line interface.

✅ **Predefined Stock Prices** — Includes a hardcoded dictionary with stock prices for major companies (AAPL, TSLA, MSFT, GOOGL, AMZN).

✅ **Portfolio Calculation** — Automatically calculates total investment value by multiplying quantity × price for each stock.

✅ **Summary Display** — Shows a detailed breakdown of holdings with individual values and total investment.

✅ **Dual Format Export** — Saves portfolio summary to both `.txt` and `.csv` files for flexibility.

✅ **Error Handling** — Validates user input and handles edge cases (invalid symbols, non-integer quantities, empty portfolios).

---

## Project Structure

```
codealphatask2/
├── stock_portfolio_tracker.py      # Main Python script
├── portfolio_summary.txt           # Sample text output
├── portfolio_summary.csv           # Sample CSV output
└── README.md                       # Project documentation
```

### File Descriptions

#### 1. **stock_portfolio_tracker.py**
The core application file containing the portfolio tracking logic.

**Key Functions:**
- `main()` — Entry point of the program; manages the interactive user workflow including stock input, validation, and calculation.
- `save_summary()` — Handles file output by writing portfolio data to both `.txt` and `.csv` formats.

**Workflow:**
1. Displays available stock symbols and prices
2. Prompts user to enter stock symbols and quantities
3. Validates input (checks for valid symbols and positive quantities)
4. Calculates total investment value
5. Displays portfolio summary
6. Optionally saves results to output files

**Stock Database:**
```python
{
    "AAPL": 180,    # Apple Inc.
    "TSLA": 250,    # Tesla Inc.
    "MSFT": 310,    # Microsoft Corporation
    "GOOGL": 135,   # Alphabet Inc. (Google)
    "AMZN": 120,    # Amazon.com Inc.
}
```

#### 2. **portfolio_summary.txt**
A human-readable text file containing sample portfolio output.

**Format:**
- Header with title and separator
- Line-by-line breakdown of each stock holding (symbol, quantity, price per share, total value)
- Summary line with total investment value

**Example:**
```
Stock Portfolio Summary
========================
AAPL: 5 shares x $180 = $900
TSLA: 2 shares x $250 = $500
...
Total investment value: $3055
```

#### 3. **portfolio_summary.csv**
A comma-separated values file suitable for spreadsheet applications like Excel.

**Format:**
- Header row: `Stock, Quantity, Price, Value`
- Data rows: One row per stock holding
- Final row: `TOTAL` with cumulative value

**Example:**
```csv
Stock,Quantity,Price,Value
AAPL,5,180,900
TSLA,2,250,500
...
TOTAL,,,3055
```

---

## How to Use

### Prerequisites
- Python 3.6 or higher installed on your system

### Running the Application

1. **Open Terminal/Command Prompt** and navigate to the project directory:
   ```bash
   cd "c:\Users\Adarsh\OneDrive\Attachments\codeyy\CodeAlpha Tasks\codealphatask2"
   ```

2. **Run the script:**
   ```bash
   python stock_portfolio_tracker.py
   ```

3. **Follow the prompts:**
   - The program displays available stocks and their prices
   - Enter a stock symbol (e.g., `AAPL`, `TSLA`) when prompted
   - Enter the quantity of shares for that stock
   - Press Enter without entering a symbol to finish adding stocks
   - Choose whether to save the portfolio to files

### Example Session
```
Stock Portfolio Tracker
Available stock prices:
  AAPL: $180
  TSLA: $250
  MSFT: $310
  GOOGL: $135
  AMZN: $120

Enter stock symbol (or press Enter to finish): AAPL
Enter quantity of AAPL: 5
Enter stock symbol (or press Enter to finish): TSLA
Enter quantity of TSLA: 2
Enter stock symbol (or press Enter to finish): 

Portfolio Summary:
  AAPL: 5 shares x $180 = $900
  TSLA: 2 shares x $250 = $500
Total investment value: $1400

Save portfolio summary to .txt and .csv files? (y/n): y
Saved portfolio summary to 'portfolio_summary.txt' and 'portfolio_summary.csv'.
```

---

## Key Concepts Demonstrated

| Concept | Implementation |
|---------|-----------------|
| **Dictionary** | Stock prices stored as key-value pairs |
| **User Input/Output** | `input()` for user interaction, `print()` for display |
| **Basic Arithmetic** | Multiplication for calculating stock values, addition for totals |
| **File Handling** | Reading/writing to `.txt` and `.csv` files |
| **String Formatting** | F-strings for formatted output |
| **Control Flow** | While loops, if-else statements, input validation |
| **Error Handling** | Try-except blocks for handling invalid inputs |

---

## Input Validation

The application includes robust input validation:

✓ **Stock Symbol Validation** — Only accepts symbols in the predefined dictionary (AAPL, TSLA, MSFT, GOOGL, AMZN).

✓ **Quantity Validation** — Requires positive integer values; rejects zero, negative numbers, and non-integer inputs.

✓ **Empty Portfolio Handling** — Gracefully exits if no stocks are entered.

---

## Output Files

When the user chooses to save the portfolio:

- **portfolio_summary.txt** — Created in the same directory, formatted for easy reading
- **portfolio_summary.csv** — Created in the same directory, formatted for import into spreadsheet applications

Both files can be opened and edited with any text editor or spreadsheet software.

---

## Potential Enhancements

Future improvements could include:

- 📈 **Dynamic Stock Prices** — Fetch real-time prices from an API
- 💾 **Database Integration** — Store portfolios in a database for persistence
- 📊 **Visualization** — Generate charts showing portfolio distribution
- 🌐 **Web Interface** — Build a web-based GUI for better usability
- 📱 **Mobile Support** — Create a mobile app version
- 🔔 **Price Alerts** — Notify users of significant price changes
- 📑 **Portfolio History** — Track portfolio changes over time

---

## Requirements

- **Python Version:** 3.6+
- **External Libraries:** None (uses only Python standard library)
- **Disk Space:** Minimal (~50 KB)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Command not found: python" | Ensure Python is installed and added to PATH |
| Invalid symbol error | Use only supported symbols: AAPL, TSLA, MSFT, GOOGL, AMZN |
| Quantity error | Enter a positive whole number without decimals |
| Files not created | Ensure write permissions in the project directory |

---




## Quick Reference

| Task | Command |
|------|---------|
| Run the program | `python stock_portfolio_tracker.py` |
| View text output | Open `portfolio_summary.txt` in any text editor |
| View CSV output | Open `portfolio_summary.csv` in Excel or spreadsheet app |
| Edit stock prices | Modify the `stock_prices` dictionary in the Python file |

---
