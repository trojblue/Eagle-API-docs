* [Methods](#z1a5y)
* [show(options)](#tkp0d)

1. [API Reference](/plugin-api/api)
# notification

Display a pop-up window in the corner of the screen to inform users about operation status.

## Methods

## show(options)

Display a notification window

* `options` Object

  + `title` string - Notification window title
  + `description` string - Notification window description
  + `icon` URL/base64 - Notification window icon, supporting URL or base64 format (optional)
  + `mute` boolean - Sound effect (optional)
  + `duration` Integer - Auto-hide duration (milliseconds) (optional)
* Returns `Promise<>`

Copy
```
await eagle.notification.show({
    title: "Basic Notification",
    body: "Notification from the Plugin process",
    mute: false,
    duration: 3000,
    icon: "https://"
});
```

---

[Previousscreen](/plugin-api/api/screen)[NextcontextMenu](/plugin-api/api/context-menu)

Last updated 1 year ago