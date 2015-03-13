----------------------------------------------------------------------------------------------
 MEMORY_TEST is a C++ program which declares and uses a sequence of larger and larger arrays, to see what the memory limits are on a given computer.
The program tries an increasing series of values of N, using powers of 2, between limits that you set. At some point, the program may ask for more memory than can be provided, and crash. This is one way to find out what the memory ceiling is!
 Usage:
    memory_test log_n_min log_n_max 

runs the program for sizes N = 2log_n_min to 2log_n_max. 
