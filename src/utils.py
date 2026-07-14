import pandas as pd

def get_summary_stats(df):
    return {
        'min': df['Price'].min(),
        'max': df['Price'].max(),
        'mean': df['Price'].mean(),
        'median': df['Price'].median(),
        'std': df['Price'].std(),
        'count': len(df)
    }

def find_events_near_date(events_df, target_date, days=30):
    window = pd.Timedelta(days=days)
    mask = (events_df['Date'] >= target_date - window) & 
           (events_df['Date'] <= target_date + window)
    return events_df[mask].copy()
