import skrf as rf
import numpy as np
import matplotlib.pyplot as plt



def reflection(Zl, Z0):

    Gamma = (Zl-Z0)/(Zl+Z0)

    return Gamma


def Zin(f, Zl, Z0, l, krel):

    k = (krel * 2 * np.pi*f) / 2.997e8

    Z_in = Z0 * ( (Zl+1j*Z0*np.tan(k*l)) / (Z0+1j*Zl*np.tan(k*l)) )

    return Z_in


def parse_impedance_data(file_path):
    frequencies = []
    z_real = []
    z_imag = []

    with open(file_path, 'r') as f:
        for line in f:
            # Skip comments and empty lines
            if line.startswith("#") or line.strip() == "":
                continue
            parts = line.strip().split()
            if len(parts) >= 3:
                frequencies.append(float(parts[0]))
                z_real.append(float(parts[1]))
                z_imag.append(float(parts[2]))

    return np.array(frequencies), np.array(z_real), np.array(z_imag)


def plotReflection(Zl, Z0, fRange):


    gamma_squared = abs(reflection(Zl,Z0))**2

    plt.figure(figsize=(8, 5))
    plt.plot(fRange, 10*np.log10(gamma_squared))
    plt.xlabel('Frequency (GHz)', fontsize=15)
    plt.ylabel('Power reflection coefficient [dB] ' ,fontsize=15)
    plt.grid(True)
    plt.tick_params(axis='both', labelsize=15)
    # plt.xticks(np.linspace(0, 10, 11))
    # plt.yticks(np.linspace(-180, 180, 10))
    # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    plt.tight_layout()
    plt.savefig("ReflectedpowerPlot.svg")

    plt.show()

    return 0

def plotRadiatedPower(Zl, Z0, fRange, P_in):

    gamma_squared = abs(reflection(Zl, Z0)) ** 2

    power_transmitted = (1-gamma_squared)*P_in

    plt.figure(figsize=(8, 5))
    plt.rcParams['font.size'] = '16'
    plt.plot(fRange, 10*np.log10(power_transmitted))
    plt.xlabel('Frequency (GHz)', fontsize=15)
    plt.ylabel('Radiated power [dBW] ', fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    plt.grid(True)

    # plt.xticks(np.linspace(0, 10, 11))
    # plt.yticks(np.linspace(-180, 180, 10))
    # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    plt.savefig("radiatedpowerPlot.svg")
    plt.show()

    return 0
if __name__ == '__main__':

    # Gamma = reflection(50+100j, 50)
    # print(abs(Gamma)**2)
    #
    # Zin = Zin(15e9, 50+100j, 50, 0.05, 0.8)
    # print(Zin)

    frequencies, z_real, z_imag = parse_impedance_data("Impedance_Antenna.txt")
    Zl = z_real + 1j*z_imag

    plotReflection(Zl, 50, frequencies)


    plotRadiatedPower(Zl, 50, frequencies, 0.1)


