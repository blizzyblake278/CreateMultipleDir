import pandas as pd
import os


# URL = 'https://pythonbasics.org/read-excel/'


def main():
    counter = 0
    df = pd.read_excel('sample.xls')  # df = datafile
    dfDATE = df['DATE'].dt.strftime(' -- DUE %m-%d-%y').tolist()  # gets data from date column & formats it to list
    dfSKU = df['SKU'].tolist()

    listTest = [i + j for i, j in zip(dfSKU, dfDATE)]  # combines both lists into 1 at each index.

    while counter < len(listTest):
        for i in listTest:
            # print(i)
            os.makedirs(i)
            counter += 1


if __name__ == '__main__':
    main()
