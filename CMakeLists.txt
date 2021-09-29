cmake_minimum_required(VERSION 3.12)
project(travis-cpp-test)
set(CMAKE_CXX_STANDARD 14)

# configuration
option(BUILD_TESTS "Build tests and switch on gcov coverage" ON)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/tools/cmake")

# setup conan
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# lib
add_subdirectory(src)

# tests
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(test)
endif()
