1. [Getting Started](/plugin-api/get-started)
3. [Plugin Types](/plugin-api/get-started/plugin-types)
# Window

In this article, we will explain the basic concepts of window plugins.

[PreviousPlugin Types](/plugin-api/get-started/plugin-types)[NextBackground Service](/plugin-api/get-started/plugin-types/service)

Last updated 6 months ago

The vast majority of plugins should be developed using this method. It provides a browser window where you can develop the desired features, and this window will automatically pop up when the user clicks on the plugin.

We can set the window properties by setting the main field in the manifest.json file.

Copy
```
{
    "main": {}
}
```

Set the default open link URL for the window:

Copy
```
{
    "main": {
        "url": "index.html"
    }
}
```

Set the default width and height of the window:

Copy
```
{
    "main": {
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```

After setting other metadata.json fields, the final code is as follows:

manifest.jsonindex.htmlplugin.jsCopy
```
{
    "id": "LBCZE8V6LPCKD",
    "version": "1.0.0",
    "name": "Window Plugin",
    "logo": "/logo.png",
    "keywords": [],
    "main":
    {
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
    <div id="message"></div>
</body>
</html>
```
Copy
```
eagle.onPluginCreate((plugin) => {
    console.log('eagle.onPluginCreate');
    console.log(plugin);
    document.querySelector('#message').innerHTML = `
    <ul>
        <li>id: ${plugin.manifest.id}</li>
        <li>version: ${plugin.manifest.version}</li>
        <li>name: ${plugin.manifest.name}</li>
        <li>logo: ${plugin.manifest.logo}</li>
        <li>path: ${plugin.path}</li>
    </ul>
`;
});
eagle.onPluginShow(() => {
    console.log('eagle.onPluginShow');
});
eagle.onPluginHide(() => {
    console.log('eagle.onPluginHide');
});
eagle.onPluginBeforeExit((event) => {
    console.log('eagle.onPluginBeforeExit');
});
```

**Check out this sample code!**

Looking for inspiration? Come and explore our sample code; there's a wealth of exciting content waiting for you!

<https://github.com/eagle-app/eagle-plugin-examples/tree/main/Window>

**Sample code for Multilanguage + Multitheme**

For developers aiming to achieve multilanguage internationalization (i18n), this GitHub project is your best learning companion! Click the link below to explore how to cleverly combine i18n with multitheme design, adding a touch of magic to your application's multilanguage support.

[https://github.com/eagle-app/eagle-plugin-examples/tree/main/i18n+theme](https://github.com/eagle-app/eagle-plugin-examples/tree/main/i18n%2Btheme)

Note: You can refer to [this article](/plugin-api/tutorial/manifest) to learn about all the configuration methods for manifest.json

![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252Fgit-blob-b8d618997d0dc7e53df2a4b775bb0f4d21e25ed9%252Fimage%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=7eaa53c9&sv=2)