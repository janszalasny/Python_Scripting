# strategy/strategies.py
#
# Implements the Strategy design pattern for trading algorithms.
# Defines a base Strategy class and concrete strategy implementations.

import pandas as pd
import numpy as np


class Strategy:
    """
    Abstract base class for a trading strategy.
    """
    
    def __init__(self, symbol: str):
        self.symbol = symbol
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generates trading signals based on historical data.

        Args:
            data (pd.DataFrame): DataFrame with price data.

        Returns:
            pd.DataFrame: DataFrame with a 'signal' column.
        """
        raise NotImplementedError("Should implement generate_signals()")


class MovingAverageCrossoverStrategy(Strategy):
    """
    A concrete strategy based on the moving average crossover.
    - A 'BUY' signal is generated when the short-term moving average crosses
      above the long-term moving average.
    - A 'SELL' signal is generated when the short-term moving average crosses
      below the long-term moving average.
    """
    
    def __init__(self, symbol: str, short_window: int = 40, long_window: int = 100):
        super().__init__(symbol)
        if short_window >= long_window:
            raise ValueError("Short window must be smaller than long window.")
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generates trading signals for the moving average crossover strategy.

        Args:
            data (pd.DataFrame): The input market data.

        Returns:
            pd.DataFrame: The data with calculated signals.
        """
        print("Generating signals for Moving Average Crossover strategy...")
        signals = pd.DataFrame(index=data.index)
        signals['price'] = data['price']
        signals['signal'] = 0.0  # Start with no signal
        
        # Calculate short and long moving averages
        signals['short_mavg'] = data['price'].rolling(window=self.short_window, min_periods=1).mean()
        signals['long_mavg'] = data['price'].rolling(window=self.long_window, min_periods=1).mean()
        
        # Generate signal when short MA crosses long MA
        # np.where(condition, value_if_true, value_if_false)
        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0
        )
        
        # Take the difference of the signals column to generate actual trading orders
        signals['positions'] = signals['signal'].diff()
        
        print("Signals generated.")
        return signals
