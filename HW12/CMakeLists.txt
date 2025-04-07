CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
PROJECT(dynamic_array)

set(CMAKE_CXX_STANDARD 23)

set(SOURCES
    dynamic_array.cpp
)

ADD_EXECUTABLE(dynamic_array ${SOURCES})
