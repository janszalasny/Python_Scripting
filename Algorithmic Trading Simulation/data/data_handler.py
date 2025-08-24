# data/data_handler.py
#
# Handles fetching and processing of financial market data.
# This implementation uses the yfinance library to fetch data from Yahoo Finance.

import pandas as pd
import yfinance as yf


class DataHandler:
    """
    Abstract base class for data handlers.
    Provides an interface for fetching market data.
    """
    
    def get_latest_data(self):
        """
        Returns the latest market data.
        """
        raise NotImplementedError("Should implement get_latest_data()")


class YahooFinanceDataHandler(DataHandler):
    """
    Data handler for fetching daily stock data from Yahoo Finance.
    """
    
    def __init__(self, symbol: str, start_date: str, end_date: str):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()
    
    def _fetch_data(self) -> pd.DataFrame:
        """
        Fetches historical data from Yahoo Finance.

        Returns:
            pd.DataFrame: A DataFrame with historical price data.
        """
        print(f"Fetching data for {self.symbol} from {self.start_date} to {self.end_date} using yfinance...")
        try:
            # --- CORRECTED SECTION ---
            # Use the yf.Ticker object for a more robust single-ticker download.
            # This provides a more consistent DataFrame format.
            ticker = yf.Ticker(self.symbol)
            df = ticker.history(start=self.start_date, end=self.end_date)
            # --- END OF CORRECTION ---
            
            if df.empty:
                raise ValueError("No data found for the specified symbol and date range.")
            
            # Check if 'Close' column exists before proceeding.
            if 'Close' not in df.columns:
                raise ValueError(f"'Close' column not found. Available columns: {df.columns.tolist()}")
            
            # Create a new DataFrame with just the 'Close' data, renaming it to 'price'.
            price_df = pd.DataFrame(index=df.index)
            price_df['price'] = df['Close']
            
            print("Data fetched successfully.")
            return price_df
        
        except Exception as e:
            print(f"An error occurred while fetching or processing data with yfinance: {e}")
            return pd.DataFrame()
    
    def get_data_generator(self):
        """
        A generator that yields data for each timestamp.
        This simulates a live feed of market data.
        """
        for timestamp, row in self.data.iterrows():
            yield timestamp, row
