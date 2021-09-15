"""Fetches the 'famous' iris dataset and sets it up for a very naive KNN algorithm."""

from zlib import crc32

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

IRIS_DATASET_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
IRIS_NAMES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

def test_set_check(identifier, test_ratio):
    """Uses a hash function to consistently return True if an identifier belongs in a test set."""
    # src: (Geron, 2019, 53)
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_test(df, test_ratio=0.2, id_column='index'):
    """Splits an input dataframe into two separate dataframes, based on the
    test_ratio. Row index is used as the identifier for consistent
    separation."""
    # src: (Geron, 2019, 54)
    ids = df[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return df.loc[~in_test_set], df.loc[in_test_set]

def explore_dataset(df):
    """Some quick exploration of a dataframe."""
    df.hist()
    plt.show()

def l2_distance(vector, other):
    """Returns the euclidean distance between vector and other."""
    return np.sqrt(np.sum((vector - other) ** 2))

def get_nearest_neighbors(model, v, k):
    """Returns a dataframe of the k nearest neighbors to v."""

    # Currently uses the naive approach to sort the entire dataset by distance
    # from v and then pull the first k elements
    neighbors = model
    neighbors['d'] = model.apply(lambda r: l2_distance(r, v), axis=1, raw=True)
    neighbors = neighbors.sort_values('d')
    return neighbors.iloc[0:k]

def predict(data, labels, v):
    knn = get_nearest_neighbors(data, v, 3)
    return labels.loc[knn['index']].mode()['class'].iloc[0]

def main():
    """Main function"""

    # Fetch the dataset
    df = pd.read_csv(IRIS_DATASET_URL, names=IRIS_NAMES).reset_index()
    print(df.info())
    print(df.head)

    # Separate data from labels
    data = df.loc[:, 'index':'petal_width']
    print(data.info())
    labels = df['class']

    # Separate the test set
    training_data, test_data = split_test(data)
    training_labels, test_labels = split_test(labels.reset_index())

    # Plot some data about the training set
    explore_dataset(training_data)

    # test get_nearest_neighbors
    knn = get_nearest_neighbors(training_data, training_data.iloc[65], 3)
    print(predict(training_data, training_labels, training_data.iloc[65]))

if __name__ == '__main__':
    main()
