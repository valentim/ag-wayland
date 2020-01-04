import numpy as np
import matplotlib.pyplot as plt


def save(x, y, labels):
    fig = plt.figure(dpi=128, figsize=(10,6))
    
    plt.stackplot(x,y, labels=labels, baseline='weighted_wiggle')
    plt.legend(loc='upper left')
    fig.autofmt_xdate()
    plt.savefig('books_read.png')