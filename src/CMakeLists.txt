add_library(src OBJECT src.cpp)
target_include_directories(src PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
# target_compile_options(src PRIVATE -fprofile-arcs -ftest-coverage)
