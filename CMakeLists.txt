cmake_minimum_required(VERSION 3.12)
project(travis-cpp-test)
set(CMAKE_CXX_STANDARD 14)

# setup conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# units
add_library(src OBJECT src.cpp)

# tests
enable_testing()

add_executable(testcase test.cpp $<TARGET_OBJECTS:src>)
target_link_libraries(testcase CONAN_PKG::gtest)
add_test(NAME testcase COMMAND $<TARGET_FILE:testcase>)
