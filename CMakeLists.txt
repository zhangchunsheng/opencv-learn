cmake_minimum_required(VERSION 3.8)
project(opencv_learn)

include_directories(/usr/local/include)
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        cascade-classifier/objectDetection.cpp)

add_executable(opencv_learn ${SOURCE_FILES})