from conans import ConanFile, CMake, tools


class VulkansdkConan(ConanFile):
    name = "vulkan-sdk"
    version = "1.1.126"
    license = "Apache 2.0"
    author = "Vincent-Olivier Roch <vroch@edu.uwaterloo.ca>"
    url = "https://github.com/CytopiaTeam/conan-vulkan-sdk"
    description = "LunarG's Vulkan SDK"
    topics = ("vulkan", "gpu", "graphics")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run(f'git clone https://github.com/KhronosGroup/Vulkan-Headers.git -b sdk-{self.version}')
        self.run(f'git clone https://github.com/KhronosGroup/Vulkan-Loader.git -b sdk-{self.version}')

    def build(self):
        cmake = CMake(self)
        cmake.configure(
                source_folder='Vulkan-Headers',
                build_folder='Vulkan-Headers',
                defs={ 'CMAKE_INSTALL_PREFIX': '../headers_install' })
        cmake.install()
        cmake.configure(
                source_folder='Vulkan-Loader',
                build_folder='Vulkan-Loader',
                defs={ 'VULKAN_HEADERS_INSTALL_DIR': '../headers_install' })
        cmake.install()

    def package(self):
        self.copy("LICENSE.txt", dst="license", src='Vulkan-Headers')
        self.copy(f"include/*", src="Vulkan-Headers")

    def package_info(self):
        self.cpp_info.libs = ["vulkan"]
