cmake_minimum_required(VERSION 3.10)
project(insertion_sort)

set(CMAKE_CXX_STANDARD 23)

# Source files
set(SOURCES
    main.cpp
    insertion_sort.cpp
)

add_executable(main ${SOURCES})
