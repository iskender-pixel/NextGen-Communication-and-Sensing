import matplotlib.pyplot as plt
import numpy as np


def Plot(P1, P2,  xAxisLabel, yAxisLabel, Title ,Filename="untitled", SaveFile=False):
    plt.figure(figsize=(8, 6))
    plt.rcParams['font.size'] = 19
    plt.plot(P1, P2, linewidth=2.5)
    plt.xlabel(xAxisLabel, fontsize=19)
    plt.ylabel(yAxisLabel, fontsize=19)
    plt.grid(True)
    # plt.ylim([0,13])
    plt.title(Title,fontsize=19)
    plt.tick_params(axis='both', labelsize=19)
    plt.tight_layout()
    if SaveFile:
        plt.savefig(f'{Filename}.svg')
    plt.show()