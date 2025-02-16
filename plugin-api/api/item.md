* [Methods](#z1a5y)
* [get(options)](#bdcw2)
* [getAll()](#na8ve)
* [getById(itemId)](#katrb)
* [getByIds(itemIds)](#by1ek)
* [getSelected()](#ffgvj)
* [addFromURL(url, options)](#tg9ak)
* [addFromBase64(base64, options)](#zmwst)
* [addFromPath(path, options)](#lnsox)
* [addBookmark(url, options)](#atulp)
* [open(itemId)](#yxkul)
* [Class: Item](#uezi0)
* [save()](#save)
* [moveToTrash()](#movetotrash)
* [replaceFile(filePath)](#replacefile-filepath)
* [refreshThumbnail()](#refreshthumbnail)
* [setCustomThumbnail(thumbnailPath)](#setcustomthumbnail-thumbnailpath)
* [open()](#open)
* [id string](#id-string)
* [name string](#name-string)
* [ext string](#ext-string)
* [width Interger](#width-interger)
* [height Interger](#height-interger)
* [url string](#url-string)
* [isDeleted boolean](#isdeleted-boolean)
* [annotation string](#annotation-string)
* [tags string[]](#tags-string)
* [folders string[]](#folders-string)
* [palettes Object[]](#palettes-object)
* [size Interger](#size-interger)
* [star Interger](#star-interger)
* [importedAt Interger](#importedat-interger)
* [noThumbnail boolean](#nothumbnail-boolean)
* [noPreview boolean](#nopreview-boolean)
* [filePath string](#filepath-string)
* [fileURL string](#fileurl-string)
* [thumbnailPath string](#thumbnailpath-string)
* [thumbnailURL string](#thumbnailurl-string)
* [metadataFilePathstring](#metadatafilepathstring)

1. [API Reference](/plugin-api/api)
# item

The eagle.item API allows you to easily query the current content of the resource library or add new content to the resource library.

Copy
```
eagle.onPluginCreate(async (plugin) => {
    // Get the currently selected file in the Eagle app
    let items = await eagle.item.getSelected();
    let item = items[0];

    // Modify attributes
    item.name = 'New Name';
    item.tags = ['tag1', 'tag2'];

    // Save modifications
    await item.save();
});
```

**🦄 Best Practice:** To ensure data security, use the `item` API provided `save()` method for data access and modification, and avoid directly modifying the `metadata.json` or any files under the Eagle resource library.

---

## Methods

## get(options)

Universal search method that can get files with specified conditions.

* `options` Object - Query conditions

  + `id` string (optional) - File id
  + `ids` string[] (optional) - Array of file ids
  + `isSelected` boolean (optional) - Currently selected files
  + `isUntagged` boolean (optional) - Files that have not been tagged
  + `isUnfiled` boolean (optional) - Files that have not been categorized
  + `keywords` string[] (optional) - Contains keywords
  + `tags` string[] (optional) - Contains tags
  + `folders` string[] (optional) - Contains folders
  + `ext` string (optional) - Format
  + `annotation` string (optional) - Annotation
  + `rating` Integer (optional) - Rating, range from `0 ~ 5`
  + `url` string (optional) - Source URL
  + `shape` string (optional) - Shape, options are `square`, `portrait`, `panoramic-portrait`, `landscape`, `panoramic-landscape`
* Returns `Promise<items: Item[]>` - `items` query result

Copy
```
let items = await eagle.item.get({
    ids: [],
    isSelected: true,
    isUnfiled: true,
    isUntagged: true,
    keywords: [""],
    ext: "",
    tags: [],
    folders: [],
    shape: "square",
    rating: 5,
    annotation: "",
    url: ""
});
let selected = await eagle.item.get({
    isSelected: true
});
let jpgs = await eagle.item.get({
    ext: "jpg"
});
```

---

## getAll()

Return all files.

* Returns `Promise<items: Item[]>` - `items` all files

Copy
```
let items = await eagle.item.getAll();
console.log(items);
```

**🦄 Best Practice:** If the resource library has a large number of files (e.g., 20W+), avoid calling this method without restrictions to avoid reducing application performance.

---

## getById(itemId)

Return the file with the specified ID.

* `itemId` string
* Returns `Promise<item: Item>` - `item` the file with the corresponding ID

Copy
```
let item = await eagle.item.getById('item_id');
console.log(item);
```
## getByIds(itemIds)

Return the files with the specified IDs.

* `itemIds` string[]
* Returns `Promise<items: Item[]>` - `items` the files with the corresponding IDs

Copy
```
let items = await eagle.item.getByIds(['item_id_1', 'item_id_2']);
console.log(items);
```

---

## getSelected()

Return the currently selected files in the application.

* Returns `Promise<items: Item[]>` - `items` selected files

Copy
```
let selected = await eagle.item.getSelected();
console.log(selected);
```

---

## addFromURL(url, options)

Add an image link to Eagle.

* `url`string - The image link to add, supports `http`, `https`, `base64`
* `options` Object

  + `name` string (optional) - File name
  + `website` string (optional) - Source URL
  + `tags` string[] (optional) - Tags
  + `folders` string[] (optional) - Belonging folder IDs
  + `annotation` string (optional) - Annotation
* Returns `Promise<itemId: string>` - `itemId` is the successfully created item ID

Copy
```
const imgURL = 'https://cdn.dribbble.com/userupload/3885520/file/original-ee68b80a6e10edab6f192e1e542da6ed.jpg';
const itemId = await eagle.item.addFromURL(imgURL, {
    name: 'Camping',
    website: 'https://dribbble.com/shots/19744134-Camping-2',
    tags: ["Dribbble", "Illustration"],
    folders: [],
    annotation: 'add from eagle api',
});
```

---

## addFromBase64(base64, options)

Add a base64 image to Eagle.

* `base64`string - Base64 format image
* `options` Object

  + `name` string (optional) - File name
  + `website` string (optional) - Source URL
  + `tags` string[] (optional) - Tags
  + `folders` string[] (optional) - Belonging folder IDs
  + `annotation` string (optional) - Annotation
* Returns `Promise<itemId: string>` - `itemId` is the successfully created item ID

Copy
```
const base64 = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNDAgMjM0IiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAyNDAgMjM0Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZmlsbD0iIzI2MTMwMCIgZD0iTTEwIDEwaDIyMHYyMTMuOTk5aC0yMjB6Ii8+PHBhdGggZD0iTTAgMHYyMzRoMjQwLjAwMXYtMjM0aC0yNDAuMDAxem0xMCAxMGgyMjAuMDAxdjIxNGgtMjIwLjAwMXYtMjE0em03My4yNTIgMTIyLjUwMWwtNy45MiAyOS45ODJjLS4xNjUuODI0LS40OTUgMS4wMTgtMS40ODUgMS4wMThoLTE0LjY4N2MtLjk4OCAwLTEuMTUyLS4zMy0uOTg4LTEuNDg1bDI4LjM4LTk5LjQ0OGMuNDk1LTEuODE1LjgyNS0zLjM3Ny45OS04LjMyOCAwLS42Ni4zMy0uOTkuODI1LS45OWgyMC45NTVjLjY2IDAgLjk5LjE2NSAxLjE1NS45OWwzMS44NDUgMTA3Ljk0Yy4xNjUuODI0IDAgMS4zMi0uODI1IDEuMzJoLTE2LjVjLS44MjQgMC0xLjMxOS0uMTkzLTEuNDg0LS44NTRsLTguMjUtMzAuMTQ2aC0zMi4wMTF6bTI3Ljg4NS0xNi4yNWMtMi44MDUtMTEuMDU2LTkuNDA1LTM1LjI4Ni0xMS44OC00N2gtLjE2NWMtMi4xNDYgMTEuNzE1LTcuNDI1IDMxLjQ5LTExLjU1IDQ3aDIzLjU5NXptNDQuOTkzLTU1LjU3OGMwLTYuNDM1IDQuNDU1LTEwLjIzIDEwLjIzLTEwLjIzIDYuMTA1IDAgMTAuMjMgNC4xMjUgMTAuMjMgMTAuMjMgMCA2LjYtNC4yOSAxMC4yMy0xMC4zOTUgMTAuMjMtNS45NCAwLTEwLjA2NS0zLjYzLTEwLjA2NS0xMC4yM3ptMS4xMiAyMi43MzJjMC0uODI1LjMzLTEuMTU1IDEuMTU1LTEuMTU1aDE1LjY4OWMuODI1IDAgMS4xNTUuMzMgMS4xNTUgMS4xNTV2NzguOTM5YzAgLjgyNi0uMTY1IDEuMTU2LTEuMTU1IDEuMTU2aC0xNS41MjRjLS45OSAwLTEuMzItLjQ5Ni0xLjMyLTEuMzJ2LTc4Ljc3NXoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsPSIjRkY3QzAwIi8+PC9zdmc+';
const itemId = await eagle.item.addFromBase64(base64, {
    name: 'Illustation Logo',
    website: 'https://www.eagle.cool/',
    tags: ["Adobe", "Logo"],
    folders: [],
    annotation: 'ai logo form api',
});
```

---

## addFromPath(path, options)

Add files to Eagle from a local file path.

* `path`string - The file path to add
* `options` Object

  + `name` string (optional) - File name
  + `website` string (optional) - Source URL
  + `tags` string[] (optional) - Tags
  + `folders` string[] (optional) - Belonging folder IDs
  + `annotation` string (optional) - Annotation
* Returns `Promise<itemId: string>` - `itemId` is the successfully created item ID

Copy
```
const filePath = 'C:\\Users\\User\\Downloads\\ai.svg';
const itemId = await eagle.item.addFromPath(filePath, {
    name: 'Illustation Logo',
    website: 'https://www.eagle.cool/',
    tags: ["Adobe", "Logo"],
    folders: [],
    annotation: 'ai logo form api',
});
```

---

## addBookmark(url, options)

Add a bookmark link to Eagle.

* `url`string - The bookmark link to add
* `options` Object

  + `name` string (optional) - Bookmark name
  + `base64` string (optional) - Custom thumbnail in base64 format
  + `tags` string[] (optional) - Tags
  + `folders` string[] (optional) - Belonging folder IDs
  + `annotation` string (optional) - Annotation
* Returns `Promise<itemId: string>` - `itemId` is the successfully created item ID

Copy
```
const bookmarkURL = 'https://www.google.com/';
const itemId = await eagle.item.addBookmark(bookmarkURL, {
    name: 'Eagle',
    tags: ["Eagle", "Site"],
    folders: [],
    annotation: 'bookmark form api',
});
```
Copy
```
const bookmarkURL = 'https://www.google.com/';
const base64 = 'data:image/png;base64,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';
const itemId = await eagle.item.addBookmark(bookmarkURL, {
    name: 'Eagle',
    base64: base64,
    tags: ["Eagle", "Site"],
    folders: [],
    annotation: 'bookmark form api',
});
```

---

## open(itemId)

Display the file corresponding to `itemId` in the full list

* `itemId` string - ID of the file to display
* Returns `Promise<result: boolean>`

Copy
```
await eagle.item.open("item_id");
```

Hint: You can also directly call the `open()` method of the item instance to open the file.

---

## Class: Item

Object type returned by Eagle API `get`, provides modification and save features.

**🦄 Best Practice:** To ensure data security, use `save()` method provided by the Item instance for data access and modification. Avoid directly modifying `metadata.json` or any files in the Eagle repository.

---

#### Instance methods

### **save()**

Save all modifications

* Returns `Promise<result: boolean>` - `result` indicates whether the modification was successful

Copy
```
let item = await eagle.item.getById('item_id');
item.name = 'New Name';
item.tags = ['tag_1', 'tag_2'];
// Save changes
await item.save();
```

---

### **moveToTrash()**

Move the file to the trash.

* Returns `Promise<result: boolean>` - `result` Indicates whether the deletion was successful.

Copy
```
await item.moveToTrash();
```

---

### **replaceFile(filePath)**

Replace the original file with the specified file, automatically refreshing the thumbnail without needing to call `refreshThumbnail()` again.

**🦄 Best Practice:** Directly modifying the file you want to change can be risky. Errors or exceptions during the process may cause file corruption and be irreversible. Therefore, to ensure a more robust operation, first save the new version of the file in another location on your computer. After verifying it's correct, use the `replaceFile()` method to replace it.

* `filePath` string - Path of the file to replace
* Returns `Promise<result: boolean>` - `result` indicates whether the replacement was successful

Copy
```
let item = await eagle.item.getById('item_id');
let result = await item.replaceFile('new_file_path');
console.log(result);
```

---

### **refreshThumbnail()**

Refreshes the file thumbnail, and updates the properties like file size, color analysis, dimensions, etc.

* Returns `Promise<result: boolean>` - `result` indicates whether the operation was successful

Copy
```
let item = await eagle.item.getById('item_id');
let result = await item.refreshThumbnail();
console.log(result);
```

---

### **setCustomThumbnail(thumbnailPath)**

Set a custom thumbnail for the file.

* `thumbnailPath` string - Path of the thumbnail to set
* Returns `Promise<result: boolean>` - `result` indicates whether the replacement was successful

Copy
```
let item = await eagle.item.getById('item_id');
let result = await item.setCustomThumbnail('thumbnail_path');
console.log(result);
```

---

### **open()**

Display this file in the full list

* Returns `Promise<void>`

Hint: You can also directly call the `eagle.item.open(itemId)` method to open the file.

Copy
```
let item = await eagle.item.getById('item_id');
await item.open();
// Equivalent to
await eagle.item.open('item_id');
```

---

#### Instance properties

### `id` **string**

Read-only, file ID.

### `name` **string**

File name.

### `ext` **string**

Read-only, file extension.

### `width` **Interger**

Image width.

### `height` **Interger**

Image height.

### `url` **string**

Source link.

### `isDeleted` **boolean**

Read-only, is the file in the trash.

### `annotation` **string**

File annotation.

### `tags` **string[]**

File tags.

### `folders` **string[]**

Belonging folder ids.

### `palettes` **Object[]**

Read-only, color palette information.

### `size` **Interger**

Read-only, file size.

### `star` **Interger**

Rating information, `0 ~ 5`.

### `importedAt` **Interger**

Read-only, time the file was added.

Copy
```
let date = new Date(item.importedAt);
```
### `noThumbnail` **boolean**

Read-only, the file doesn't have a thumbnail. Files without a thumbnail will be previewed using the original file.

### `noPreview` **boolean**

Read-only, the file is not supported for double-click preview.

### `filePath` **string**

Read-only, returns the file path.

### `fileURL` **string**

Read-only, returns the file URL (`file:///`).

### `thumbnailPath` **string**

Read-only, returns the thumbnail path.

### `thumbnailURL` **string**

Read-only, returns the thumbnail URL (`file:///`). Use this property if you want to display the file in HTML.

### `metadataFilePath`**string**

Read-only, location of the `metadata.json` file for this file.

**🦄 Best Practice:** To ensure data security, use the `item` API provided `save()` method for data access and modifications. Avoid directly modifying `metadata.json`.

###

[Previousevent](/plugin-api/api/event)[Nextfolder](/plugin-api/api/folder)

Last updated 2 months ago