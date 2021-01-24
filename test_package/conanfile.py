import os

from conans import ConanFile, CMake, tools


class TestTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "gtest/1.10.0"
    default_options = {"gtest:shared": True}

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        cmake = CMake(self)
        cmake.test(output_on_failure=True)
