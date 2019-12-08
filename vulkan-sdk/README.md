# vulkan-sdk

This dependency contains the Vulkan headers and libraries.

# Building on Windows

You will need to [install the Windows Driver Kit](https://docs.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk).
It's possible that you will also need Spectre-mitigated libraries which you can download with the Visual Studio Installer.

# Building on Linux

You will need to install some libraries:

+ libwayland
+ libx11-xcb
+ libxrandr

On Ubuntu, you can install all these packages by running
```
sudo apt-get install libx11-xcb-dev libxkbcommon-dev libwayland-dev libxrandr-dev
```

