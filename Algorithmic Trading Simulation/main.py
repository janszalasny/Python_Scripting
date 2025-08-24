# main.py
#
# Main entry point for the Algorithmic Trading Simulator.
# This script initializes the necessary components, runs the backtest,
# and generates a performance plot.

import pandas as pd
from data.data_handler import YahooFinanceDataHandler # <-- UPDATED
from strategy.strategies import MovingAverageCrossoverStrategy
from portfolio.portfolio import Portfolio
from execution.backtester import Backtester
from visualization.visualizer import MatplotlibVisualizer

def main():
    """
    Main function to run the trading simulation.
    """
    # --- Configuration ---
    symbol = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    initial_capital = 100000.0
    short_window = 40
    long_window = 100

    # --- Initialization ---
    print("Initializing components...")
    # Use the new YahooFinanceDataHandler
    data_handler = YahooFinanceDataHandler(symbol=symbol, start_date=start_date, end_date=end_date)
    strategy = MovingAverageCrossoverStrategy(symbol=symbol, short_window=short_window, long_window=long_window)
    portfolio = Portfolio(initial_capital=initial_capital)
    visualizer = MatplotlibVisualizer()

    # The Backtester orchestrates the simulation
    backtester = Backtester(
        data_handler=data_handler,
        strategy=strategy,
        portfolio=portfolio,
        visualizer=visualizer
    )

    # --- Run Simulation ---
    print("Starting backtest...")
    try:
        backtester.run_backtest()
        print("Backtest completed successfully.")
    except Exception as e:
        print(f"An error occurred during the backtest: {e}")
        return

    # --- Display Results ---
    print("Generating performance report...")
    backtester.show_results()


if __name__ == "__main__":
    main()
