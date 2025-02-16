* [onPluginCreate(callback)](#gylpl)
* [onPluginRun(callback)](#gylpl-1)
* [onPluginBeforeExit(callback)](#z1a5y)
* [onPluginShow(callback)](#w2vxi)
* [onPluginHide(callback)](#zgvst)
* [onLibraryChanged(callback)](#g3tny)
* [onThemeChanged(callback)](#xlf6z)

1. [API Reference](/plugin-api/api)
# event

You can define some callback functions in advance according to your needs, and Eagle will actively call them when events occur.

## onPluginCreate(callback)

When the plugin window is created, Eagle will actively call this method. You can use this method to initialize the modules required by the plugin.

* `callback` Function

  + `plugin` Object - Plugin attributes

    - `manifest` Object - The complete configuration of the plugin's manifest.json.
    - `path` String - The path where the plugin is located

Copy
```
eagle.onPluginCreate((plugin) => {
    console.log(plugin.manifest.name);
    console.log(plugin.manifest.version);
    console.log(plugin.manifest.logo);
    console.log(plugin.path);
});
```

Tip: If the plugin can run without manifest information, you can also use `window.onload` for development.

## onPluginRun(callback)

When the user clicks on the plugin in the plugin panel, Eagle will actively call this method.

* `callback` Function

Copy
```
eagle.onPluginRun(() => {
    console.log('eagle.onPluginRun');
});
```
## onPluginBeforeExit(callback)

Before the plugin window closes, Eagle will actively call this method.

* `callback` Function

Copy
```
eagle.onPluginBeforeExit(() => {
    console.log("Plugin will exit");
});
// Prevent window from closing
window.onbeforeunload = (event) => {
    return event.returnValue = false;
};
```

Tip: If you want to prevent the window from being closed, you can register the `window.onbeforeunload` method to avoid the window being closed.

## onPluginShow(callback)

When the plugin window is displayed, Eagle will actively call this method.

* `callback` Function

Copy
```
eagle.onPluginShow(() => {
    console.log("Plugin window displayed");
});
```
## onPluginHide(callback)

When the plugin window is hidden, Eagle will actively call this method.

* `callback` Function

Copy
```
eagle.onPluginHide(() => {
    console.log("Plugin window hidden");
});
```
## onLibraryChanged(callback)

When the user switches the resource library, Eagle will actively call this method.

* `callback` Function

  + `libraryPath` String - The current resource library path.

Copy
```
eagle.onLibraryChanged((libraryPath) => {
    console.log(`Resource library switch detected, new resource library path: ${libraryPath}`);
});
```

Tip: If you need to get more complete information about the resource library, you can use the `eagle.library.info()` method to obtain it.

**Note:** If the plugin execution process must rely on a relative resource library path, you may need to register this method and make corresponding adjustments when the resource library changes to avoid errors during program execution.

## onThemeChanged(callback)

When the main program theme color of Eagle changes, Eagle will actively call this method. If the plugin supports multiple color themes, you can use this method to make corresponding UI adjustments.

* `callback` Function

  + `theme` String - The name of the current theme color, such as `Auto`, `LIGHT`, `LIGHTGRAY`, `GRAY`, `DARK`, `BLUE`, `PURPLE`.

Copy
```
eagle.onThemeChanged((theme) => {
    console.log(`Color theme has changed to: ${theme}`);
});
```
###

[PreviousFrameless Window](/plugin-api/tutorial/frameless-window)[Nextitem](/plugin-api/api/item)

Last updated 1 year ago