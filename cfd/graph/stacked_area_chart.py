import numpy as np
import matplotlib.pyplot as plt


def save(x, y, labels):
    plt.stackplot(x,y, labels=labels)
    plt.legend(loc='upper left')
    plt.savefig('books_read.png')