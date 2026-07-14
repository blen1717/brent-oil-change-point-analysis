import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def plot_prices(df, title='Brent Oil Prices (1987-2022)'):
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df['Date'], df['Price'], linewidth=0.8, color='navy')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (USD per Barrel)', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig, ax

def stationarity_test(series, name='Series'):
    result = adfuller(series)
    print(f"ADF Statistic: {result[0]:.6f}")
    print(f"p-value: {result[1]:.6f}")
    print(f"Stationary: {'Yes' if result[1] < 0.05 else 'No'}")
    return result
