function(add_gtest target)
    set(multiValueArgs FILES UNITS)
    cmake_parse_arguments(PARAM "" "" "${multiValueArgs}" ${ARGN})

    add_executable(${target} "")

    foreach(file ${PARAM_FILES})
        target_sources(${target} PRIVATE ${file})
    endforeach()

    foreach(unit ${PARAM_UNITS})
        target_sources(${target} PRIVATE $<TARGET_OBJECTS:${unit}>)
        target_include_directories(${target} PRIVATE $<TARGET_PROPERTY:${unit},INTERFACE_INCLUDE_DIRECTORIES>)
    endforeach()

    target_link_options(${target} PRIVATE -lgcov -coverage)
    target_link_libraries(${target} CONAN_PKG::gtest)

    add_test(NAME ${target} COMMAND $<TARGET_FILE:${target}>)
endfunction()
