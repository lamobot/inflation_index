import pandas as pd
from config import INDEX_CSV_FILE
import matplotlib.pyplot as plt


def show_index_plot():
    df = pd.read_csv(INDEX_CSV_FILE, dtype={'fuel_index': float, 'housing_index': float, 'product_index': float})
    df['sum_index'] = df['fuel_index'] + df['housing_index'] + df['product_index']
    df.plot(title="Russian Inflation Index", x='date')
    plt.show()


if __name__ == '__main__':
    show_index_plot()
