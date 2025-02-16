1. [Getting Started](/plugin-api/get-started)
3. [Plugin Types](/plugin-api/get-started/plugin-types)
# Inspector

This article will explain the basic concepts of the inspector plugin.

Note: The inspector plugin requires Eagle version 4.0 Beta 17 or above.

You can develop an additional inspector tool for specific file formats. When a user selects a file of that format, they can directly use the plugin in the inspector on the right side. For example, an EXIF attribute inspector plugin can be developed for JPG/Raw files, allowing users to easily view additional data such as "shooting time, focal length, aperture, latitude and longitude" on the right side when they select such files.

The inspector plugin is actually a variant of the format extension plugin, and its definition method is very similar. The inspector plugin does not need to define the `main` attribute in `manifest.json`, but needs to set the `preview` attribute. Below is an example code:

Copy
```
{
    "preview": {}
}
```

In `preview`, you can define the file extensions you want to extend. For example, if you want to develop an additional plugin for jpg and png formats, you can enter `"jpg,png": {}`:

Copy
```
{
    "preview": {
        "jpg,png": {}
    }
}
```

Then set the following properties:

* `path`: The path to the HTML file of the plugin
* `height`: The default height of the plugin
* `multiSelect`: Whether to display when multiple selections are made (it is recommended to set to `false` unless in special cases)

Copy
```
{
    "preview": {
        "jpg,png": {
            "inspector": {
                "path": "index.html",
                "height": 100,
                "multiSelect": false
            }
        }
    }
}
```

After setting other fields in `metadata.json`, the final code is as follows:

manifest.jsonindex.htmlCopy
```
{
    "id": "cc41e899-5fc3-445c-a113-2d9573d6edcc",
    "version": "1.0.0",
    "platform": "all",
    "arch": "all",
    "name": "Inspector Plugin",
    "logo": "/logo.png",
    "keywords": [],
    "devTools": true,
    "preview": {
        "jpg,png": {
            "inspector": {
                "path": "index.html",
                "height": 100,
                "multiSelect": false
            }
        }
    }
}
```
Copy
```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Inspector Plugin Example</title>
    <style>
        html {
            font-size: 11px;
            font-family: sans-serif;
            border-radius: 6px;
            overflow: hidden;
        }
        body {
            padding: 0;
            margin: 0;
            color: transparent;
        }
        /* colors for different themes */
        body[theme="LIGHT"],
        body[theme="LIGHTGRAY"] {
            color: black;
        }
        body[theme="GRAY"],
        body[theme="BLUE"],
        body[theme="PURPLE"],
        body[theme="DARK"] {
            color: white;
        }
    </style>
</head>
<body>
    Inspector Plugin Example
    <script>
        // Listen to plugin creation
        eagle.onPluginCreate(async (plugin) => {
            // Get the current theme
            const theme = await eagle.app.theme;
            document.body.setAttribute('theme', theme);
            // Get the selected item
            const item = await eagle.item.getSelected();
            console.log(item);
            console.log(theme);
        });
        // Listen to theme changes
        eagle.onThemeChanged((theme) => {
            document.body.setAttribute('theme', theme);
        });
    </script>
</body>
</html>
```

**Complete example code:**
<https://github.com/eagle-app/eagle-plugin-examples/tree/main/Inspector>

### How to Debug Inspector Plugins

Debugging inspector plugins is simple. You can right-click on the inspector plugin in the screen and then select "Developer Tools" to start debugging.

[PreviousFormat Extension](/plugin-api/get-started/plugin-types/preview)[NextDebug Plugin](/plugin-api/get-started/debugging)

Last updated 10 months ago