set(COVERAGE_LINK_FLAGS "-lgcov -coverage")

# tests
add_executable(testcase test.cpp $<TARGET_OBJECTS:src>)
target_include_directories(testcase PRIVATE $<TARGET_PROPERTY:src,INTERFACE_INCLUDE_DIRECTORIES>)
target_link_libraries(testcase CONAN_PKG::gtest)
set_target_properties(testcase PROPERTIES LINK_FLAGS "${COVERAGE_LINK_FLAGS}")
add_test(NAME testcase COMMAND $<TARGET_FILE:testcase>)
