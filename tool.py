import os as os
import pandas as pd

DATA_PATH = "data"


"""A class manager for a specific CSV data set."""


class Tool:
    def __init__(self, filename):
        self._df = pd.read_csv(os.path.join(DATA_PATH, filename))

    """Reads the CSV file of the given filename and returns the pandas.DataFrame."""
    def get_data(self):
        return self._df

    """Returns None if the time coloumn in the CSV file is consistent.
    Returns a list of timestamps and its corresponding indexes if faults are found."""
    def check_timestamp(self):
        pass

    """Returns a list of tuples for each outlier with its corresponding timestamp."""
    def get_outliers(self, data_type):
        pass
