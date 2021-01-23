cmake_minimum_required(VERSION 3.12)
project(travis-cpp-test)
set(CMAKE_CXX_STANDARD 14)

# setup conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# units
add_subdirectory(src)

# tests
enable_testing()
add_subdirectory(test)
