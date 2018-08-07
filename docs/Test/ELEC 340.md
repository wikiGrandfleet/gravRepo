##### ELEC 340
Applied Electromagnetics

* Used textbooks 
* [Introduction to Engineering Electromagnetics](Textbooks/Extra/6wfa1.Introduction.to.Engineering.Electromagnetics)


Midterm for 2014 ELEC 340
```octave
%% ELEC 340 Midterm Prep
u = symunit
format compact
%%  Midterm 2014
%%
% In wet soil, characterized by $/sigma=10^{-2}S/m$ , $/mu_r=1$, and $/epsilon_r=36$, at what frequency is
% the conduction current density equal in magnitude to the displacement current density?
sigma = 1e-2/(u.ohm*u.m)
epsr = 36
eps0 = 8.854187817*1e-12*u.F/u.m
mur  = 1
eps = epsr*eps0
%%
% $/tilde{J}_c = /sigma /mathbf{/tilde{E}}$
%%
% $/tilde{J}_d = j /omega /mathbf{/tilde{D}}= j /omega /epsilon /mathbf{/tilde{E}}$

f = sigma/(2*pi*eps);
f = rewrite(f,u.Hz);
fVal = vpa(f,10)
```

