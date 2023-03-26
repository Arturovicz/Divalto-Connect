import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def specific_query(cursorij, table, column, specificity):
    try:
        cursorij.execute(f"select * from {table} where {column} like '%{specificity}%'")
        glob_data = cursorij.fetchall()
        return glob_data
    except:
        raise Exception("Could not execute, verify details of table/column/specificity ")


class Queries:
    def __init__(self):
        pass


def ecdsa_curve():
    x = np.linspace(-100, 100, 1000)
    y = x**3 + x + 7
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    ecdsa_curve()