import os as os
import csv as csv
import numpy as np


DATA_PATH = "data"
CSV_DELIMITER = ','


class Tool:
    def __init__(self):
        pass

    @staticmethod
    def get_data(filename):
        # file = open(os.path.join(DATA_PATH, filename))
        # data = np.loadtxt(os.path.join(DATA_PATH, filename), delimiter=CSV_DELIMITER)
        d = open(os.path.join(DATA_PATH, filename), 'r')
        dre = csv.reader(d, delimiter=',')
        temp = []
        a = 1
        for row in dre:
            if a == 1:
                a += 1
            elif a == 2:
                a = 0
            else:
                temp.append(row[1])

        return temp
