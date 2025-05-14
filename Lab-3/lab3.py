import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import interpolate
from statsmodels.sandbox.regression.ar_panel import PanelAR1


def imp(S22, Z0):
    Zin = Z0 * (1+S22) / (1-S22)
    return Zin

def OperationalBW(S22, f):
    mask = 20*np.log(abs(S22)) < -10

    print(20*np.log(abs(S22)))

    indices = np.where(mask)[0]

    print(f[indices])

    f_low = f[indices[0]]
    f_high = f[indices[-1]]
    print(f_low, f_high)

    BW = f_high - f_low
    return BW

P1 = rf.Network("Exercises/Patch1.s2p")
P2 = rf.Network("Exercises/Patch2.s2p")
P4 = rf.Network("Exercises/Patch4.s2p")
A = rf.Network("Exercises/Patch8/Patch8A.s2p")
B = rf.Network("Exercises/Patch8/Patch8B.s2p")
C = rf.Network("Exercises/Patch8/Patch8C.s2p")
D = rf.Network("Exercises/Patch8/Patch8D.s2p")

freq = B.frequency.f.squeeze()

S22P1 = P1.s22.s.squeeze()
S22P2 = P2.s22.s.squeeze()
S22P4 = P4.s22.s.squeeze()
S22A = A.s22.s.squeeze()
S22B = B.s22.s.squeeze()
S22C = C.s22.s.squeeze()
S22D = D.s22.s.squeeze()

impP1 = imp(S22P1, 50)
impP2 = imp(S22P2, 50)
impP4 = imp(S22P4, 50)
impA = imp(S22A, 50)
impB = imp(S22B, 50)
impC = imp(S22C, 50)
impD = imp(S22D, 50)

#plotting impedances
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impP1), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impP1), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotP1.svg", format="svg")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impP2), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impP2), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotP2.svg", format="svg")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impP4), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impP4), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotP4.svg", format="svg")
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impA), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impA), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotA.svg", format="svg")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impB), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impB), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotB.svg", format="svg")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impC), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impC), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotC.svg", format="svg")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# plt.plot(freq / 1e9, np.real(impD), label='Real(Z)', color='blue', linewidth=2)
# plt.plot(freq / 1e9, np.imag(impD), label='Imag(Z)', color='red', linewidth=2)
# plt.title("Input Impedance vs Frequency", fontsize=14)
# plt.xlabel("Frequency (GHz)", fontsize=12)
# plt.ylabel("Input Impedance (Ohms)", fontsize=12)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.tight_layout()
# plt.savefig("impedance_plotD.svg", format="svg")
# plt.show()



#(f"Input impedance Patch1: {impedance} Ohm")


#plotting
plt.plot(freq, 20*np.log10(abs(S22P4)))
plt.axhline(-10)
#plt.xlim(1.35e10,1.52e10)
plt.show()

def operationalBW(S22, freq):
    # calculate the crossings of the -10 dB line
    diff = 20 * np.log10(abs(S22)) + 10
    # Find where the sign changes (crossing points)
    sign_changes = np.where(np.diff(np.sign(diff)))[0]

    # Interpolate to get more accurate x-values of intersection
    x_intersections = []
    x_bw = []
    for i in sign_changes:
        f = interpolate.interp1d(diff[i:i + 2], freq[i:i + 2])
        x_cross = f(0.0)
        x_intersections.append(float(x_cross))

    for i in range(len(x_intersections) - 2):
        x_bw.append((x_intersections[i + 1] - x_intersections[i]) / 10 ** 9)
    print("Operational BW:", max(x_bw))
    return

operationalBW(S22P4, freq)