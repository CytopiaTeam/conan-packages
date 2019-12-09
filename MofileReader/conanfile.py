from conans import ConanFile, CMake, tools
import os

class MofilereaderConan(ConanFile):
    name = "MofileReader"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/Cytopia/conan-packages.git"
    description = "This API lets you read .mo-Files and use their content just as you would do with GNUs gettext."
    settings = ("os", "build_type", "arch_build")
    exports_sources = "include*", "src*", "CMakeLists.txt"

    def source(self):
        self.run('git clone https://github.com/AnotherFoxGuy/MofileReader.git')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder='MofileReader')
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
