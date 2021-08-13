python3 -m pytest
cd generated/oop
rm -rf build
mkdir build
cd build
cmake .. && make && make test
