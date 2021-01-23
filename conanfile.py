from conans import ConanFile, CMake

class TestConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   build_requires = "gtest/1.10.0"
   generators = "cmake"
   default_options = {"gtest:shared": True}
