# import matplotlib.pyplot as plt

# def plot_stock_data(data):
#     """Plot stock data with indicators."""
#     plt.figure(figsize=(12, 6))
#     plt.plot(data['Close'], label='Close Price')
#     if 'MA' in data.columns:
#         plt.plot(data['MA'], label='Moving Average')
#     if 'Upper' in data.columns and 'Lower' in data.columns:
#         plt.plot(data['Upper'], linestyle='--', color='gray', label='Upper Band')
#         plt.plot(data['Lower'], linestyle='--', color='gray', label='Lower Band')
#     plt.legend()
#     plt.show()
import plotly.graph_objects as go

def plot_stock_data(data):
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name="Candlestick"
    )])

    fig.update_layout(
        title="Initial Stock Data",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark"
    )
    return fig

def plot_stock_with_signals(data, positions):
    fig = go.Figure()

    # Plot the stock closing price
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='Stock Price'
    ))

    # Separate buy and sell signals from positions
    buys = [(date, price) for date, action, shares, price in positions if action == "Buy"]
    sells = [(date, price) for date, action, shares, price in positions if action == "Sell"]

    # Plot buy signals
    if buys:
        buy_dates, buy_prices = zip(*buys)
        fig.add_trace(go.Scatter(
            x=buy_dates,
            y=buy_prices,
            mode='markers',
            marker=dict(symbol='triangle-up', color='green', size=10),
            name='Buy Signal'
        ))

    # Plot sell signals
    if sells:
        sell_dates, sell_prices = zip(*sells)
        fig.add_trace(go.Scatter(
            x=sell_dates,
            y=sell_prices,
            mode='markers',
            marker=dict(symbol='triangle-down', color='red', size=10),
            name='Sell Signal'
        ))

    # Customize layout
    fig.update_layout(
        title="Backtest Results with Buy/Sell Signals",
        xaxis_title="Date",
        yaxis_title="Close Price",
        template="plotly_dark"
    )

    return fig
