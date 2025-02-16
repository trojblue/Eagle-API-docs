* [Window Plugin Debug](#zqpdi)
* [Debug Thumbnail Plugin](#debug-thumbnail-plugin)
* [Debug Preview Plugin](#debug-preview-plugin)
* [Log System](#pui04)

1. [Getting Started](/plugin-api/get-started)
# Debug Plugin

This article will provide a detailed explanation of effective methods for debugging and troubleshooting Eagle plugins.

[PreviousInspector](/plugin-api/get-started/plugin-types/inspector)[NextPrepare Plugin](/plugin-api/distribution/prepare)

Last updated 7 months ago

## Window Plugin Debug

After opening the plugin, press the F12 key to open the DevTools debugging tool.

The specific steps are as follows:

2. Open the plugin you want to debug in Eagle, and press the F12 key to open DevTools.
5. In DevTools, you can view the plugin's code and use breakpoints and debugging tools to debug the plugin's execution process.
8. You can also use other tools in DevTools to view information about the plugin's performance, memory usage, etc.

## Debug Thumbnail Plugin

The thumbnail plugin runs in the background, and the code is only executed when files are added or updated. If you want to debug the thumbnail function code, you can set the devTools property to true in the manifest.json file and set debugger breakpoints in the code, which can then be debugged using devTools.

## Debug Preview Plugin

Add and select the file format you want to develop in Eagle, open the plugin panel, click on the plugin you're developing, and a separate preview window will open. You can press `F12` to open `DevTools` for debugging.

Learn more: If you are unsure how to use DevTools, you can refer to the following learning resources:

2. Google official documentation: <https://developers.google.com/web/tools/chrome-devtools>
5. MDN Web documentation: <https://developer.mozilla.org/zh-CN/docs/Tools>
8. W3Schools tutorial: <https://www.w3schools.com/js/js_debugging.asp>

## Log System

Please note: The preview and thumbnail plugins currently do not support the log API.

A logging system is a tool used to record the running status of software, helping developers to locate and solve problems more quickly. The logging system records software error information, warning information, runtime information, etc., and can be used as a debugging tool. In a non-development environment, the logging system effectively helps developers identify the causes of problems and take measures to solve them.

Eagle Plugin API provides a [log functionality](/plugin-api/api/log) to record plugin runtime information. This way, developers can record the plugin's running, warnings, errors, and other information in Eagle's software logs. By using this feature, developers can view this information by only providing a debug report to the user. While developing plugins, the logging feature helps developers to quickly locate and solve problems.

Copy
```
eagle.log.debug('debug message from plugin');
eagle.log.info('info message from plugin');
eagle.log.warn('warn message from plugin');
eagle.log.error('error message from plugin');
// [13:19:39.845] [debug] [plugin] "debug message from plugin"
// [13:19:39.845] [info] [plugin] "info message from plugin"
// [13:19:39.845] [warn] [plugin] "warn message from plugin"
// [13:19:39.845] [error] [plugin] "error message from plugin"
```

Learn More: [Log - API Reference](/plugin-api/api/log)

Click here to view Eagle's [software log](https://docs-cn.eagle.cool/article/92-how-do-i-get-the-error-log) acquisition method.

DevTools

![](https://developer.eagle.cool/~gitbook/image?url=https%3A%2F%2F1590693372-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8ag8XBIM3olHOU7WmBBx%252Fuploads%252FMGg6WE08zUPf91TNYj4H%252Fimage.png%3Falt%3Dmedia%26token%3D744097d1-6a51-4c21-afbb-e726cc3811c6&width=768&dpr=4&quality=100&sign=6fc3c95c&sv=2)