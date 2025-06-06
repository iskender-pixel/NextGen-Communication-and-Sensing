import skrf as rf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def e_eff(e_rel, d, W):
    e_eff = (e_rel+1)/2 + ((e_rel-1)/2) * (1+12*d/W)**(-0.5)
    return e_eff

def L_eff(fr, e_eff):
    L_eff = 2.997e8 / (2*fr*np.sqrt(e_eff))
    return L_eff

def W(fr, e_r):
    W = 2.997e8 / (2*fr*np.sqrt((e_r+1)/2))
    return W

def Lslot(e_eff, d, W):
    Lslot = 0.412*d*((e_eff + 0.3)*(W/d + 0.264))/((e_eff - 0.258)*(W/d + 0.8))
    return Lslot

def PatchRadTheta(k,W,L,theta,phi):
    E = np.sinc((k*W*np.sin(theta)*np.sin(phi))/(2*np.pi)) * np.cos((k*L)/2 * np.sin(theta) * np.cos(phi)) * np.cos(phi)
    return E

def PatchRadPhi(k,W,L,theta,phi):
    E = np.sinc((k*W*np.sin(theta)*np.sin(phi))/(2*np.pi)) * np.cos((k*L)/2 * np.sin(theta) * np.cos(phi)) * np.cos(theta) * np.sin(phi)
    return E

def PatchRad(E_theta,E_phi):
    f = np.sqrt(E_theta**2 + E_phi**2)
    return f

Width = W(15e9, 3.66)
eps_eff = e_eff(3.66, 0.0005, Width)
Length_eff = L_eff(15e9, eps_eff)
Length = Length_eff - 2*Lslot(eps_eff, 0.0005, Width)

theta = np.linspace(-90, 90, 180)
phi = np.linspace(-90, 90, 180)
theta_rad = np.deg2rad(theta)
phi_rad = np.deg2rad(phi)
k = 2*np.pi*15e9/2.997e8
radius = PatchRad(PatchRadTheta(k, Width, Length, theta_rad, phi_rad), PatchRadPhi(k, Width, Length, theta_rad, phi_rad))

# Create meshgrid for theta and phi
THETA, PHI = np.meshgrid(theta_rad, phi_rad)

# Recompute the radiation pattern over the grid
E_theta = PatchRadTheta(k, Width, Length, THETA, PHI)
E_phi = PatchRadPhi(k, Width, Length, THETA, PHI)
radius = PatchRad(E_theta, E_phi)

# Convert spherical to Cartesian coordinates for 3D plotting
X = radius * np.sin(THETA) * np.cos(PHI)
Y = radius * np.sin(THETA) * np.sin(PHI)
Z = radius * np.cos(THETA)

# Plotting
fig = plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Radiation Pattern')
plt.show()
