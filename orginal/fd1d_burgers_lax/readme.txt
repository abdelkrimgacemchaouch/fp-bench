----------------------------------------------------------------------------------------------
 FD1D_BURGERS_LAX is a C++ program which solves the nonviscous time-dependent Burgers equation using finite differences and the Lax-Wendroff method.

The function u(x,t) is to be solved for in the equation:

    du/dt + u * du/dx = 0 

for a <= x <= b and t_init <= t <= t_last.

Problem data includes an initial condition for u(x,t_init), and the boundary value functions u(a,t) and u(b,t).

The non-viscous Burgers equation can develop shock waves or discontinuities. 
