* [show()](#kaydt)
* [showInactive()](#reqm4)
* [hide()](#mklts)
* [focus()](#lskqe)
* [minimize()](#de7df)
* [isMinimized()](#v47e2)
* [restore()](#yvcxf)
* [maximize()](#a53af)
* [unmaximize()](#tg6me)
* [isMaximized()](#zxdhs)
* [setFullScreen(flag)](#leibk)
* [isFullScreen()](#irx5v)
* [setAspectRatio(aspectRatio)](#plpcl)
* [setBackgroundColor(backgroundColor)](#no73b)
* [setSize(width, height)](#mq0dz)
* [getSize()](#mq0dz-1)
* [setBounds(bounds)](#setbounds-bounds)
* [getBounds()](#getbounds)
* [setResizable(resizable)](#e56j2)
* [isResizable()](#pyh5l)
* [setAlwaysOnTop(flag)](#p5shn)
* [isAlwaysOnTop()](#quly3)
* [setPosition(x, y)](#erkhe)
* [getPosition()](#ua19x)
* [setOpacity(opacity)](#dlzuz)
* [getOpacity()](#fes0x)
* [flashFrame(flag)](#vxzv7)
* [setIgnoreMouseEvents(ignore)](#yvfx8)
* [capturePage(rect)](#yvfx9)
* [setReferer(url)](#id-4a6f)

1. [API Reference](/plugin-api/api)
# window

Control operations for plugin window display, hide, fullscreen, etc.

Below are common examples of `window` functionalities:

Copy
```
await eagle.window.show();            // Show plugin window
await eagle.window.hide();            // Hide plugin window
await eagle.window.minimize();        // Minimize window
await eagle.window.restore();         // Restore minimized
await eagle.window.maximize();        // Maximize window
await eagle.window.unmaximize();      // Restore maximized
await eagle.window.setFullScreen(true);       // Set to fullscreen
await eagle.window.setFullScreen(false);      // Exit fullscreen
```

---

#### Methods

## show()

Show and focus the window.

* Returns `Promise<>`

Copy
```
await eagle.window.show();
```

---

## showInactive()

Show the window but don't focus on it.

* Returns `Promise<>`

Copy
```
await eagle.window.showInactive();
```

---

## hide()

Hide the plugin window.

* Returns `Promise<>`

Copy
```
await eagle.window.hide();
```

---

## focus()

Give the plugin window focus.

* Returns `Promise<>`

Copy
```
await eagle.window.focus();
```

---

## minimize()

Minimize the plugin window.

* Returns `Promise<>`

Copy
```
await eagle.window.minimize();
```

---

## isMinimized()

Determine if the window is minimized.

* Returns `Promise<minimized: boolean>`

  + `minimized` boolean - Whether the window is minimized

Copy
```
let isMinimized = await eagle.window.isMinimized();
```

---

## restore()

Restore the plugin window from a minimized state to its previous state.

* Returns `Promise<>`

Copy
```
await eagle.window.restore();
```

---

## maximize()

Maximize the plugin window. If the window has not yet been displayed, this method will also show it (but not focus on it).

* Returns `Promise<>`

Copy
```
await eagle.window.maximize();
```

---

## unmaximize()

Unmaximize the plugin window.

* Returns `Promise<>`

Copy
```
await eagle.window.unmaximize();
```

---

## isMaximized()

Determine if the window is maximized.

* Returns `Promise<maximized: boolean>`

  + `maximized` boolean - Whether the window is maximized

Copy
```
let isMaximized = await eagle.window.isMaximized();
```

---

## setFullScreen(flag)

Set whether the window should be in fullscreen mode.

* `flag` boolean - Whether to set as fullscreen
* Returns `Promise<>`

Copy
```
await eagle.window.setFullScreen(true);        // Enter fullscreen
await eagle.window.setFullScreen(false);       // Exit fullscreen
```

---

## isFullScreen()

Determine if the window is in fullscreen mode.

* Returns `Promise<fullscreen: boolean>`

  + `fullscreen` boolean - Whether the window is in fullscreen

Copy
```
let isMaximized = await eagle.window.isMaximized();
```

---

## setAspectRatio(aspectRatio)

This will make the window maintain its aspect ratio.

* `aspectRatio` Float - The aspect ratio to maintain (width / height)
* Returns `Promise<>`

Copy
```
await eagle.window.setAspectRatio(16/9);        // Restrict the window aspect ratio to 16:9
```

---

## setBackgroundColor(backgroundColor)

Set the background color of the window.

* `backgroundColor` String - This parameter represents the HEX code of your desired background color.
* Returns `Promise<>`

Copy
```
await eagle.window.setBackgroundColor("#FFFFFF");
```

Note 1: This property can be set directly in manifest.json.

Note 2: This setting is mainly used to set the default background color of the window when the HTML/CSS content is not yet complete. Proper setting can avoid the flickering of the window display.

---

## setSize(width, height)

Set window size.

* `width` Integer - window width
* `height` - Integer - window height
* Returns `Promise<>`

Copy
```
await eagle.window.setSize(720, 480);
```

Note: This property can be set directly in manifest.json.

## getSize()

Get window size.

* Returns `Promise<Integer[]>`

Copy
```
await eagle.window.getSize();
```
## setBounds(**bounds**)

Adjust the window size and move it to the provided bounds. Any properties not provided will default to their current values.

Copy
```
await eagle.window.setBounds({ x: 440, y: 225, width: 800, height: 600 })
```
## getBounds()

Get window bounds.

* Returns `Promise<Rectangle[]>` - object representing the window bounds

Copy
```
await eagle.window.getBounds()
```
## setResizable(resizable)

Set whether the window supports resizing.

* `resizable` boolean - whether resizing is supported
* Returns `Promise<>`

Copy
```
await eagle.window.setResizable(true);
await eagle.window.setResizable(false);
```

Note: This property can be set directly in manifest.json.

---

## isResizable()

Whether the window supports resizing.

* Returns `Promise<resizable: boolean>`

  + `resizable` boolean

Copy
```
let isResizable = await eagle.window.isResizable();
```

---

## setAlwaysOnTop(flag)

Set whether the window should always be displayed in front of other windows.

* `flag` boolean
* Returns `Promise<>`

Copy
```
await eagle.window.setAlwaysOnTop(true);
await eagle.window.setAlwaysOnTop(false);
```

---

## isAlwaysOnTop()

Whether the window should always be displayed in front of other windows.

* Returns `Promise<alwaysOnTop: boolean>`

  + `alwaysOnTop` boolean

Copy
```
let isAlwaysOnTop = await eagle.window.isAlwaysOnTop();
```

---

## setPosition(x, y)

Move the window to x and y.

* `x` Integer
* `y` Integer
* Returns `Promise<>`

Copy
```
await eagle.window.setPosition(100, 200);
```

---

## getPosition()

Get plugin window coordinates x and y.

* Returns `Promise<position: Integer[]>`

  + `position` Integer[]

    - x - position[0]
    - y - position[1]

Copy
```
let position = await eagle.window.getPosition();  // [100, 200]
```

---

## setOpacity(opacity)

Set the opacity of the window, values outside the range are limited to the [0, 1] range.

* `opacity` number - between 0.0 (completely transparent) and 1.0 (completely opaque)
* Returns `Promise<>`

Copy
```
await eagle.window.setOpacity(0.5);
```

---

## getOpacity()

Get window opacity, between 0.0 (completely transparent) and 1.0 (completely opaque).

* Returns `Promise<opacity: number>`

  + `opacity` number

Copy
```
let opacity = await eagle.window.getOpacity();
```

---

## flashFrame(flag)

Start or stop flashing the window to attract the user's attention.

* `flag` boolean - whether to flash
* Returns `Promise<>`

Copy
```
await eagle.window.flashFrame(true);
await eagle.window.flashFrame(false);
```

---

## setIgnoreMouseEvents(ignore)

Ignore all mouse events within the window. All mouse events occurring in this window will be passed to the window below it but if this window has focus, it will still receive keyboard events.

* `ignore` boolean - whether to ignore mouse events
* Returns `Promise<>`

Copy
```
await eagle.window.setIgnoreMouseEvents(true);
await eagle.window.setIgnoreMouseEvents(false);
```

Combined with the setAlwaysOnTop() feature, you can create a special window that floats at the top of the screen and is permeable to mouse clicks.

## capturePage(rect)

Capture a snapshot of the page within the specified `rect` area. Omitting `rect` will capture the entire visible page.

* `rect` object - Optional, screenshot range

  + `x` number
  + `y` number
  + `width` number
  + `height` number
* Returns `Promise<[NativeImage](https://www.electronjs.org/docs/latest/api/native-image)>`

Copy
```
const image = await eagle.window.capturePage();
const base64 = image.toDataURL("image/jpeg");
const image2 = await eagle.window.capturePage({ x: 0, y: 0, width: 100, height: 50 });
const buffer = image2.toPNG();
```
## setReferer(url)

Sets the current referer URL. Once set, subsequent requests will utilize this referer.

* `url` string - The URL of the referer.
* Returns `void`

Copy
```
eagle.window.setReferer("https://en.eagle.cool");
```
[Previouslibrary](/plugin-api/api/library)[Nextapp](/plugin-api/api/app)

Last updated 6 months ago