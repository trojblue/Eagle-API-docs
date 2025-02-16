* [startDrag(filePaths)](#tkp0d)

1. [API Reference](/plugin-api/api)
# drag

Implement native system file drag-and-drop functionality.

#### Method

## startDrag(filePaths)

Display notification window

* `filePaths` string[] - File paths to drag
* Returns `Promise<>`

Copy
```
await eagle.drag.startDrag([
    "C:\\Users\\User\\Pictures\\drag1.jpg",
    "C:\\Users\\User\\Pictures\\drag2.jpg",
]);
```

Note: This function is similar to Electron API's [webContents.startDrag(item)](https://www.electronjs.org/en/docs/latest/tutorial/native-file-drag-drop) feature.

####

###

[Previousclipboard](/plugin-api/api/clipboard)[Nextshell](/plugin-api/api/shell)

Last updated 1 year ago