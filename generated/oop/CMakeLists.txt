cmake_minimum_required(VERSION 3.14)

project(STATE_MACHINE VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")
include(CTest)
include(FetchContent)
FetchContent_Declare(
                    googletest
                    # Specify the commit you depend on and update it regularly.
                    URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
                    )
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

FILE(GLOB SOURCES src/*.cpp)

set(LIBRARY_NAME state_machine_generator)  # Default name for the library built from src/*.cpp (change if you wish)

add_library(${LIBRARY_NAME} OBJECT ${SOURCES})

target_include_directories(${LIBRARY_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include)

include_directories(${PROJECT_SOURCE_DIR}/include)



enable_testing()

FILE(GLOB TESTFILES test/*.cpp)

set(TEST_MAIN unit_tests)   # Default name for test executable (change if you wish).
add_executable(${TEST_MAIN} ${TESTFILES} ${SOURCES})
target_link_libraries(${TEST_MAIN} gtest_main)

add_test(
    # Use some per-module/project prefix so that it is easier to run only tests for this module
    NAME ${LIBRARY_NAME}.${TEST_MAIN}
    COMMAND ${TEST_MAIN} ${TEST_RUNNER_PARAMS})
