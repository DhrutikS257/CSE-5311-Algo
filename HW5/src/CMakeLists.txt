cmake_minimum_required(VERSION 3.10)
project(HW5)

set(CMAKE_CXX_STANDARD 23)

set(SOURCES 
    min_heap.cpp
)

foreach(SourceFile ${SOURCES})
    get_filename_component(ExeName ${SourceFile} NAME_WE)

    add_executable(${ExeName} ${SourceFile})
endforeach()


