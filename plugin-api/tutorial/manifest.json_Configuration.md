1. [Developer Guide](/plugin-api/tutorial)
# manifest.json Configuration

In this article, we will provide a detailed explanation of all the supported fields in the manifest.json file for an Eagle plugin.

Each plugin must include a `manifest.json` file. This file defines the plugin's execution method and basic information such as the plugin's name, version number, and entry point for the execution code.

A complete configuration for a `manifest.json` file might look like this:

Copy
```
{
    "id": "LBCZE8V6LPCKD",
    "version": "1.0.0",
    "platform": "all",
    "arch": "all",
    "name": "Windows Plugin",
    "logo": "/logo.png",
    "keywords": [],
    "devTools": false,
    "main":
    {
        "url": "index.html",
        "width": 640,
        "height": 480,
        "minWidth": 640,
        "minHeight": 480,
        "maxWidth": 640,
        "maxHeight": 480,
        "alwaysOnTop": false,
        "frame": true,
        "fullscreenable": true,
        "maximizable": true,
        "minimizable": true,
        "resizable": true,
        "backgroundColor": "#ffffff",
        "multiple": false,
        "runAfterInstall": false
    }
}
```
## Example of each field in the `manifest.json` file for a plugin:

* `id` - Plugin ID
* `version` - Plugin Version
* `platform` - Support Platform

  + `all` - Support All Platforms
  + `mac` - macOS only
  + `win` - Windows OS only
* `arch` - CPU Architectures

  + `all` - Support All Architectures
  + `arm` - only support `arm` architecture
  + `x64` - only support `x64` architecture
* `name` - Plugin Name
* `logo` - Plugin Logo File (only support `png`, `jpg`, `webp` format)
* `keywords` - Plugin Keywords, In addition to the plugin name, adding "keywords" can help users quickly find the plugin when searching.
* `devTools` - To open the developer debug window for your plugin, you need to specify this setting.
* `main` - Plugin main entry configuration

  + `url` - Entry Page
  + `width` - Window width
  + `height` - Window height
  + `minWidth` - Window min-width
  + `minHeight` - Window min-height
  + `maxWidth` - Window max-width
  + `maxHeight` - Window max-height
  + `alwaysOnTop` - Whether the window is always on top of other windows, default value is `false`.
  + `frame` - Default value is `true`. When set to `false`, a [frameless window](/plugin-api/tutorial/frameless-window) is used. This is a special window mode that does not have an outer shell (including window border, title bar, toolbar, etc.) and only contains web page content.
  + `fullscreenable` - Whether the window can enter fullscreen mode, default value is `true`.
  + `maximizable` - Whether the window can be maximized, default value is `true`.
  + `minimizable` - Whether the window can be minimized, default value is `true`.
  + `resizable` - Whether the window size can be adjusted, default value is `true`.
  + `backgroundColor` - Window background color, default value is `#FFF`.
  + `multiple` - Whether the window can be opened multiple times, default value is `false`.
  + `runAfterInstall` - Automatically opens after installation, default value is `false`.

[PreviousDeveloper Policies](/plugin-api/distribution/developer-policies)[NextRetrieve Data](/plugin-api/tutorial/get-eagle-data)

Last updated 8 months ago