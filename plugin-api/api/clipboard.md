* [Methods](#z1a5y)
* [clear()](#tkp0d)
* [has(format)](#p4ult)
* [writeText(text)](#eear5)
* [readText()](#ytddd)
* [writeBuffer(format, buffer)](#ol666)
* [readBuffer(format)](#gadle)
* [writeImage(image)](#cwuzf)
* [readImage()](#hfggy)
* [writeHTML(markup)](#naujl)
* [readHTML()](#btaqx)
* [copyFiles(paths)](#t8sny)

1. [API Reference](/plugin-api/api)
# clipboard

Perform copy and paste operations on the system clipboard.

Tip: It is recommended to use Clipboard Viewer ([Win](https://freeclipboardviewer.com/) / [Mac](https://langui.net/clipboard-viewer/)) tool for development debugging to make the development process smoother.

Copy
```
await eagle.clipboard.writeText('Example string');
console.log(await eagle.clipboard.readText());
```

---

### Methods

## clear()

Clear the clipboard content.

Copy
```
eagle.clipboard.writeText('Example string');
eagle.clipboard.clear();
console.log(eagle.clipboard.readText());	// undefined
```

---

## has(format)

Check if the current clipboard content contains the specified format.

* `format` string - Specified format
* Returns boolean - Whether it contains the specified format

Copy
```
console.log(eagle.clipboard.has('public/utf8-plain-text'));	// false
const buffer = Buffer.from('writeBuffer', 'utf8');
eagle.clipboard.writeBuffer('public/utf8-plain-text', buffer);
console.log(clipboard.has('public/utf8-plain-text'));	// true
```

---

## writeText(text)

Write `text` as plain text to the clipboard.

* `text` string - Text to be written

Copy
```
eagle.clipboard.writeText('Example string');
console.log(eagle.clipboard.readText());	// 'Example string'
```

---

## readText()

Get the plain text content of the current clipboard.

* Returns string

Copy
```
console.log(await eagle.clipboard.readText());
```

---

## writeBuffer(format, buffer)

Write `buffer` as `format` type to the clipboard.

* `format` string - Clipboard format
* `buffer` Buffer - Buffer format of the content to be written

Copy
```
const buffer = Buffer.from('writeBuffer', 'utf8');
eagle.clipboard.writeBuffer('public/utf8-plain-text', buffer);
```

---

## readBuffer(format)

Read `format` type content from the clipboard.

* Returns Buffer

Copy
```
const buffer = Buffer.from('this is binary', 'utf8');
eagle.clipboard.writeBuffer('public/utf8-plain-text', buffer);
const out = eagle.clipboard.readBuffer('public/utf8-plain-text');
console.log(buffer.equals(out));	// true
```

---

## writeImage(image)

Write `image` to the clipboard.

* `image` [NativeImage](https://www.electronjs.org/docs/latest/api/native-image) - Image to be written to the clipboard

Copy
```
let img = nativeImage.createFromPath('path_to_img_file');
eagle.clipboard.writeImage(img);
```

---

## readImage()

Read image format content from the clipboard.

* Returns [NativeImage](https://www.electronjs.org/docs/latest/api/native-image)

Copy
```
let input = nativeImage.createFromPath('path_to_img_file');
eagle.clipboard.writeImage(input);
let output = eagle.clipboard.readImage();
```

---

## writeHTML(markup)

Write `markup` as HTML format to the clipboard.

* `markup` string

Copy
```
eagle.clipboard.writeHTML('<b>Hi</b>');
console.log(eagle.clipboard.readHTML());	// <b>Hi</b>
```

---

## readHTML()

Read HTML format content from the clipboard.

* Returns string

Copy
```
eagle.clipboard.writeHTML('<b>Hi</b>');
console.log(eagle.clipboard.readHTML());	// <b>Hi</b>
```

---

## copyFiles(paths)

Copy the specified files to the clipboard, supporting paste in file manager.

* `paths` strings[] - Files to be copied to the clipboard.

Copy
```
eagle.clipboard.copyFiles([
    'path_to_file',
    'path_to_file2'
]);
```

---

[Previousdialog](/plugin-api/api/dialog)[Nextdrag](/plugin-api/api/drag)

Last updated 1 year ago