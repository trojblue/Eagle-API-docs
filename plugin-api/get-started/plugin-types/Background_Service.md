1. [Getting Started](/plugin-api/get-started)
3. [Plugin Types](/plugin-api/get-started/plugin-types)
# Background Service

This article will describe the basic concepts of background service plugins.

The development of background service plugins is similar to [window plugins](/plugin-api/get-started/plugin-types/window), with the main difference being the timing of code execution. Background service plugins will automatically start when the software starts, while window plugins will only execute when the user clicks on them. To create a background service plugin, simply add `"serviceMode": true` to the `main` field in the `manifest.json`, as shown below:

Copy
```
{
    "main":
    {
        "serviceMode": true,    // main difference
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```

Background service plugins can also pop up windows, in which you can display the progress and status of the current background task, allowing users to clearly understand the current state of the plugin.

The final code is as follows:

manifest.jsonindex.htmlplugin.jsCopy
```
{
    "id": "LBCZEHP8BBO94",
    "version": "1.0.0",
    "name": "Service Plugin",
    "logo": "/logo.png",
    "keywords": [],
    "main":
    {
        "serviceMode": true,
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```
Copy
```

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
    <script type="text/javascript" src="js/plugin.js"></script>
</head>
<body>
    <div>Background services can be without UI, but you can still display the status of background services here.</div>
</body>
</html>
```
Copy
```
console.log(`Plugins will be created automatically, no need for users to execute them.`);
eagle.onPluginCreate((plugin) => {
    console.log('eagle.onPluginCreate');
    console.log(plugin);
});
eagle.onPluginShow(() => {
    console.log('eagle.onPluginShow');
});
eagle.onPluginHide(() => {
    console.log('eagle.onPluginHide');
});
```

**Complete example code**:

<https://github.com/eagle-app/eagle-plugin-examples/tree/main/Service>

Note: You can refer to [this article](/plugin-api/tutorial/manifest) to learn about all the configuration methods for manifest.json

**Note:** If the plugin execution process relies on a relative resource library path, you may need to use [`onLibraryChanged(callback)`](/plugin-api/api/event#g3tny) to make corresponding adjustments when the resource library switches, avoiding errors during the program execution.

[PreviousWindow](/plugin-api/get-started/plugin-types/window)[NextFormat Extension](/plugin-api/get-started/plugin-types/preview)

Last updated 1 year ago