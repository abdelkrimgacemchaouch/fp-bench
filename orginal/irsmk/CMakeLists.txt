cmake_minimum_required(VERSION 2.8)
enable_language (C Fortran)
file(GLOB g 
"src/*.h" "src/*.c" )
add_executable(be ${g})
target_link_libraries(be m) #pour les bibiotheque mathematique
