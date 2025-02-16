* [Methods](#z1a5y)
* [create(options)](#xnzds)
* [createSubfolder(parentId, options)](#rys4i)
* [get(options)](#x9nu2)
* [getAll()](#fbdzh)
* [getById(folderId)](#sy5fz)
* [getByIds(folderIds)](#n0gjq)
* [getSelected()](#dsbgj)
* [getRecents()](#dwsxw)
* [open(folderId)](#gjdst)
* [Class: Folder](#uezi0)
* [save()](#save)
* [open()](#open)
* [id string](#id-string)
* [name string](#name-string)
* [description string](#description-string)
* [icon string](#icon-string)
* [iconColor string](#iconcolor-string)
* [createdAt Integer](#createdat-integer)
* [children Folder[]](#children-folder)

1. [API Reference](/plugin-api/api)
# folder

The eagle.folder API allows you to easily create new folders or access existing ones in the current application.

Copy
```
// Get the currently selected folder in the Eagle application
let folder = (await eagle.folder.getSelected())[0];
// Modify properties
folder.name = 'New Folder Name';
folder.description = 'New description...';
// Save changes
await folder.save();
```

**🦄 Best Practice:** To ensure data safety, please use the `save()` method provided by the API for data access and modification. Avoid directly modifying the `metadata.json` or any files under the Eagle resource library.

## Methods

## create(options)

Create a folder.

* `options` Object

  + `name` string - Folder name
  + `description` string (optional) - Folder description
  + `parent` string (optional) - Parent folder ID; with this parameter, it is equivalent to `createSubfolder(parentId, options)`
* Returns `Promise<folder: Folder>` - Successfully created `folder`

Copy
```
let newFolder = await eagle.folder.create({
    name: 'New Folder',
    description: 'Folder\'s description.',
});
```

---

## createSubfolder(parentId, options)

Create a subfolder.

* `parentId` string - Parent folder ID
* `options` Object

  + `name` string - Folder name
  + `description` string (optional) - Folder description
* Returns `Promise<folder: Folder>` - Successfully created `folder`

Copy
```
let parentFolder = await eagle.folder.getById('folder_id');
let subFolder = await eagle.folder.createSubfolder(parentFolder.id, {
    name: 'Subfolder',
    description: 'Subfolder description.',
});
```

---

## get(options)

Get folders with specified conditions.

* `options` Object - Query conditions

  + `id` string (optional) - Folder id
  + `ids` string[] (optional) - Array of folder ids
  + `isSelected` boolean (optional) - Currently selected folders
  + `isRecent` boolean (optional) - Recently accessed folders
* Returns `Promise<folders: Folder[]>` - Query result `folders`

Copy
```
// Get the folder corresponding to the specified id
let folders = await eagle.folder.get({
    ids: ['folder_id1', 'folder_id2']
});
// Get currently selected folders in the application
let folders = await eagle.folder.get({
    isSelected: true
});
```

---

## getAll()

Get all folders.

* Returns `Promise<folders: Folder[]>` - Query result `folders`

Copy
```
let folders = await eagle.folder.getAll();
```

---

## getById(folderId)

Get the folder corresponding to `folderId`.

* `folderId` string - Folder id
* Returns `Promise<folder: Folder>` - Query result `folder`

Copy
```
let folder = await eagle.folder.getById('folder_id');
```

---

## getByIds(folderIds)

Get an array of folders corresponding to `folderIds`.

* `folderIds` string[] - Array of folder ids
* Returns `Promise<folders: Folder[]>` - Query result `folders`

Copy
```
let folders = await eagle.folder.getByIds(['folder_id1', 'folder_id2']);
```

---

## getSelected()

Get the currently selected folders in the application.

* Returns `Promise<folders: Folder[]>` - `folders`

Copy
```
let folders = await eagle.folder.getSelected();
```

---

## getRecents()

Get the recently used folders.

* Returns `Promise<folders: Folder[]>` - `folders`

Copy
```
let folders = await eagle.folder.getRecents();
```

---

## open(folderId)

Eagle will open the folder corresponding to `folderId`.

* Returns `Promise<void>`

Copy
```
await eagle.folder.open('folder_id');
// Equivalent to
let folder = await eagle.folder.getById('folder_id');
await folder.open();
```

Tip: You can also directly call the folder instance's `open()` method to open the folder.

---

## Class: Folder

An Object type returned by the Folder API `get`, provides modification and save functions.

Copy
```
let folder = await eagle.folder.getById('folder_id');
console.log(folder.id);
console.log(folder.name);
folder.name = 'new name';
console.log(folder.name);
await folder.save();
```

**🦄 Best Practice:** To ensure data security, please use the `save()` method provided by the Folder instance for data access and modification, and avoid directly modifying the `metadata.json` or any files under the Eagle repository.

---

#### Instance Methods

### **save()**

Save all modifications.

* Returns `Promise<void>`

Copy
```
let folder = await eagle.folder.getById('folder_id');
folder.name = 'New Folder Name';
// Save modifications
await folder.save();
```

---

### **open()**

Eagle will open this folder.

* Returns `Promise<void>`

Copy
```
let folder = await eagle.folder.getById('folder_id');
await folder.open();
// Equivalent to
await eagle.folder.open('folder_id');
```

Tip: You can also directly call `eagle.folder.open(folderId)` method to open the folder.

---

#### Instance Properties

The `Folder` instance includes the following properties:

### `id` **string**

Read-only, folder id.

### `name` **string**

Folder name.

### `description` **string**

Folder description/introduction.

### `icon` **string**

Read-only, folder icon.

### `iconColor` **string**

Read-only, folder icon color.

### `createdAt` **Integer**

Read-only, folder creation time (timestamp).

Copy
```
let date = new Date(folder.createdAt);
```
### `children` **Folder[]**

Read-only, an array of child folders.

Copy
```
let children = folder.children;
console.log(children[0]);
await children[0].open();
```
###

[Previousitem](/plugin-api/api/item)[Nexttag](/plugin-api/api/tag)

Last updated 10 months ago