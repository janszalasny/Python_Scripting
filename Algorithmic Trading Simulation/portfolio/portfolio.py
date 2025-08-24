# portfolio/portfolio.py
#
# Manages the portfolio's state, including cash, holdings, and total value.
# Acts as an Observer to be notified of market data changes.

import pandas as pd
from collections import defaultdict


class Portfolio:
    """
    Represents a trading portfolio. Manages cash, positions, and calculates value.
    This class acts as an Observer in the Observer pattern, where it observes
    market data changes to update its value.
    """
    
    def __init__(self, initial_capital: float = 100000.0):
        self.initial_capital = float(initial_capital)
        self.cash = float(initial_capital)
        self.holdings = defaultdict(float)  # {symbol: quantity}
        self.positions_history = []  # To track historical positions
        self.portfolio_value_history = []  # To track historical portfolio value
    
    def update_portfolio_value(self, timestamp, market_data):
        """
        Updates the total value of the portfolio at a given timestamp.
        This method is called by the Subject (Backtester) when new data arrives.

        Args:
            timestamp: The current timestamp of the market data.
            market_data (dict): A dictionary with current prices {symbol: price}.
        """
        total_holdings_value = 0.0
        for symbol, quantity in self.holdings.items():
            price = market_data.get(symbol, 0)
            total_holdings_value += quantity * price
        
        current_total_value = self.cash + total_holdings_value
        self.portfolio_value_history.append({'date': timestamp, 'total_value': current_total_value})
        
        # Also record current positions
        self.positions_history.append({'date': timestamp, 'holdings': self.holdings.copy(), 'cash': self.cash})
    
    def execute_trade(self, timestamp, symbol: str, quantity: float, price: float, side: str):
        """
        Executes a trade and updates the portfolio.

        Args:
            timestamp: The timestamp of the trade.
            symbol (str): The symbol being traded.
            quantity (float): The number of shares.
            price (float): The execution price per share.
            side (str): 'BUY' or 'SELL'.
        """
        trade_cost = quantity * price
        
        if side.upper() == 'BUY':
            if self.cash < trade_cost:
                print(f"Warning: Not enough cash to execute BUY order for {quantity} {symbol} at {price}.")
                return
            self.cash -= trade_cost
            self.holdings[symbol] += quantity
            print(f"{timestamp.date()}: BOUGHT {quantity:.2f} {symbol} at ${price:.2f}")
        
        elif side.upper() == 'SELL':
            if self.holdings.get(symbol, 0) < quantity:
                print(f"Warning: Not enough holdings to execute SELL order for {quantity} {symbol}.")
                return
            self.cash += trade_cost
            self.holdings[symbol] -= quantity
            print(f"{timestamp.date()}: SOLD {quantity:.2f} {symbol} at ${price:.2f}")
        else:
            print(f"Warning: Invalid trade side '{side}'.")
    
    def get_portfolio_value_df(self) -> pd.DataFrame:
        """ Returns the portfolio value history as a DataFrame. """
        df = pd.DataFrame(self.portfolio_value_history)
        if not df.empty:
            df.set_index('date', inplace=True)
        return df
