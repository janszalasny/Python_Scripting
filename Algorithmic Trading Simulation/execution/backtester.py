# execution/backtester.py
#
# The core backtesting engine. It orchestrates the simulation,
# connecting the data handler, strategy, and portfolio.
# Acts as the Subject in the Observer pattern, notifying the Portfolio
# of price updates.

import pandas as pd


class Backtester:
    """
    The backtesting engine. It simulates the trading strategy over historical data.
    This class acts as the Subject in the Observer pattern. It notifies observers
    (the Portfolio) of new market data.
    """
    
    def __init__(self, data_handler, strategy, portfolio, visualizer):
        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.visualizer = visualizer
        self.trade_history = []
        self.signals = None
    
    def run_backtest(self):
        """
        Runs the backtest from the start to the end date of the data.
        """
        # Generate signals for the entire dataset first
        self.signals = self.strategy.generate_signals(self.data_handler.data)
        
        data_generator = self.data_handler.get_data_generator()
        
        for timestamp, row in data_generator:
            # 1. Update portfolio value with current market data (Notify Observer)
            current_market_data = {self.strategy.symbol: row['price']}
            self.portfolio.update_portfolio_value(timestamp, current_market_data)
            
            # 2. Check for trading signals for the current timestamp
            if timestamp in self.signals.index:
                signal_event = self.signals.loc[timestamp]
                if signal_event['positions'] == 1.0:  # Buy signal
                    self._execute_buy(timestamp, row['price'])
                elif signal_event['positions'] == -1.0:  # Sell signal
                    self._execute_sell(timestamp, row['price'])
    
    def _execute_buy(self, timestamp, price):
        """ Handles the logic for executing a buy order. """
        # Simple strategy: invest all available cash
        quantity_to_buy = self.portfolio.cash / price
        if quantity_to_buy > 0:
            self.portfolio.execute_trade(timestamp, self.strategy.symbol, quantity_to_buy, price, 'BUY')
            self.trade_history.append({
                'date': timestamp, 'symbol': self.strategy.symbol, 'type': 'BUY',
                'quantity': quantity_to_buy, 'price': price
            })
    
    def _execute_sell(self, timestamp, price):
        """ Handles the logic for executing a sell order. """
        # Simple strategy: sell all holdings of the symbol
        quantity_to_sell = self.portfolio.holdings.get(self.strategy.symbol, 0)
        if quantity_to_sell > 0:
            self.portfolio.execute_trade(timestamp, self.strategy.symbol, quantity_to_sell, price, 'SELL')
            self.trade_history.append({
                'date': timestamp, 'symbol': self.strategy.symbol, 'type': 'SELL',
                'quantity': quantity_to_sell, 'price': price
            })
    
    def show_results(self):
        """
        Displays the backtesting results, including a performance plot.
        """
        portfolio_value_df = self.portfolio.get_portfolio_value_df()
        
        if portfolio_value_df.empty:
            print("No portfolio data to visualize.")
            return
        
        # Add trade history to the signals DataFrame for plotting
        trade_df = pd.DataFrame(self.trade_history)
        if not trade_df.empty:
            trade_df.set_index('date', inplace=True)
            self.signals['trades'] = trade_df['type']
        
        self.visualizer.plot_performance(
            portfolio_value_df,
            self.signals,
            self.strategy.symbol
        )

