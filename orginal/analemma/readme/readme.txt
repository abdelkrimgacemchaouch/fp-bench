 ANALEMMA is a C++ program which evaluates the equation of time, by Brian Tung.

The program can compute and plot an analemma curve for various orbital parameters. The analemma is the curve traced by the position of the sun, measured at clock noon, over a year.

The program creates data and command files which must be processed by the GNUPLOT program:

        gnuplot < analemma_commands.txt
      

which will create PNG images of the analemma, the declination, and the equation of time. 
 Author:

Original C version by Brian Tung. C++ version by John Burkardt.
Reference:

    Brian Tung,
    Figure Eight in the Sky, a new perspective on an old fascination,
    Astronomical Games, August 2002,
    http://www.astronomycorner.net/games/analemma.html.

