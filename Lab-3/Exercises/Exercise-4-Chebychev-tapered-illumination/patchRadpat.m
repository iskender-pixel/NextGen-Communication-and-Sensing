f = 15e9;
c = 3e8;                
lambda = c / f;     
epsr = 3.66;
k = 2*pi / (lambda*sqrt(epsr));
L = 0.5 * lambda/sqrt(epsr);         
W = lambda /sqrt(epsr);

theta = linspace(eps, pi, 361);
phi = linspace(eps, 2*pi, 361);
[TH,PH] = meshgrid(theta,phi);

P1 = k*W*sin(TH).*sin(PH)/2;
P2 = k*L*sin(TH).*cos(PH)/2;

E_theta = (sin(P1)./(P1+1e-6)) .*cos(P2).*cos(PH) ;
E_phi = (sin(P1)./(P1+1e-6)).*cos(P2).*cos(TH).*sin(PH);

RP = sqrt(abs(E_theta).^2 + abs(E_phi).^2);   
RP_dB = 20*log10(abs(RP));
TH_deg = rad2deg(TH); 
PH_deg = rad2deg(PH);

patternCustom(RP_dB(:),TH_deg(:), PH_deg(:))
clim([-30 0]);


U = abs(RP).^2;
Umax = max(U(:)); 
dtheta = theta(2) - theta(1);
dphi = phi(2) - phi(1);
Prad = sum(U .* sin(TH), "all") * dtheta * dphi;
D = 4*pi*Umax/Prad;
D_dB = 10*log10(D);
fprintf('Directivity (dB): %.3f dB\n', D_dB);

