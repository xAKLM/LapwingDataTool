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
        time_list = self.get_column("Time")
        faulty_list = []
        previous_time = -0.05

        for time in time_list:
            if time - previous_time != 0.05:
                faulty_list.append(time)
            previous_time = time

        return faulty_list

    """Returns a list of tuples for each outlier with its corresponding timestamp."""
    def get_outliers(self, data_type):
        if data_type == "Altitude":
            return self.get_column("Altitude")
        if data_type == "Pressure":
            pass
        if data_type == "Velocity":
            pass
        if data_type == "Temperature":
            pass
        if data_type == "Events":
            pass
        if data_type == "Voltages":
            pass

    """Returns the raw data of a given column name"""
    def get_column(self, column_name):
        return getattr(self._df, column_name)


