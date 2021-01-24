cmake_minimum_required(VERSION 3.12)
project(PackageTest C CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(package_test package_test.cpp)
target_link_libraries(package_test ${CONAN_LIBS})

enable_testing()
add_test(NAME package_test
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND package_test)
