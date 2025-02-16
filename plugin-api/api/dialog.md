* [showOpenDialog(options)](#tkp0d)
* [showSaveDialog(options)](#g872m)
* [showMessageBox(options)](#grq5h)
* [showErrorBox(title, content)](#erokr)

1. [API Reference](/plugin-api/api)
# dialog

System dialog functionality, including opening, saving files, prompts, alerts, etc.

Below is an example of a dialog box for selecting multiple files:

Copy
```
let result = await eagle.dialog.showOpenDialog({
    properties: ['openFile', 'multiSelections']
});
```

---

#### Methods

## showOpenDialog(options)

Displays the open file dialog.

* `options` Object

  + `title` string (optional) - The title of the dialog window
  + `defaultPath` string (optional) - The default display path of the dialog
  + `buttonLabel` string (optional) - Custom label for the "Confirm" button; if empty, the default label is used.
  + `filters` [FileFilter](https://www.electronjs.org/zh/docs/latest/api/structures/file-filter)[] (optional)

    - `name` string
    - `extensions` string[]
  + `properties` string[] (optional) - Contains dialog-related attributes. The following attribute values are supported:

    - `openFile` - Allows selecting files
    - `openDirectory` - Allows selecting folders
    - `multiSelections`- Allows multiple selections.
    - `showHiddenFiles`- Displays hidden files in the dialog.
    - `createDirectory` `macOS` - Allows you to create a new directory through the dialog.
    - `promptToCreate` `Windows`- If the entered file path does not exist in the dialog, prompt to create it. This does not actually create a file on the path but allows returning some non-existent addresses for the application to create.
  + `message` string (optional) `macOS` - The message displayed above the input box.
* Returns `Promise<result: Object>`

  + `result`Object

    - `canceled` boolean - Whether the dialog was canceled
    - `filePaths` string[] - Array of chosen file paths by the user. If the dialog is canceled, this will be an empty array.

Copy
```
{
  filters: [
    { name: 'Images', extensions: ['jpg', 'png', 'gif'] },
    { name: 'Movies', extensions: ['mkv', 'avi', 'mp4'] },
    { name: 'Custom File Type', extensions: ['as'] },
    { name: 'All Files', extensions: ['*'] }
  ]
}
```
Copy
```
let result = await eagle.dialog.showOpenDialog({
    properties: ['openFile', 'openDirectory']
});
```

Note: This feature is similar to Electron API's [dialog.showOpenDialog](https://www.electronjs.org/zh/docs/latest/api/dialog#dialogshowopendialogbrowserwindow-options) feature.

---

## showSaveDialog(options)

Displays the save file dialog.

* `options` Object

  + `title` string (optional) - The title of the dialog window
  + `defaultPath` string (optional) - The default display path of the dialog
  + `buttonLabel` string (optional) - Custom label for the "Confirm" button; if empty, the default label is used.
  + `filters` [FileFilter](https://www.electronjs.org/zh/docs/latest/api/structures/file-filter)[] (optional)

    - `name` string
    - `extensions` string[]
  + `properties` string[] (optional) - Contains dialog-related attributes. The following attribute values are supported:

    - `openDirectory` - Allows selecting folders
    - `showHiddenFiles`- Displays hidden files in the dialog.
    - `createDirectory` `macOS` - Allows you to create a new directory through the dialog.
* Returns `Promise<result: Object>`

  + `result`Object

    - `canceled` boolean - Whether the dialog was canceled
    - `filePath` string - If the dialog is canceled, this value will be `undefined`.

Copy
```
{
  filters: [
    { name: 'Images', extensions: ['jpg', 'png', 'gif'] },
    { name: 'Movies', extensions: ['mkv', 'avi', 'mp4'] },
    { name: 'Custom File Type', extensions: ['as'] },
    { name: 'All Files', extensions: ['*'] }
  ]
}
```
Copy
```
let result = await eagle.dialog.showSaveDialog({
    properties: ['openDirectory']
});
```

Note: This function is similar to the Electron API's [dialog.showSaveDialog](https://www.electronjs.org/zh/docs/latest/api/dialog#dialogshowsavedialogbrowserwindow-options) function.

---

## showMessageBox(options)

Display a message dialog.

* `options` Object

  + `message` string - The main content of the dialog
  + `title` string (optional) - Dialog title
  + `detail` string (optional) - Additional information
  + `buttons` strings[] (optional) - Array of button texts
  + `type` string (optional) - Can be `none`, `info`, `error`, `question`, or `warning`
* Returns `Promise<result: Object>`

  + `result` Object

    - `response` Integer - The index of the clicked button

Copy
```
let result = await eagle.dialog.showMessageBox({
    title: "Messagebox title",
    message: "Message from the Plugin process",
    detail: "Ultra message here",
    buttons: ["OK", "Cancel"],
    type: "info"
});
console.log(result);		// {response: 0}
```

This function is similar to the Electron API's [dialog.showSaveDialog](https://www.electronjs.org/zh/docs/latest/api/dialog#dialogshowsavedialogbrowserwindow-options) function.

---

## showErrorBox(title, content)

Display an error message dialog.

* `title` string - The title displayed in the error box
* `content` string - The text content displayed in the error box
* Returns `Promise<void>`

Copy
```
await eagle.dialog.showErrorBox("Error box title", "Error message from the Plugin process");
```

Note: This function is similar to the Electron API's [dialog.showSaveDialog](https://www.electronjs.org/zh/docs/latest/api/dialog#dialogshowsavedialogbrowserwindow-options) function.

###

[PreviouscontextMenu](/plugin-api/api/context-menu)[Nextclipboard](/plugin-api/api/clipboard)

Last updated 1 year ago