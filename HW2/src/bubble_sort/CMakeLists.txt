cmake_minimum_required(VERSION 3.10)
project(bubble_sort)

set(CMAKE_CXX_STANDARD 23)

# Source files
set(SOURCES
    main.cpp
    bubble_sort.cpp
)

add_executable(main ${SOURCES})
