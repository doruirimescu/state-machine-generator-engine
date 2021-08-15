
rm -rf tests/test_files/oop/include
cp -r generated/oop/include/ tests/test_files/oop

rm -rf tests/test_files/oop/src
cp -r generated/oop/src/ tests/test_files/oop

rm -rf tests/test_files/procedural/include
cp -r generated/procedural/include/header.h tests/test_files/procedural/include

rm -rf tests/test_files/procedural/src
cp -r generated/procedural/src tests/test_files/procedural/src
