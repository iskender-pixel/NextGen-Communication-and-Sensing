        from Exercise1 import *
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    S = rf.Network('../Data/direction0.s2p')

    S11 = S.s11.s.squeeze()
    S22 = S.s22.s.squeeze()
    f = S.frequency.f.squeeze()

    S11_dB = 20*np.log10(abs(S11))
    S22_dB = 20*np.log10(abs(S22))

    plt.figure(figsize=(8, 6))
    plt.rcParams['font.size'] = 16
    plt.plot(f*1e-9, S11_dB, label='Antenna 1 (dB)')
    plt.plot(f*1e-9, S22_dB, label='Antenna 2 (dB)')
    plt.xlabel('Frequency (GHz)', fontsize=15)
    plt.ylabel('Magnitude (dB)', fontsize=15)
    plt.legend(fontsize=14)
    plt.grid(True)
    plt.tick_params(axis='both', labelsize=15)
    plt.tight_layout()
    plt.savefig('Reflection.svg')
    plt.show()

    below_10dB = S11_dB < -50

    f_band = f[below_10dB]
    f_low = f_band[0]
   


    print(f"Low frequency: {f_low*1e-9:.2f}")
