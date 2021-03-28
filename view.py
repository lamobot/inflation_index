import pandas as pd
from config import INDEX_CSV_FILE
import matplotlib.pyplot as plt
import datetime
import matplotlib
# matplotlib.use('Agg')


def show_index_plot():
    df = pd.read_csv(INDEX_CSV_FILE, dtype={'fuel_index': float, 'housing_index': float, 'product_index': float})
    # df['sum_index'] = df['fuel_index'] + df['housing_index'] + df['product_index']
    #
    # plt.plot(df['date'], df['sum_index'], label='Inflation index per day')
    # plt.plot(df['date'], df['fuel_index'], label='Inflation index per day')
    df.plot()
    plt.show()


if __name__ == '__main__':
    show_index_plot()
