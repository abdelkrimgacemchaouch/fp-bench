 FD_PREDATOR_PREY is a C program which applies the finite difference method to estimate solutions of a pair of ordinary differential equations that model the behavior of a pair of predator and prey populations.

The physical system under consideration is a pair of animal populations.

The PREY reproduce rapidly; for each animal alive at the beginning of the year, two more will be born by the end of the year. The prey do not have a natural death rate; instead, they only die by being eaten by the predator. Every prey animal has 1 chance in 1000 of being eaten in a given year by a given predator.

The PREDATORS only die of starvation, but this happens very quickly. If unfed, a predator will tend to starve in about 1/10 of a year. On the other hand, the predator reproduction rate is dependent on eating prey, and the chances of this depend on the number of available prey.

The resulting differential equations can be written:

        PREY(0) = 5000
        PRED(0) =  100

        d PREY / dT =    2 * PREY(T) - 0.001 * PREY(T) * PRED(T)
        d PRED / dT = - 10 * PRED(T) + 0.002 * PREY(T) * PRED(T)
      

Here, the initial values (5000,100) are a somewhat arbitrary starting point.

The pair of ordinary differential equations that result have an interesting behavior. For certain choices of the interaction coefficients (such as those given here), the populations of predator and prey will tend to a periodic oscillation. The two populations will be out of phase; the number of prey will rise, then after a delay, the predators will rise as the prey begins to fall, causing the predator population to crash again.

In this program, the pair of ODE's is solved with a simple finite difference approximation using a fixed step size. In general, this is NOT an efficient or reliable way of solving differential equations. However, this program is intended to illustrate the ideas of finite difference approximation.

In particular, if we choose a fixed time step size DT, then a derivative such as dPREY/dT is approximated by:

        d PREY / dT = approximately ( PREY(T+DT) - PREY(T) ) / DT
      

which means that the first differential equation can be written as

        PREY(T+DT) = PREY(T) + DT * ( 2 * PREY(T) - 0.001 * PREY(T) * PRED(T) ).
      

We can rewrite the equation for PRED as well. Then, since we know the values of PRED and PREY at time 0, we can use these finite difference equations to estimate the values of PRED and PREY at time DT. These values can be used to get estimates at time 2*DT, and so on. To get from time T_START = 0 to time T_STOP = 5, we simply take STEP_NUM steps each of size

        DT = ( T_STOP - T_START ) / STEP_NUM
      

Because finite differences are only an approximation to derivatives, this process only produces estimates of the solution. And these estimates tend to become more inaccurate for large values of time. Usually, we can reduce this error by decreasing DT and taking more, smaller time steps.

In this example, for instance, taking just 100 steps gives nonsensical answers. Using STEP_NUM = 1000 gives an approximate solution that seems to have the right kind of oscillatory behavior, except that the amplitude of the waves increases with each repetition. Using 10000 steps, the approximation begins to become accurate enough that we can see that the waves seem to have a fixed period and amplitude.
Usage:

    fd_predator_prey step_num 

where

    step_num is the number of time steps to take.

