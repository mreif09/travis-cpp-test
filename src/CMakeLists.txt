if(BUILD_TESTS)
    add_compile_options(-fprofile-arcs -ftest-coverage)
endif()

# units
add_library(src OBJECT src.cpp)
target_include_directories(src PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

#lib
add_library(mytest $<TARGET_OBJECTS:src>)
