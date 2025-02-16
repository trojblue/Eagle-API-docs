* [beep()](#tkp0d)
* [openExternal(url)](#haugb)
* [openPath(path)](#bh5yu)
* [showItemInFolder(path)](#sdnth)

1. [API Reference](/plugin-api/api)
# shell

Manage files and URLs using default applications.

The `shell` module provides functionalities related to desktop integration.

---

#### Methods

## beep()

Plays the system's beep sound.

* Returns `Promise<void>`

Copy
```
await eagle.shell.beep();
```

---

## openExternal(url)

Opens the specified URL using the system's default method. Note: This function will not have any effect if there is no default application set by the system.

* `url` string - The URL to be opened
* Returns `Promise<void>`

Copy
```
await eagle.shell.openExternal('https://www.google.com/');
```

---

## openPath(path)

Opens the specified path using the system's default method.

* `path` string - The file path to be opened
* Returns `Promise<void>`

Copy
```
await eagle.shell.openPath('path_to_file');
```

---

## showItemInFolder(path)

Shows the specified file or folder in the file manager.

* `path` string - The file or folder to be displayed
* Returns `Promise<void>`

Copy
```
await eagle.shell.showItemInFolder('path_to_file_or_directory');
```
###

[Previousdrag](/plugin-api/api/drag)[Nextlog](/plugin-api/api/log)

Last updated 1 year ago