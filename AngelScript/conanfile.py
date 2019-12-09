from conans import ConanFile, CMake, tools


class AngelscriptConan(ConanFile):
    name = "AngelScript"
    version = "2.33"
    license = "zlib"
    url = "https://github.com/CytopiaTeam/conan-packages.git"
    description = "AngelScript is an extremely flexible cross-platform scripting library designed to allow applications to extend their functionality through external scripts."
    settings = ("os", "build_type", "arch_build")
    generators = "cmake"
    exports_sources = "cmake*", "include*", "source*", "CMakeLists.txt", "angelscript.pc.in"

    def source(self):
        self.run('git clone https://github.com/AnotherFoxGuy/angelscript.git')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder='angelscript')
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
