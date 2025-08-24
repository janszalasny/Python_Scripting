# visualization/visualizer.py
#
# Handles plotting of backtest results using matplotlib.

import matplotlib.pyplot as plt
import pandas as pd

class MatplotlibVisualizer:
    """
    Visualizes trading performance using Matplotlib.
    """
    def plot_performance(self, portfolio_value: pd.DataFrame, signals: pd.DataFrame, symbol: str):
        """
        Plots the portfolio value over time along with trading signals.

        Args:
            portfolio_value (pd.DataFrame): DataFrame of portfolio value history.
            signals (pd.DataFrame): DataFrame containing price data and signals.
            symbol (str): The ticker symbol being traded.
        """
        if portfolio_value.empty or signals.empty:
            print("Cannot plot performance due to empty data.")
            return

        fig, ax1 = plt.subplots(figsize=(14, 8))
        fig.suptitle(f'Trading Strategy Performance for {symbol}', fontsize=16)

        # Plot 1: Portfolio Value (left y-axis)
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Portfolio Value ($)', color='tab:blue')
        ax1.plot(portfolio_value.index, portfolio_value['total_value'], color='tab:blue', label='Portfolio Value')
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        ax1.grid(True)

        # Plot 2: Stock Price and Moving Averages (right y-axis)
        ax2 = ax1.twinx()
        ax2.set_ylabel(f'{symbol} Price ($)', color='tab:gray')
        ax2.plot(signals.index, signals['price'], color='gray', alpha=0.7, label=f'{symbol} Price')
        if 'short_mavg' in signals.columns:
            ax2.plot(signals.index, signals['short_mavg'], color='orange', alpha=0.8, label='Short MA')
        if 'long_mavg' in signals.columns:
            ax2.plot(signals.index, signals['long_mavg'], color='purple', alpha=0.8, label='Long MA')
        ax2.tick_params(axis='y', labelcolor='tab:gray')

        # Plotting Buy/Sell markers on the price chart
        if 'trades' in signals.columns:
            buy_signals = signals[signals['trades'] == 'BUY']
            sell_signals = signals[signals['trades'] == 'SELL']
            ax2.plot(buy_signals.index, signals.loc[buy_signals.index]['price'], '^', markersize=10, color='g', label='Buy Signal')
            ax2.plot(sell_signals.index, signals.loc[sell_signals.index]['price'], 'v', markersize=10, color='r', label='Sell Signal')

        # Final Touches
        fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
        fig.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust layout to make room for suptitle
        plt.show()
