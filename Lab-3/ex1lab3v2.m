clc; clear; close all;

e_eff = @(e_rel, d, W) (e_rel+1)/2 + ((e_rel-1)/2) * (1+12*d/W)^(-0.5);
L_eff = @(fr, e_eff) 2.997e8 / (2*fr*sqrt(e_eff));
W = @(fr, e_r) 2.997e8 / (2*fr*sqrt((e_r+1)/2));
Lslot = @(e_eff, d, W) 0.412*d*((e_eff + 0.3)*(W/d + 0.264))/((e_eff - 0.258)*(W/d + 0.8));

E_theta = @(k,W,theta,phi,L) sinc(k*W*sin(theta).*sin(phi)/(2*pi)) .*cos(k*L/2 .*sin(theta) .*cos(phi)) .* cos(phi);
E_phi = @(k,W,theta,phi,L) sinc(k*W*sin(theta).*sin(phi)/(2*pi)) .*cos(k*L/2 .*sin(theta) .*cos(phi)) .*cos(theta) .* sin(phi);

% --- Constants ---
f1 = 14e9;
f2 = 15e9;
f3 = 16e9;
freq = f3;          % Frequency 15 GHz
eps_r = 3.66;         % Relative permittivity
d = 0.0005;           % Substrate thickness 0.5 mm

% --- Calculate patch parameters ---
Width = W(freq, eps_r);
eps_eff = e_eff(eps_r, d, Width);
Length_eff = L_eff(freq, eps_eff);
Length = Length_eff - 2*Lslot(eps_eff, d, Width);

k1 = 2*pi*f1/2.997e8; % Wave number
k2 = 2*pi*f2/2.997e8; % Wave number
k3 = 2*pi*f3/2.997e8; % Wave number

%directivity
theta = linspace(eps,pi,180);
phi = linspace(eps,2*pi, 360);
[THETA, PHI] = meshgrid(theta, phi);
THETA_DEG = rad2deg(THETA);
PHI_DEG = rad2deg(PHI);

%14 GHz
Ephi1 = E_phi(k1, Width, THETA, PHI, Length);
Etheta1 = E_theta(k1, Width, THETA, PHI, Length);
Etotal1 = sqrt(abs(Ephi1).^2 + abs(Etheta1.^2));
Etotal_dB1 = 20*log10(Etotal1);

%15GHz
Ephi2 = E_phi(k2, Width, THETA, PHI, Length);
Etheta2 = E_theta(k2, Width, THETA, PHI, Length);
Etotal2 = sqrt(abs(Ephi2).^2 + abs(Etheta2.^2));
Etotal_dB2 = 20*log10(Etotal2);
    
%16GHz
Ephi3 = E_phi(k3, Width, THETA, PHI, Length);
Etheta3 = E_theta(k3, Width, THETA, PHI, Length);
Etotal3 = sqrt(abs(Ephi3).^2 + abs(Etheta3.^2));
Etotal_dB3 = 20*log10(Etotal3);


%Slices
% patternCustom(Etotal_dB1(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(eps)); hold on;
% patternCustom(Etotal_dB2(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(eps)); hold on;
% patternCustom(Etotal_dB3(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(eps));

% patternCustom(Etotal_dB1(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi(90))); hold on;
% patternCustom(Etotal_dB2(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi(90))); hold on;
% patternCustom(Etotal_dB3(:),THETA_DEG(:),PHI_DEG(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi(90)));

%3D plot
%patternCustom(Etotal_dB1(:),THETA_DEG(:),PHI_DEG(:));
%caxis([-30 0]);

% patternCustom(Etotal_dB2(:),THETA_DEG(:),PHI_DEG(:));
% caxis([-30 0]);

%patternCustom(Etotal_dB3(:),THETA_DEG(:),PHI_DEG(:));
%caxis([-30 0]);

%directivity
U1 = abs(Etotal1).^2;
Umax1 = max(U1(:)); 
Prad1 = trapz(phi, trapz(theta, U1.*sin(THETA), 2));
D1 = 4*pi*Umax1/Prad1;
D_dB1 = 10*log10(abs(D1));

U2 = abs(Etotal2).^2;
Umax2 = max(U2(:)); 
Prad2 = trapz(phi, trapz(theta, U2.*sin(THETA), 2));
D2 = 4*pi*Umax2/Prad2;
D_dB2 = 10*log10(abs(D2));

U3 = abs(Etotal3).^2;
Umax3 = max(U3(:)); 
Prad3 = trapz(phi, trapz(theta, U3.*sin(THETA), 2));
D3 = 4*pi*Umax3/Prad3;
D_dB3 = 10*log10(abs(D3));

fprintf('Directivity14 (dB): %.3f dB\n',D_dB1);
fprintf('Directivity15 (dB): %.3f dB\n',D_dB2);
fprintf('Directivity16 (dB): %.3f dB\n',D_dB3);

%Radiation Resistance
radres = @(eps_r, L, W) 90 * (eps_r^2/(eps_r - 1)) * (L/W)^2;
opBW = @(eps_r, W, L, d, lamda) 3.77 * ((eps_r -1)/eps_r^2) * (W/L) * (d/lamda);

lamda = 3e8/15e9;
RadResistance = radres(3.66, Length, Width);
OperativeBW = opBW(3.66, Width, Length, d, lamda);

fprintf("Radiation resistance of %.3f dB", RadResistance);
fprintf("With operative BW of %.3f Hz", OperativeBW);