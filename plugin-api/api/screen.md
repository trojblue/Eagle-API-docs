* [Methods](#z1a5y)
* [getCursorScreenPoint()](#tkp0d)
* [getPrimaryDisplay()](#sskcn)
* [getAllDisplays()](#eev58)
* [getDisplayNearestPoint(point)](#ox9dk)

1. [API Reference](/plugin-api/api)
# screen

Get information about screen size, display, cursor position, etc.

## Methods

## getCursorScreenPoint()

Absolute position x, y of the current mouse cursor.

* Returns `Promise<point: Object>`

  + `point` Object

    - `point.x`
    - `point.y`

Copy
```
let point = await eagle.screen.getCursorScreenPoint();
```

---

## getPrimaryDisplay()

Returns primary display information.

* Returns `Promise<display: Display>`

  + `display` [Display](https://www.electronjs.org/docs/latest/api/structures/display) Object - Current display information.

Copy
```
let display = await eagle.screen.getPrimaryDisplay();
```

---

## getAllDisplays()

Returns an array Display[], representing currently available screens.

* Returns `Promise<displays: Display[]>`

  + `displays` [Display](https://www.electronjs.org/docs/latest/api/structures/display)[]

Copy
```
let displays = await eagle.screen.getAllDisplays();
```

---

## getDisplayNearestPoint(point)

Gets the plugin window coordinates x and y.

* `point` Object

  + `point.x` Integer type
  + `point.y` Integer type
* Returns `Promise<display: Display>`

  + `display` [Display](https://www.electronjs.org/docs/latest/api/structures/display) Object - Current display information.

Copy
```
let display = await eagle.screen.getDisplayNearestPoint({ x: 100, y: 100 });
```
[Previousos](/plugin-api/api/os)[Nextnotification](/plugin-api/api/notification)

Last updated 7 months ago