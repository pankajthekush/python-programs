import numpy as np
import matplotlib.pyplot as plt


def createhistogram(text):
    words = text.split()
    count = dict()

    for word in words:
        count[word] = count.get(word,0) +1
    return count





def showhistogram(dictdata):
    pos = np.arange(len(dictdata.keys()))
    width = 1.0     # gives histogram aspect to the bar diagram

    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(dictdata.keys())

    plt.figure(figsize=(20, 3)) 
    plt.bar(dictdata.keys(), dictdata.values(), width=0.5, color='g',align='edge')

    plt.show()