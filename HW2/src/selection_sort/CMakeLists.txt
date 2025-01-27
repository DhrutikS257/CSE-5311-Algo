cmake_minimum_required(VERSION 3.10)
project(selection_sort)

set(CMAKE_CXX_STANDARD 23)

# Source files
set(SOURCES
    main.cpp
    selection_sort.cpp
)

add_executable(main ${SOURCES})
