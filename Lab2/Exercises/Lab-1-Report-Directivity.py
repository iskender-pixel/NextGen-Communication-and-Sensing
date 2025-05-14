import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from friis import *


def PlotDirectivity(S21, f, r):
    c = 3e8
    # G = getG(S21, f , r)
    # A = Aeff(f,G)
    # D = ((np.pi*4*(r**2))/A) * abs(S21)**2
    #
    wavelength = c/f
    D = (4*np.pi*r/wavelength)*abs(S21)

    plt.figure(figsize=(8, 6))
    plt.rcParams['font.size'] = 16
    plt.plot(f/1e9, 10*np.log10(D))
    plt.xlabel('Frequency (GHz)', fontsize=15)
    plt.ylabel('Directivity (dB)', fontsize=15)
    # plt.ylim(-40,2)
    # plt.legend()
    # plt.ylim(17, 21.5)
    plt.yticks([17,18,19,20,21], fontsize=15)

    plt.grid(True)
    plt.tick_params(axis='both', labelsize=15)
    plt.tight_layout()
    plt.savefig('Directivity.svg')
    plt.show()
    return
if __name__ == "__main__":

    S = rf.Network('../Data2/direction0-1.29v2.s2p')

    S21 = S.s21.s.squeeze()
    fRange = S.frequency.f.squeeze()

    PlotDirectivity(S21, fRange, 1.29)






