* [manifest.json](#zqpdi)
* [logo.png](#pui04)
* [index.html](#gmbp0)

1. [Getting Started](/plugin-api/get-started)
# File Structure Overview

This article will provide a quick introduction to the files that may appear in a plugin project.

[PreviousYour First Plugin](/plugin-api/get-started/creating-your-first-plugin)[NextPlugin Types](/plugin-api/get-started/plugin-types)

Last updated 1 year ago

A plugin is an installation package that contains multiple files and can be directly distributed to users.

Copy
```
Plugin
├─ manifest.json
├─ logo.png
├─ index.html
└─ js
   └─ plugin.js
```

---

## manifest.json

This is a file that every plugin must have. It contains basic information about the plugin, such as the plugin's name, version, code entry point, etc. There are different configuration methods for different types of plugins. The following is the basic configuration for a "window plugin":

Copy
```
{
    "id": "LB5UL2P0Q9FFF",
    "version": "1.0.0",
    "name": "Hello World",
    "logo": "/logo.png",
    "keywords": ["keywrod1", "keywrod2"],
    "main":
    {
        "devTools": true,
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```

* `id` - Plugin ID
* `version` - Plugin Version
* `name` - Plugin Name
* `logo` - Plugin Logo
* `keywords` - Plugin Keyword, In addition to the plugin name, users can also use these keywords to quickly search for the plugin.
* `main` - Plugin Window main entry

  + `url` - Entry Page
  + `width` - Window Width
  + `height` - Window Height

**Note**: You can refer to [this article](/plugin-api/tutorial/manifest) to learn about all the configuration methods for manifest.json.

**Example code**:

<https://github.com/eagle-app/eagle-plugin-examples/tree/main/Window>

## logo.png

The logo field in the manifest.json corresponds to the plugin's icon, which will be used in the plugin list and the plugin center. Please provide an image with a resolution of 128 x 128 pixels. The icon should generally be in PNG format, as PNG provides the best support for transparency.

---

## index.html

The main field in the manifest.json corresponds to the entry file of the plugin program. When the plugin is executed, index.html will be loaded independently and run in a separate browser window.

![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fgit-blob-4c0b26edd3a41213207a8b086b7d3e328789be3d%252Fimage%2520%2811%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=3a3b477f&sv=2)