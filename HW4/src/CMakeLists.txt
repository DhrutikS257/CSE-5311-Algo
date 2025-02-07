cmake_minimum_required(VERSION 3.10)
project(HW4)

set(CMAKE_CXX_STANDARD 23)

set(SOURCES 
    problem1.cpp
    problem2.cpp
)

foreach(SourceFile ${SOURCES})
    get_filename_component(ExeName ${SourceFile} NAME_WE)

    add_executable(${ExeName} ${SourceFile})
endforeach()


