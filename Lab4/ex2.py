import numpy as np
import matplotlib.pyplot as plt

P_peak = 150e3  #150 kW
f0 = 9.4e9      #9.4 GHz
PulseWidth = 1.2e-6
PRF = 2e3
G_dB = 45
G_Linear=10**(G_dB/10)
T_d = 18.3e-3
F_dB = 2.5
F_linear = 10**(F_dB/10)
Lr_dB = 11.2
La_dB = 0.16 #dB/km

# 5<R<105 km
# -20 < RCS < 3 dBsm


#SNR in dB as function of range for worst case detection
def averagePower(P_peak, PulseWidth, PRF):
    Pav = P_peak * PulseWidth * PRF
    return Pav

def SNR_c(P,T_d,G_dB,RCS,f0,Lr_dB,La_dB,F_dB, R, PRF, tau):
    wavelength = 2.997e8 / f0
    n = T_d * PRF
    B = 1 / tau
    L_dB = Lr_dB + La_dB*(R/1000)

    SNR_c = 10*np.log10(P) + 2*G_dB + 20*np.log10(wavelength) + RCS + 10*np.log10(n) - 33 - 40*np.log10(R) + 204 - F_dB - 10*np.log10(B) - L_dB
    return SNR_c

R = np.linspace(5000,105000,100)
#R = 10*np.log10(R)
RCS = np.linspace(-20, 3, 23)
RCS_grid, R_grid = np.meshgrid(RCS, R)
SNR = SNR_c(P_peak, T_d, G_dB, RCS_grid, f0, Lr_dB, La_dB, F_dB, R_grid, PRF, PulseWidth)
print(SNR.shape)
# plt.plot(R/1000,SNR)
# plt.xlabel('R (km)')
# plt.ylabel('SNR (dB)')
# plt.show()
#

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(RCS_grid, R_grid, SNR, cmap='viridis')

ax.set_xlabel('RCS (m²)')
ax.set_ylabel('Range R (m)')
ax.set_zlabel('SNR (dB)')
ax.set_title('3D Plot of SNR vs RCS and Range')

plt.show()
