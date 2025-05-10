% Parameters
    N = 8;                  
    f = 15e9;               
    c = 3e8;                
    lambda = c / f;         
    d = lambda / 2;         
    k0 = 2*pi / lambda;
    
    theta0 = 0;
    phi0 = 0;
    
    %Coordinatos
    theta = linspace(eps, pi, 361);
    phi = linspace(eps, 2*pi, 361);
    
    [TH,PH] = meshgrid(theta,phi);
    
    %Chebychev window
    coeff = chebwin(N,40);
    stem(coeff)
    
    %Wavenumbers
    kx_0 = k0*sin(theta0).*cos(phi0);
    ky_0 = k0*sin(theta0).*sin(phi0);
    kx = k0*sin(TH).*cos(PH);
    ky = k0*sin(TH).*sin(PH);
    
    AF_uniform = zeros(size(TH));
    AF = zeros(size(TH));
    
    for n = 0:N-1
        AF = AF + coeff(n+1) * exp(1j*n*d*(ky-ky_0));
    end
    
    for n = 0:N-1
        AF_uniform = AF_uniform + exp(1j*n*d*(ky-ky_0));
    end
    
    %Converting
    TH_deg = rad2deg(TH); 
    PH_deg = rad2deg(PH);
    
    %Plotting
    AF_mag_dB = 20*log10(abs(AF));
    AF_mag_dB = AF_mag_dB - max(AF_mag_dB(:)); 
    patternCustom(AF_mag_dB(:),TH_deg(:),PH_deg(:))
    
    AF_uniform_mag_dB = 20*log10(abs(AF_uniform));
    AF_uniform_mag_dB = AF_uniform_mag_dB - max(AF_uniform_mag_dB(:));  
    patternCustom(AF_uniform_mag_dB(:),TH_deg(:),PH_deg(:))
    
    
    % patternCustom(AF_mag_dB(:),TH_deg(:),PH_deg(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(phi()));
    % hold on
    % patternCustom(AF_uniform_mag_dB(:),TH_deg(:),PH_deg(:),CoordinateSystem="rectangular", Slice="phi", SliceValue=rad2deg(eps));
    % hold off
    
    %Compute Directivity
    
    %Weighted
    U = abs(AF).^2;
    Umax = max(U(:)); 
    Prad = trapz(phi, trapz(theta, U.*sin(TH), 2));
    D = 4*pi*Umax/Prad;
    D_dB = 10*log10(abs(D));
    fprintf('Directivity weighted (dB): %.3f dB\n', D_dB);
    
    %Uniform
    U_uniform = abs(AF_uniform).^2;
    Umax_uniform = max(U_uniform(:));
    Prad_uniform = trapz(phi, trapz(theta, U_uniform.*sin(TH), 2));
    D_uniform = 4*pi*Umax_uniform/Prad_uniform;
    D_uniform_dB = 10*log10(abs(D_uniform));
    fprintf('Directivity uniform (dB): %.3f dB\n', D_uniform_dB);