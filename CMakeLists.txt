cmake_minimum_required(VERSION 3.12)
project(travis-cpp-test)
set(CMAKE_CXX_STANDARD 14)

add_library(src OBJECT src.cpp)

enable_testing()

add_executable(testcase test.cpp $<TARGET_OBJECTS:src>)
add_test(testcase testcase)
