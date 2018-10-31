L_g=0.004 #length of glass in m
L_gap=0.01 #length og gap in m
T_inf1=20 #inner temperature in C
T_inf2=-10 #outer temperature
A=1.2 #area of wall in m2
h1=10 #convention heat transfer coefficient on the inner surface in W/m^2*C
h2=40 #on the outer surface
k_g=0.78 #conductivity in W/m*C
k_gap=0.026

R_conv1=1/(h1*A)
R_conv2=1/(h2*A)
R_g=L_g/(k_g*A)
R_gap=L_gap/(k_gap*A)
R_tot=R_conv1+R_conv2+2*R_g+R_gap
Q=(T_inf1-T_inf2)/R_tot #steady rate of heat transfer in W
T1=20-Q*R_conv1 #temperature of window inner surface in K
