import numpy as np
import matplotlib.pyplot as plt


def save(x, y, labels):
    fig = plt.figure(dpi=128, figsize=(10,6))
    
    plt.stackplot(x,y, labels=labels)
    plt.legend(loc='upper left')
    fig.autofmt_xdate()
    plt.savefig('../example/books_read.png')