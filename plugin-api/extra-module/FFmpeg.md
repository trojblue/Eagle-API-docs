* [Introduction to FFmpeg Dependency Plugin](#introduction-to-ffmpeg-dependency-plugin)
* [Installing the FFmpeg Dependency Plugin](#installing-the-ffmpeg-dependency-plugin)
* [How to Use the FFmpeg Dependency Plugin](#how-to-use-the-ffmpeg-dependency-plugin)
* [Window Plugin Example](#gylpl)
* [Thumbnail Plugin Example](#gylpl-1)

1. [Extra Moudle](/plugin-api/extra-module)
# FFmpeg

This plugin provides dependency support for FFmpeg, giving developers a wide range of image, video, and audio encoding and decoding capabilities.

Note: This feature can only be used in Eagle 4.0 beta 7 and above.

## Introduction to FFmpeg Dependency Plugin

The "FFmpeg Dependency Plugin" is a toolkit for browser plugin developers, encapsulating the powerful multimedia processing capabilities of FFmpeg into an easy-to-use dependency package. This toolkit allows developers to easily implement image, video, and audio format encoding and decoding, as well as advanced features such as streaming media processing and format conversion, in their own plugins. By integrating the "FFmpeg Dependency Plugin", developers can seamlessly expand the multimedia processing capabilities of their plugins, bringing more creative and practical features to users.

## Installing the FFmpeg Dependency Plugin

1. Enter the plugin center
2. Search and find the FFmpeg plugin
3. Click to install the FFmpeg plugin

Please note that when users install plugins with FFmpeg dependencies, Eagle will automatically prompt users to install the "FFmpeg Dependency Plugin". Therefore, developers do not need to specifically write code for users to install, just provide corresponding prompts for possible errors.

## How to Use the FFmpeg Dependency Plugin

If you want to use FFmpeg related functions in your plugin, you need to add a `dependencies` definition in the plugin's `manifest.json` file, so that the Eagle system knows that this plugin needs additional extension functions, as shown below:

Copy
```
{
    "id": "LBCZE8V6LPCKD",
    "version": "1.0.0",
    "platform": "all",
    "arch": "all",
    "name": "Window Plugin",
    "logo": "/logo.png",
    "keywords": [],
    "dependencies": ["ffmpeg"],
    "devTools": false,
    "main":
    {
        "url": "index.html",
        "width": 640,
        "height": 480,
    }
}
```
### Window Plugin Example

You can use `eagle.extraModule.ffmpeg` to call the functions provided by the FFmpeg dependency plugin, as shown below:

Copy
```
eagle.onPluginCreate(async (plugin) => {
    // Check if the FFmpeg dependency plugin is installed
    const isFFemptInstalled = await eagle.extraModule.ffmpeg.isInstalled();

    // Open the plugin center and pop up the FFmpeg dependency plugin installation page.
    if (!isFFemptInstalled) {
        await eagle.extraModule.ffmpeg.install();
        return;
    }

    // Get the location of the FFmpeg binary file
    const ffmpegPaths= await eagle.extraModule.ffmpeg.getPaths();
    const ffmpegBinaryPath = ffmpegPaths.ffmpeg;
    const ffprobeBinaryPath = ffmpegPaths.ffprobe;

    // Use the spwan command to perform related operations
    const spawn = require('child_process').spawn;
    const ffprobe = spawn(ffprobePath, [
	'-v', 'error',
	'-print_format', 'json',
	'-show_format',
	'-show_streams',
	"C:\\your_file.mp4"
    ]);
});
```
### Thumbnail Plugin Example

You can get FFmpeg related functions through the `extraModule` parameter, as shown below:

Copy
```

module.exports = async ({ src, dest, item, plugin, extraModule }) => {
    return new Promise(async (resolve, reject) => {
        try {

            const ffmpegModule = extraModule.ffmpeg;

            // Check if the FFmpeg dependency plugin is installed
            if (!ffmpegModule.isInstalled) {
		return reject(new Error(`ffmpeg is not installed.`));
	    }

            // Get the location of the FFmpeg binary file
            const { ffmpeg, ffprobe } = ffmpegModule.paths;

            // Use the spwan command to perform related operations
            const spawn = require('child_process').spawn;
            const ffprobe = spawn(ffprobePath, [
	        '-v', 'error',
        	'-print_format', 'json',
	        '-show_format',
	        '-show_streams',
	        "C:\\your_file.mp4"
            ]);

            return resolve(item);
        }
        catch (err) {
            return reject(err);
        }
    });
}
```
[Previouslog](/plugin-api/api/log)

Last updated 7 months ago