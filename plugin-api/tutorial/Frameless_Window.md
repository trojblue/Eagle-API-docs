* [Create a Borderless Window​](#create-a-borderless-window)
* [Draggable Area](#ke-tuo-ye-qu)

1. [Developer Guide](/plugin-api/tutorial)
# Frameless Window

Open a window without toolbars, borders, and other graphical shells.

A borderless window is a special type of window mode that does not have a shell (including window borders, title bars, toolbars, etc.), containing only the web content. Using a borderless window mode allows you to fully customize the window interface, making your application look consistent across all operating systems. However, since borderless windows do not have a system-provided shell, care must be taken while using them to avoid affecting the user experience.

## Create a Borderless Window​

In the `manifest.json` file, set the `frame` property of the `window` object to `false` to enable borderless window mode.

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
        "frame": false,        // 👈 Borderless mode
        "url": "index.html",
        "width": 640,
        "height": 480
    }
}
```
## Draggable Area

You can use the `-webkit-app-region` property in your application to control the draggable area of the application window.

By default, borderless windows are non-draggable. The application needs to specify `-webkit-app-region: drag` in CSS to tell the plugin which areas are draggable (like standard title bars of the operating system). Use `-webkit-app-region: no-drag` within the draggable area to exclude some parts. Please note that currently only rectangular shapes are supported.

To make the entire window draggable, you can add `-webkit-app-region: drag` as the `body` style:

Copy
```
<body style="-webkit-app-region: drag">
</body>
```

Please note that if you make the entire window draggable, you must mark the buttons inside as not draggable, otherwise users will not be able to click on them:

Copy
```
button {
  -webkit-app-region: no-drag;
}
```

If you only set the custom title bar to be draggable, you also need to make all the buttons within the title bar non-draggable.

[PreviousMultilingual (i18n)](/plugin-api/tutorial/i18n)[Nextevent](/plugin-api/api/event)

Last updated 1 year ago