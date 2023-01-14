function cppBuildAndTest()
{
    rm -rf build
    mkdir build
    cd build
    cmake .. && make && make test
    cd ..
    rm -rf build
}

#Runs all python tests
python3 -m pytest

# From_python tests
#Runs tests on generated oop C++ code
cd generated/from_python/oop
cppBuildAndTest

#Runs tests on generated procedural C++ code
cd ../procedural
cppBuildAndTest

cd ../../from_drawio/procedural
cppBuildAndTest
