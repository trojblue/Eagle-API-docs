* [Methods](#z1a5y)
* [isDarkColors()](#a6hjz)
* [getPath(name)](#b8lgu)
* [getFileIcon(path[, options])](#ndrop)
* [createThumbnailFromPath(path, maxSize)](#psczp)
* [Properties](#adtwq)
* [version](#f95hw)
* [build](#gwrv2)
* [locale](#dd0fm)
* [arch](#hqmzh)
* [platform](#z5qbr)
* [env](#bdd4y)
* [execPath](#uvg0k)
* [pid](#cldbp)
* [isWindows](#u8kad)
* [isMac](#qw2s4)
* [runningUnderARM64Translation](#kbkmv)
* [theme](#cztqx)

1. [API Reference](/plugin-api/api)
# app

Retrieve Eagle application attributes like version, architecture, and language.

Here are common attributes for the `app`:

Copy
```
console.log(eagle.app.version);                // Eagle version
console.log(eagle.app.build);                  // Eagle Build number
console.log(eagle.app.locale);                 // Application interface language, en/zh_CN/zh_TW/ja_JP
console.log(eagle.app.arch);                   // x86 | x64
console.log(eagle.app.platform);               // darwin | win32
console.log(eagle.app.isWindows);              // true | false, whether the operating system is Windows
console.log(eagle.app.isMac);                  // true | false, whether the operating system is Mac
console.log(eagle.app.runningUnderARM64Translation);   // Whether it is running in rosetta translation mode
```

---

## Methods

## isDarkColors()

Check if the current system is in dark (Dark) mode.

* Returns `boolean` - Whether the current system is in Dark mode.

Copy
```
eagle.app.isDarkColors();        // true | false
```

---

## getPath(name)

You can request the following paths by name:

* `name` string - You can request the following paths by name:

  + `home` - User's home folder (main directory)
  + `appData` - Application data directory for each user, defaults to:
  + `userData` - Folder for storing your application configuration files, default is the appData folder plus the application's name. User data files should be written here by convention, but it is not recommended to write large files, as some environments will back up this directory to cloud storage.
  + `temp` - Temporary folder
  + `exe` - Current executable file
  + `desktop` - Current user's desktop folder
  + `documents` - Path of the user's documents directory
  + `downloads` - Path of the user's download directory
  + `music` - Path of the user's music directory
  + `pictures` - Path of the user's picture directory
  + `videos` - Path of the user's video directory
  + `recent` - Directory of the user's recent files (Windows only).
* Returns `Promise<path: string>` - `path` query path result.

Copy
```
await eagle.app.getPath('appData');   // 'C:\Users\User\AppData\Roaming'
await eagle.app.getPath('pictures');   // 'C:\Users\User\Pictures'
await eagle.app.getPath('desktop');    // 'C:\Users\User\Desktop'
```

Note: This feature is similar to Electron API's [app.getPath](https://www.electronjs.org/zh/docs/latest/api/app#appgetapppath) feature.

---

## getFileIcon(path[, options])

Get the icon associated with the specified path file.

* `path` string - File path for which you want to get the icon
* `options` Object (optional)

  + `size` string
  + `small` - 16x16
  + `normal` - 32x32
  + `large` - 32x32 on `Windows`, not supported on `macOS`.
* Returns `Promise<img: NativeImage>`

  + `img` [NativeImage](https://www.electronjs.org/zh/docs/latest/api/native-image) - A NativeImage type application icon.

Copy
```
let img = await eagle.app.getFileIcon('path_to_file', { size: 'small' });
// Get image information
let base64 = img.toDataURL();
let size = img.getSize();   // {'width': 16, height: 16}
// Save to computer
let buffer = img.toPNG();
require('fs').writeFileSync('output_path/example.png', buffer);
```

Note: This feature is similar to Electron API's [app.getAppIcon](https://www.electronjs.org/zh/docs/latest/api/app#appgetfileiconpath-options) feature.

---

## createThumbnailFromPath(path, maxSize)

Get the icon associated with the file at the specified path.

* `path` string - The file path to get the thumbnail from
* `maxSize` Size - The maximum width and height (positive number) of the returned thumbnail. On Windows platform, maxSize.height will be ignored and height will be scaled according to maxSize.width
* Returns `Promise<img: NativeImage>`

  + `img` [NativeImage](https://www.electronjs.org/zh/docs/latest/api/native-image) - The thumbnail preview image of the file.

Copy
```
let img = await eagle.app.createThumbnailFromPath('path_to_file', {
    height: 200,
    width: 200
});
// Obtain image information
let base64 = img.toDataURL();
let size = img.getSize();	// {'width': 200, height: 150}
// Save to computer
let buffer = img.toPNG();
require('fs').writeFileSync('output_path/example.png', buffer);
```

Note: This function is similar to the Electron API's [nativeImage.createThumbnailFromPath(path, maxSize)](https://www.electronjs.org/zh/docs/latest/api/native-image#nativeimagecreatethumbnailfrompathpath-maxsize-macos-windows) function.

---

## Properties

## version

`string` property, get the current Eagle application version.

## build

`number` property, get the current Eagle application Build Number.

## locale

`string` property, get the current Eagle application interface language.

* `en` - English
* `zh_CN` - Simplified Chinese
* `zh_TW` - Traditional Chinese
* `ja_JP` - Japanese
* `ko_KR` - Korean
* `es_ES` - Spanish
* `de_DE` - German
* `ru_RU` - Russian

## arch

`string` property, returns the CPU architecture of the operating system.

* `x64`
* `arm64`
* `x86`

## platform

`string` property, returns a string identifying the operating system platform.

* `darwin` - macOS operating system
* `win32` - Windows operating system

## env

`Object` property, returns an object of environment variables.

Copy
```
console.log(eagle.app.env);
{
  APPDATA: "C:\\Users\\User\\AppData\\Roaming",
  HOMEDRIVE: "C:",
	HOMEPATH: "\\Users\\User",
  LANG: "zh_TW.UTF-8",
  TEMP: "C:\\Users\\User\\AppData\\Local\\Temp"
}
```
Copy
```
console.log(eagle.app.env['TEMP']);
"C:\\Users\\User\\AppData\\Local\\Temp"
```
## execPath

`string` property, current application execution path.

Copy
```
console.log(eagle.app.execPath);
"C:\\Program Files\\Eagle\\Eagle.exe"
```
## pid

`number` property, current plugin process id.

## isWindows

`boolean` property, is the current operating system Windows.

## isMac

`boolean` property, is the current operating system Mac.

## runningUnderARM64Translation

`boolean` property, when true it indicates that the current application is running in ARM64 runtime (e.g., macOS [Rosetta Translator Environment](https://en.wikipedia.org/wiki/Rosetta_%28software%29) or Windows [WOW](https://en.wikipedia.org/wiki/Windows_on_Windows)).

Hint: This function is similar to the Electron API's [app.runningUnderARM64Translation](https://www.electronjs.org/zh/docs/latest/api/app#apprunningunderarm64translation-%E5%8F%AA%E8%AF%BB-macos-windows) function. You can use this property to prompt users to download the arm64 version of the application when they mistakenly run the x64 version in a translation environment.

## theme

`string` property, the current theme color name, such as `LIGHT`, `LIGHTGRAY`, `GRAY`, `DARK`, `BLUE`, `PURPLE`.

###

[Previouswindow](/plugin-api/api/window)[Nextos](/plugin-api/api/os)

Last updated 7 months ago