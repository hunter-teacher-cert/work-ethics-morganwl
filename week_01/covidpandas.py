"""Fetches covid dataset and does some basic transformations using
pandas."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

COVID_DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

def get_latest_nationwide(df):
    """Returns a dataframe containing entries for all counties on the
    most recent date."""

    latest_date = df['date'].max()
    return df[(df['date'] == latest_date)]

def get_county(df, county):
    """Returns a dataframe containing all entries for a given county,
    indexed by the 'date' column."""
    return df[(df['county'] == county)].set_index(['date'])

def get_nyc(df):
    """Returns a dataframe containing all entries for New York City."""
    return get_county(df, 'New York City')

def add_days(df):
    """Adds a 'days' column that counts days elapsed since the first
    row."""
    df['days'] = (df['date'] - df['date'].iloc[0]).dt.days

def main():
    """Main function"""

    # download covid data
    data = pd.read_csv(COVID_DATA_URL)
    # convert date column to datetime object
    data['date'] = pd.to_datetime(data['date'])

    # add a column for absolute days as an offset from the first date in the
    # dataset
    add_days(data)

    # get a subset containing the most recent day for every county in the dataset
    # we don't do anything with this, though
    latest_nationwide = get_latest_nationwide(data)

    # get a subset containing only New York City
    newyork = get_nyc(data)
    # the dataset should already be sorted by date, but just in case
    newyork = newyork.sort_values(['date'])
    # the dataset measures cumulative cases; let's add a column with the delta as well
    newyork['new_cases'] = newyork['cases'] - newyork['cases'].shift(1)
    # replace NaN with 0
    newyork['new_cases'] = newyork['new_cases'].fillna(0)

    # fit the data with a polynomial regression. this isn't the best way to fit
    # this data, and a one dimensional regression looking only at time and no
    # other features is probably not very useful anyway
    r = np.polynomial.Chebyshev.fit(newyork['days'], newyork['new_cases'],
                                    deg=6)
    newyork['regression'] = r(newyork['days'])

    # plot the regression against the actual case data
    newyork.plot(y=['new_cases', 'regression'], use_index=True)
    plt.show()

if __name__ == '__main__':
    main()
