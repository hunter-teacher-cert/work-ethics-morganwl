"""Fetch and display some sample information from the New York Times
covid dataset.
"""

from operator import itemgetter
import urllib.request

COVID_DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

def parse_encoding(header):
    """Finds a charset entry in a header string and returns the value."""
    for entry in header.split(';'):
        if entry.lstrip().startswith('charset='):
            return entry[len('charset='):]
    return None

def fetch_data(url):
    """Fetches a URL and returns it as a decoded list of lines."""
    data = []
    with urllib.request.urlopen(url) as fh:
        encoding = parse_encoding(fh.headers['Content-Type'])
        for line in fh:
            data.append(line.decode(encoding))
    return data

def stream_data(url):
    """Requests a URL, identifies the character encoding, and yields decoded
    strings one line at a time."""
    with urllib.request.urlopen(url) as fh:
        encoding = parse_encoding(fh.headers['Content-Type'])
        for line in fh:
            yield line.decode(encoding)

def filter_county(county, data):
    """Filters an iterator of csv rows by the value of the 2nd column."""
    for line in data:
        if line.split(',')[1] == county:
            yield line


def main():
    data = (line.strip().split(',') for line in stream_data(COVID_DATA_URL))
    keys = next(data)
    rows = (dict(zip(keys, row)) for row in data)
    rows = (row for row in rows if row['county'] == 'New York City')
    rows = list(rows)
    print(f'There are {len(rows)} dates in the dataset.')
    max_death = max(rows, key=itemgetter('deaths'))
    max_cases = max(rows, key=itemgetter('cases'))
    print(f'Highest cases on {max_cases["date"]} and highest deaths on {max_death["date"]}.')

if __name__ == '__main__':
    main()
