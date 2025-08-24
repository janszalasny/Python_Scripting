# Algorithmic Trading Simulator

## Project Overview
This project is an event-driven backtesting engine written in pure Python that allows users to simulate and evaluate algorithmic trading strategies on historical market data. It is built with a focus on modularity, scalability, and adherence to professional software engineering practices, including Object-Oriented Programming (OOP) and common design patterns.

The primary goal of this simulator is to provide a robust framework for quantitative analysis, enabling the development and testing of trading hypotheses before deploying them in a live market.

## Features
- **Event-Driven Architecture:** Simulates the flow of time by processing market data tick-by-tick, providing a realistic backtesting environment.
- **Strategy Pattern for Algorithms:** Easily implement and switch between different trading strategies (e.g., Moving Average Crossover, RSI, etc.) without altering the core engine.
- **Observer Pattern for Portfolio Management:** The portfolio is decoupled from the backtesting engine and updates its state in real-time as it gets notified of new market data.
- **Yahoo Finance Integration:** Uses the reliable `yfinance` library to fetch historical stock data, removing the need for API keys.
- **Performance Visualization:** Generates clear and informative performance charts using Matplotlib, plotting portfolio value against stock price, moving averages, and trade execution signals.
- **Modular and Scalable:** The codebase is organized into distinct modules (`data`, `strategy`, `portfolio`, `execution`), making it easy to extend and maintain.
- **Dockerized:** Comes with a Dockerfile for easy containerization, ensuring the application can run consistently in any environment.

## Tech Stack
- **Language:** Python 3.9+
- **Libraries:**
  - `pandas` for data manipulation and analysis
  - `numpy` for numerical operations
  - `yfinance` for fetching historical market data
  - `matplotlib` for data visualization and plotting results
- **Containerization:** Docker

## Design Patterns Used
This project intentionally incorporates several software design patterns to ensure a clean and maintainable architecture.

### 1. Strategy Pattern
- **Purpose:** To define a family of algorithms, encapsulate each one, and make them interchangeable.
- **Implementation:**  
  The `Strategy` class is an abstract base class that defines the interface for all trading strategies. Concrete strategies, like `MovingAverageCrossoverStrategy`, inherit from this class and implement their own `generate_signals` method. This allows the backtester to work with any strategy that conforms to the interface.

### 2. Observer Pattern
- **Purpose:** To define a one-to-many dependency between objects so that when one object (the Subject) changes state, all its dependents (Observers) are notified and updated automatically.
- **Implementation:**  
  - **Subject:** The Backtester acts as the subject. As it iterates through historical data, it notifies its observers of new price updates.  
  - **Observer:** The Portfolio acts as an observer. It registers with the backtester and implements an `update_portfolio_value` method, which is called by the subject on each tick. This decouples the portfolio's state management from the core backtesting loop.

## Setup and Installation

* **Clone the Repository**  
`git clone https://github.com/your-username/algorithmic-trading-simulator.git`  
`cd algorithmic-trading-simulator`

* **Create a Virtual Environment (Recommended)**  
`python -m venv .venv`  
`source .venv/bin/activate`  *(On Windows, use `.venv\Scripts\activate`)*

* **Install Dependencies**  
`pip install -r requirements.txt`

## Usage

* To run the simulation, execute:  
`python main.py`

* Configure simulation parameters (symbol, date range, initial capital, strategy parameters) directly in the `main()` function in `main.py`.

* After completion, a Matplotlib chart will display the performance of the strategy.

# Running with Docker

* **Build the Docker Image**  
`docker build -t trading-simulator .`

* **Run the Docker Container**  
`docker run --rm trading-simulator`

*Note:* Running Matplotlib in Docker may require extra configuration for GUI display. For headless environments or CI/CD, modify the visualizer to save plots to a file instead of displaying them.

## Future Improvements

* **Add More Strategies:** Implement other trading strategies like RSI, Bollinger Bands, or Momentum.  
* **Support for Multiple Assets:** Enable trading multiple symbols simultaneously.  
* **Advanced Risk Management:** Include stop-loss, take-profit, and other rules.  
* **Performance Metrics:** Show advanced metrics like Sharpe Ratio, Sortino Ratio, Maximum Drawdown, Calmar Ratio.  
* **Parameter Optimization:** Run multiple backtests to find optimal strategy parameters.
