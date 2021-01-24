if(BUILD_TESTS)
    set(COVERAGE_COMPILE_FLAGS "-fprofile-arcs -ftest-coverage -DGCOV_ACTIVE")
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS} ${COVERAGE_COMPILE_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${COVERAGE_COMPILE_FLAGS}")
endif()

# units
add_library(src OBJECT src.cpp)
target_include_directories(src PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

#lib
add_library(mytest $<TARGET_OBJECTS:src>)
