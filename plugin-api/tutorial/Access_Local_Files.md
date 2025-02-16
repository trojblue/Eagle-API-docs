* [Using the fs module to access local files](#iamlo)
* [Use native dialogs to get file paths](#nyq1o)

1. [Developer Guide](/plugin-api/tutorial)
# Access Local Files

We can easily use the native Node.js API to implement the functionality of accessing local files. This makes it easier for us to perform such tasks in the plugin system.

---

## Using the `fs` module to access local files

Using a series of methods from Node.js's `fs` module, we can perform operations on the local file system to access local files. For example, you can use the `fs.readFile()` method to read the contents of a file and the `fs.writeFile()` method to write to a file. Here is an example:

Copy
```
const fs = require('fs');
// Read the file
fs.readFile('/path/to/file', (err, data) => {
  if (err) throw err;
  console.log(data);
});
// Write to the file
fs.writeFile('/path/to/file', 'hello world', (err) => {
  if (err) throw err;
  console.log('done');
});
```

These methods are asynchronous, so they won't block the UI, ensuring high performance for the application. Additionally, the `fs` module provides other useful methods, such as using `fs.stat()` to obtain file size, creation time, and other information, or using `fs.rename()` to rename a file. By using the `fs` module, we can conveniently access local files.

**🦄 Best practice:** Avoid using synchronous methods in Node.js as much as possible, as these methods can cause UI thread blocking, leading to a user interface lag and poor user experience. Moreover, using asynchronous methods improves program execution efficiency because it does not block program execution and can handle multiple tasks simultaneously.

---

## Use native dialogs to get file paths

Eagle Plugin API provides a `dialog` module that can be used to create native system dialogs for file saving and selection. Here are some examples:

**Example 1: Pop-up file selection dialog**

Copy
```
let result = await eagle.dialog.showOpenDialog({
    properties: ['openFile', 'openDirectory']
});
```

**Example 2: Pop-up save dialog**

Copy
```
let result = await eagle.dialog.showSaveDialog({
    properties: ['openDirectory']
});
```

If you need a more detailed introduction, you can refer to the [dialog module](/plugin-api/api/dialog).

[PreviousModify Data](/plugin-api/tutorial/modify-eagle-data)[NextIssue Network Requests](/plugin-api/tutorial/network-request)

Last updated 7 months ago