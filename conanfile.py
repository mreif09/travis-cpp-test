from conans import ConanFile, CMake

class TestConan(ConanFile):
    name = "test"
    version = "0.2"
    license = "test"
    url = "https://github.com/mreif09/travis-cpp-test"
    description = "test for c++, cmake, conan and travis"
    settings = "os", "compiler", "build_type", "arch"
    build_requires = "gtest/1.11.0"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = {"gtest:shared": True, "shared": False}
    exports_sources = "CMakeLists.txt", "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(defs={'BUILD_TESTS': 'OFF'})
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mytest"]
