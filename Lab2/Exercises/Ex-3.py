import skrf as rf
import numpy as np
import matplotlib.pyplot as plt

def normalized_radiation_intensity(theta_rad, lx, wavelength):
    gamma = np.sin(theta_rad) * lx / wavelength
    return (np.sinc(gamma))**2  # np.sinc(x) = sin(pi x)/(pi x)

def plotPattern(lx, f):
    theta_rad = np.linspace(-np.pi/2, np.pi/2, 800)
    wavelength = 2.997e8 / f
    radpat = normalized_radiation_intensity(theta_rad, lx, wavelength)

    plt.figure(figsize=(8, 5))
    plt.plot(theta_rad*(180/np.pi), 20*np.log10(radpat))
    plt.xlabel('Theta (Deg)')
    plt.ylabel('Radiation pattern')
    plt.grid(True)
    # plt.xticks(np.linspace(0, 10, 11))
    # plt.yticks(np.linspace(-180, 180, 10))
    # plt.xlim(thru.frequency.f.min()/1e9, thru.frequency.f.max()/1e9)
    #plt.savefig("radiatedpowerPlot.svg")
    plt.show()
    return



if __name__ == '__main__':
    plotPattern(0.0886, 15e9)
