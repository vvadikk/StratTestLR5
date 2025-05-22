from matplotlib import pyplot as plt
import seaborn as sns
import pandas
from one import new_transactions

def plot_pivot_table(pivot_table):
    plt.figure(figsize=(9, 11))
    sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.3g', annot_kws={'fontsize': 14})
    plt.xticks(fontsize=15)
    plt.yticks(rotation=0, fontsize=15)
    plt.xlabel('Bucket', size=18)
    plt.ylabel('Hour', fontsize=18)
    plt.title('Gender analysis per bucker and hour', fontsize=20)
    plt.show()

pt = pandas.pivot_table(new_transactions, index='hour', columns='amount_bucket', values='gender', aggfunc=lambda x: (x == 'M').mean()) #доля мужчин в интервале (0; 1)
plot_pivot_table(pt)