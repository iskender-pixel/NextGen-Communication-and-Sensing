import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

def FindIndex(f, fRange):

    i = np.argmin(np.abs(fRange -f))

    return i
def FindIndexP(power):

    i = np.argmin(np.abs(power + 3))

    return i


def PlotRadiationPattern(f):

    fRange = rf.Network(f'../../Lab-2/Data/direction0.s2p').frequency.f.squeeze()

    fIndex = FindIndex(f, fRange)

    angle = list(range(-40, 41, 2))
    power = []

    for i in angle:
        S_i = rf.Network(f'../../Lab-2/Data/direction{i}.s2p')
        S12_i = S_i.s12.s.squeeze()[fIndex]
        S12_i_dB = 20 * np.log10(abs(S12_i))
        power.append(S12_i_dB)

    np.array(angle)
    np.array(power)
    power = power - max(power)
    FindIndexP(power)

    plt.figure(figsize=(20, 6))
    plt.rcParams['font.size'] = 16
    plt.plot(angle, power, label=f"Frequency: {f/ 1e9} GHz")
    plt.xlabel('Angle (degrees)', fontsize=15)
    plt.ylabel('Normalized Radiation Pattern (dB)', fontsize=15)
    plt.ylim(-40,2)
    plt.legend()
    plt.grid(True)
    plt.xticks(np.arange(-40, 41, 2))
    plt.axhline(-3, color='red', linestyle='--', label='-3 dB Threshold')
    plt.tick_params(axis='both', labelsize=15)
    plt.tight_layout()
    # plt.savefig(f'RadPat_F_{f/1e9:.02f}GHz.svg')

    return
if __name__ == '__main__':
    PlotRadiationPattern(12e9)
    PlotRadiationPattern(15e9)
    PlotRadiationPattern(17e9)
    plt.show()


